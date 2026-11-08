---
title: "Debugging Hidden GPU Processes in PyTorch"
summary: "When nvidia-smi shows free GPUs but PyTorch throws OOM errors, here's how to find and kill orphaned processes still holding the GPUs."
tags: ["debugging", "pytorch", "gpu"]
description: "How to find orphaned PyTorch and DataLoader processes that hold GPUs after a killed training job when nvidia-smi shows no running processes."
date: 2018-11-02T14:58:10+08:00
lastmod: 2026-11-08
draft: false
---

> **Note**: This post is from 2018. The debugging techniques may still be useful for diagnosing GPU resource leaks where processes hold memory invisibly.

## Background

I was working on semantic segmentation, which is far more memory-intensive than classification—instead of outputting class probabilities, you output dense per-pixel predictions. This means smaller batch sizes per GPU.

The problem is that batch normalization needs a reasonable batch size to compute accurate statistics. With only 2 images per GPU, the mean and standard deviation become unreliable. The solution is synchronized batch normalization, which computes statistics across all GPUs. Combined with PyTorch's multi-worker DataLoader for data loading, this means many subprocesses running alongside your main training script—and that's where the trouble began. (Today, PyTorch ships this as [`torch.nn.SyncBatchNorm`](https://pytorch.org/docs/stable/generated/torch.nn.SyncBatchNorm.html).)

## The Problem

I was running this setup on a cloud GPU cluster with 8 Tesla V100s in a Docker container. After killing my training script (via the cloud GUI), subsequent runs would fail with OOM errors—even though `nvidia-smi` showed all GPUs were free:

```text
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 390.46                 Driver Version: 390.46                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla V100-PCIE...  Off  | 00000000:1A:00.0 Off |                    0 |
| N/A   32C    P0    25W / 250W |     11MiB / 16160MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  Tesla V100-PCIE...  Off  | 00000000:1F:00.0 Off |                    0 |
| N/A   34C    P0    25W / 250W |     11MiB / 16160MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   2  Tesla V100-PCIE...  Off  | 00000000:20:00.0 Off |                    0 |
| N/A   33C    P0    25W / 250W |     11MiB / 16160MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   3  Tesla V100-PCIE...  Off  | 00000000:21:00.0 Off |                    0 |
| N/A   33C    P0    23W / 250W |     11MiB / 16160MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   4  Tesla V100-PCIE...  Off  | 00000000:B2:00.0 Off |                    0 |
| N/A   32C    P0    26W / 250W |     11MiB / 16160MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   5  Tesla V100-PCIE...  Off  | 00000000:B3:00.0 Off |                    0 |
| N/A   35C    P0    26W / 250W |     11MiB / 16160MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   6  Tesla V100-PCIE...  Off  | 00000000:B4:00.0 Off |                    0 |
| N/A   34C    P0    25W / 250W |     11MiB / 16160MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   7  Tesla V100-PCIE...  Off  | 00000000:B5:00.0 Off |                    0 |
| N/A   35C    P0    25W / 250W |     11MiB / 16160MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

But when I tried to start a new training job, I got an OOM error:

```text
RuntimeError: CUDA error (2): out of memory
```

How could I be out of memory when no processes were using the GPUs?

## Step 1: Verify with CUDA APIs

My first instinct was to double-check `nvidia-smi`'s report using CUDA APIs directly. I wrote a quick `check.cu`:

```cpp
#include <iostream>
#include "cuda.h"
#include "cuda_runtime_api.h"

using namespace std;

int main( void ) {
    int num_gpus;
    size_t free, total;
    cudaGetDeviceCount( &num_gpus );
    for ( int gpu_id = 0; gpu_id < num_gpus; gpu_id++ ) {
        cudaSetDevice( gpu_id );
        int id;
        cudaGetDevice( &id );
        cudaMemGetInfo( &free, &total );
        cout << "GPU " << id << " memory: free=" << free << ", total=" << total << endl;
    }
    return 0;
}
```

The output confirmed what `nvidia-smi` showed—all GPUs reported nearly full free memory:

```bash
$ nvcc check.cu -o check && ./check
GPU 0 memory: free=16488464384, total=16945512448
GPU 1 memory: free=16488464384, total=16945512448
GPU 2 memory: free=16488464384, total=16945512448
GPU 3 memory: free=16488464384, total=16945512448
GPU 4 memory: free=16488464384, total=16945512448
GPU 5 memory: free=16488464384, total=16945512448
GPU 6 memory: free=16488464384, total=16945512448
GPU 7 memory: free=16488464384, total=16945512448
```

## Step 2: Test at the PyTorch Level

Since the error came from PyTorch, I tested at that level with a minimal `check.py`:

```python
import torch

if __name__ == '__main__':
    num_gpus = torch.cuda.device_count()
    for gpu_id in range(num_gpus):
        try:
            torch.cuda.set_device(gpu_id)
            torch.randn(1, device='cuda')
            print('GPU {} is good'.format(gpu_id))
        except Exception as e:
            print('GPU {} is bad: {}'.format(gpu_id, e))
```

This revealed the issue:

```bash
$ python3 check.py
GPU 0 is good
GPU 1 is bad: CUDA error: out of memory
THCudaCheck FAIL file=/pytorch/aten/src/THC/THCGeneral.cpp line=663 error=2 : out of memory
GPU 2 is bad: cuda runtime error (2) : out of memory at /pytorch/aten/src/THC/THCGeneral.cpp:663
GPU 3 is good
GPU 4 is good
GPU 5 is good
GPU 6 is good
GPU 7 is good
```

GPUs 1 and 2 were occupied even though `nvidia-smi` and CUDA APIs reported them as free. Something was holding resources that these tools couldn't see.

## Step 3: Find the Hidden Processes

After searching online, I found [@smth](https://discuss.pytorch.org/u/smth/summary)'s suggestion in [this PyTorch forum reply](https://discuss.pytorch.org/t/pytorch-doesnt-free-gpus-memory-of-it-gets-aborted-due-to-out-of-memory-error/13775/14):

> We found that there's actually a bug in python multiprocessing that might keep the child process hanging around, as zombie processes. It is not even visible to `nvidia-smi`.

Strictly speaking, these were not zombies in the Unix sense: a true zombie (a `<defunct>` entry in `ps`) has already exited, holds no resources, and cannot be killed. What I had were orphaned, hung processes that were still alive. Another likely reason `nvidia-smi` showed nothing is that it was running inside a Docker container, where it cannot map GPU processes in other PID namespaces.

The suggested `killall python` didn't work for me, but it pointed me in the right direction: look for processes using the GPU device files directly. The command `fuser -v /dev/nvidia*` lists all processes with handles to the NVIDIA device files:

```bash
$ fuser -v /dev/nvidia*
                     USER        PID ACCESS COMMAND
/dev/nvidia0:        root       5284 F...m python3
                     root       5416 F...m python3
                     root       5417 F...m python3
                     ...
/dev/nvidia1:        root       5284 F...m python3
                     root       5416 F...m python3
                     ...
```

There they were—orphaned Python processes still holding GPU device handles. The main process (PID 5284) and 16 DataLoader worker subprocesses (PIDs 5416-5431) had survived the termination signal and were invisibly occupying the GPUs.

## The Fix

Once identified, the fix was straightforward—kill the orphaned processes. Try `SIGTERM` first so they get a chance to clean up, and fall back to `SIGKILL` only for processes that ignore it:

```bash
$ kill 5284 {5416..5431}      # SIGTERM: ask them to exit
$ kill -9 5284 {5416..5431}   # SIGKILL: only if some are still alive
```

After this, `check.py` confirmed all GPUs were truly available:

```bash
$ python3 check.py
GPU 0 is good
GPU 1 is good
GPU 2 is good
GPU 3 is good
GPU 4 is good
GPU 5 is good
GPU 6 is good
GPU 7 is good
```

## A Hacky Workaround

If the above solution doesn't work, here's a hacky but reliable alternative: add a file-based kill switch to your training loop.

```python
import os
import sys

# Add this check inside your training loop
if os.path.isfile('kill.me'):
    sys.exit(0)
```

When you want to stop training, just run `touch kill.me` in the training directory. The script will exit cleanly on the next iteration. This lets Python shut down the DataLoader workers properly instead of relying on external termination signals. There is no need to call `torch.cuda.empty_cache()` first: all GPU memory held by a process is released by the driver when the process exits.

## Key Takeaways

**1. `nvidia-smi` doesn't show everything.** Orphaned processes can hold GPU device handles without showing memory usage in `nvidia-smi`. Always verify at the level where the problem manifests.

**2. Test at multiple layers.** When debugging resource issues, test at different levels of abstraction: OS tools → CUDA APIs → framework-specific code. This narrows down where the problem actually occurs.

**3. Use `fuser` for device file diagnostics.** The command `fuser -v /dev/nvidia*` reveals processes holding GPU device handles that other tools miss.

**4. Terminate gracefully first.** Send `SIGTERM` before `SIGKILL`, so processes get a chance to clean up; with `SIGKILL`, the order in which you kill them does not matter.

Hope this helps if you run into similar issues.
