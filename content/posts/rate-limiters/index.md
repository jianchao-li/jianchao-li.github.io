---
title: "Rate Limiters"
summary: "I will explain five algorithms for rate limiters with example Python implementation: token bucket, leaky bucket, fixed window counter, sliding window log and sliding window counter."
tags: ["software-engineering", "system-design", "rate-limiting"]
description: "An explanation of five rate limiting algorithms."
date: 2026-06-19T14:45:22+02:00
lastmod: 2026-06-19
draft: false
---

I recently read about [rate limiting](https://en.wikipedia.org/wiki/Rate_limiting) in Alex Xu's [System Design Interview - An Insider's Guide](https://www.amazon.com/System-Design-Interview-insiders-Second/dp/B08CMF2CQF) (you can find a copy [here](https://bytes.usc.edu/~saty/courses/docs/data/SystemDesignInterview.pdf)). It nicely illustrates five algorithms for rate limiting: token bucket, leaky bucket, fixed window counter, sliding window log, sliding window counter.

Reading something from a great book can easily give me an illusion of understanding it. So I decided to implement the five algorithms myself to check whether I have grasped the nitty gritty.

**Disclaimer**: I won't go over the algorithms in details in this post, you can read them from pages 54 to 62 on the above copy. Moreover, all the following implementations are based on my understanding and are meant to explain the algorithms, rather than replicating what an actual implementation looks like in real-world systems.

# Interface

For rate limiters, its core interface boils down to the follows: it takes a `request` that contains a `timestamp` and decides whether to accept or reject it.

```python
from dataclasses import dataclass

@dataclass
class Request:
	timestamp: int

class RateLimiter:
	def accept(self, request: Request) -> bool:
	    pass
```

# Token bucket

In token bucket, you have a bucket that contains a specified number of tokens (`bucket_size`; note that this has nothing to do with the tokens in LLMs), when a request comes, it consumes one token to be processed; tokens are refilled in a specified rate (`refill_rate`). **All rates are defined for one minute in the following implementations.**

```python
SECONDS_TO_MINUTES = 1 / 60

class TokenBucket:
    def __init__(self, bucket_size: int, refill_rate: float):
        self.bucket_size = bucket_size
        self.refill_rate = refill_rate
        self.tokens = bucket_size. # Number of remaining tokens
        self.last = None  # Timestamp of the last arrived request

    def accept(self, request: Request) -> bool:
        if self.last is None:
            # First request
            self.last = request.timestamp
            self.tokens -= 1
            return True
		 
        # Compute how many tokens are refilled
        delta = request.timestamp - self.last
        self.tokens = min(
            self.bucket_size,
            self.tokens + self.refill_rate * delta * SECONDS_TO_MINUTES,
        )
        
        self.last = request.timestamp

        if self.tokens < 1:
            return False

        self.tokens -= 1
        return True
```

# Leaky bucket

Leaky bucket is similar to token bucket. You have a bucket which has a specified size (`bucket_size`), and it leaks in a specified rate (`leak_rate`). You can think of it as a fixed-size queue that you can add the requests to it, and those requests are processed and dequed at a certain rate. The code is very similar to that of token bucket.

```python
class LeakyBucket:
    def __init__(self, size: int, leak_rate: float) -> None:
        self.size = size
        self.rate = leak_rate
        self.level = 0.0  # How many slots remain in the bucket
        self.last = None

    def accept(self, request: Request) -> bool:
        if self.last is None:
            self.last = request.timestamp
            self.level = 1
            return True

        # Compute how many slots are leaked
        delta = request.timestamp - self.last
        self.level = max(0.0, self.level - self.rate * delta * SECONDS_TO_MINUTES)
        self.last = req.timestamp

        if self.level >= self.size:
            return False

        self.level += 1
        return True
```

# Fixed window counter

Fixed window counter divides the time into fixed-sized windows (**we use 60-second time windows for all following algorithms**). A counter (`count`) is used to track how many requests are accepted for each window. Only if the counter doesn't exceed a limit (`limit`) will the request be accepted.

```python
class FixedWindowCounter:
    def __init__(self, limit: int, window: int = 60) -> None:
        self.limit = limit
        self.window = window
        self.start = None  # The stating timestamp of the current window
        self.count = 0

    def accept(self, request: Request) -> bool:
        window_start = int(request.timestamp // self.window)

        if self.start != window_start:
            self.start = window_start
            self.count = 0

        if self.count >= self.limit:
            return False

        self.count += 1
        return True
```

# Sliding window log

Fixed window counter has the problem of accepting more requests when there is a burst of requests near the window boundaries. Sliding window log fixes this by using a sliding window: when a request arrives, we treat its timestamp as the end of the window, and check whether the accepted requests in this window has exceeded the limit.

```python
class SlidingWindowLog:
    def __init__(self, limit: int, window: int = 60) -> None:
        self.limit = limit
        self.window = window
        self.q = deque()

    def accept(self, request: Request) -> bool:
        cutoff = req.timestamp - self.window

        # Remove requests that are out of the window ending at the current timestamp
        while self.q and self.q[0] <= cutoff:
            self.q.popleft()

        if len(self.q) >= self.limit:
            return False

        self.q.append(request.timestamp)
        return True
``` 

# Sliding window counter

Sliding window counter is a combination of fixed window counter and sliding window log, by calculating the number of accepted requests in the sliding window as the sum of #requests in the current fixed window and the #requests in the previous fixed window multiplied by the overlap percentage of the sliding window and the previous fixed window. If you have difficulties understand what this means, Figure 4-11 in the copy of Alex's book should make it clear.

```python
class SlidingCounter:
    def __init__(self, limit: int, window: int = 60) -> bool:
        self.limit = limit
        self.window = window
        self.curr_start = None  # Index of the current fixed window
        self.curr = 0  # Number of requests in the current fixed window
        self.prev = 0  # Number of requests in the previous fixed window

    def _start(self, t: float) -> int:
        # Get the index of the fixed window containing t
        return int(t // self.window)

    def accept(self, request: Request) -> bool:
        w = self._start(req.timestamp)

        if self.curr_start is None:
            # First request
            self.curr_start = w
            self.curr = 0

        if w != self.curr_start:
            # A new fixed window
            self.prev = self.curr
            self.curr = 0
            self.curr_start = w

        # Clamp the weight to be [0, 1]
        weight = max(0.0, min(1.0, 1 - ((req.timestamp % self.window) / self.window)))
        effective = self.curr + self.prev * weight

        if effective >= self.limit:
            return False

        self.curr += 1
        return True
```

# Simulation: burst of traffic near window boundaries

An interesting case to simulate is when there is a burst of traffic near window boundaries. This should reveal the issue of fixed window counter. The simulation is done as follows.

```python
def generate_requests():
    requests = []
    # Burst right before the boundary
    for _ in range(100):
        requests.append(Request(59.9))
    # Burst immediately after the boundary
    for _ in range(100):
        requests.append(Request(60.1))
    return requests

def run():
    reqs = generate_requests()

    algorithms = {
        "token": TokenBucket(100, 100),
        "leaky": LeakyBucket(100, 100),
        "fixed": FixedWindow(100),
        "sliding_log": SlidingLog(100),
        "sliding_counter": SlidingCounter(100),
    }

    results = {k: 0 for k in algorithms}

    for r in reqs:
        for name, alg in algorithms.items():
            if alg.accept(r):
                results[name] += 1

    for k, v in results.items():
        print(f"{k:15s}: {v}")


if __name__ == "__main__":
    run()
```

The following is the result we obtain. As can be seen, fixed window counter allows all 200 requests while all other algorithms allow rougly 100 requests as intended.

```
token          : 100
leaky          : 101
fixed          : 200
sliding_log    : 100
sliding_counter: 101
```