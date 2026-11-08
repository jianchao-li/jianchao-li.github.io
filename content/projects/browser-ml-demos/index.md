---
title: "Browser ML Demos"
summary: "Interactive machine learning demos that run entirely in your browser using Transformers.js. No server required — all inference happens locally on your device."
description: "Two Transformers.js demos, visual question answering with Moondream2 and image captioning with ViT-GPT2, that run model inference locally in the browser."
tags: ["transformers.js", "machine-learning", "computer-vision"]
weight: 2
showDate: false
showReadingTime: false
showComments: false
---

A collection of interactive demos showcasing machine learning models running directly in your browser. These demos use [Transformers.js](https://huggingface.co/docs/transformers.js) to run inference locally — **your data never leaves your device**.

<div class="demo-grid">
  <div class="demo-card">
    <h3>Visual Question Answering</h3>
    <p>Ask questions about images and get natural language answers powered by the Moondream vision-language model.</p>
    <div class="tech">Moondream2 (SigLIP + Phi-1.5) · ~1.9 GB download, cached after first visit</div>
    <a href="/demos/vqa/" target="_blank" class="demo-btn">Try Demo</a>
  </div>
  <div class="demo-card">
    <h3>Image Captioning</h3>
    <p>Generate natural language captions for any image using a Vision Transformer and GPT-2 decoder.</p>
    <div class="tech">ViT-GPT2 (8-bit quantized) · ~246 MB download, cached after first visit</div>
    <a href="/demos/image-captioning/" target="_blank" class="demo-btn">Try Demo</a>
  </div>
</div>

## Model downloads

Both demos run on the CPU through ONNX Runtime Web (WebAssembly). The browser downloads the model weights from Hugging Face on the first visit and caches them, so later visits start much faster.

| Demo | Model | Weights loaded | Download |
|---|---|---|---|
| Visual Question Answering | [Xenova/moondream2](https://huggingface.co/Xenova/moondream2) (ONNX export of [vikhyatk/moondream2](https://huggingface.co/vikhyatk/moondream2)) | token embeddings (fp16, 210 MB), vision encoder (fp16, 879 MB), decoder (4-bit, 824 MB) | ~1.9 GB |
| Image Captioning | [Xenova/vit-gpt2-image-captioning](https://huggingface.co/Xenova/vit-gpt2-image-captioning) | encoder (8-bit, 87 MB), decoder (8-bit, 159 MB) | ~246 MB |

The VQA model is large: use a desktop browser on an unmetered connection.

## Privacy

Since these models run entirely in your browser, your images never leave your device. No data is sent to any server.
