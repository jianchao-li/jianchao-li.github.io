---
title: "Visual Question Answering Demo"
summary: "An interactive browser-based demo that answers questions about images using Transformers.js and the Moondream model."
tags: ["Transformers.js", "Machine Learning", "Computer Vision"]
date: 2018-08-27T14:34:35+08:00
lastmod: 2026-02-12
draft: false
---

<div class="project-links" style="text-align: center; margin: 2rem 0;">
  <a href="/demos/vqa/" target="_blank" style="display: inline-block; padding: 0.75rem 2rem; background: linear-gradient(135deg, #3b82f6, #8b5cf6); color: white; font-weight: 600; font-size: 1.1rem; border-radius: 0.5rem; text-decoration: none; box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4); transition: transform 0.2s, box-shadow 0.2s;">🚀 Try the Demo</a>
</div>

This demo runs a vision-language model entirely in your browser to answer questions about images. Upload your own image or try one of the sample images, then ask any question about what you see.

## How It Works

The demo uses [Transformers.js](https://huggingface.co/docs/transformers.js) to run [Moondream2](https://huggingface.co/vikhyatk/moondream2), a lightweight vision-language model designed for efficient inference, directly in your browser. No server is required — all processing happens locally on your device.

**Vision Encoder.** Moondream uses SigLIP, a vision encoder that processes the image into visual embeddings. The image is divided into patches and encoded through transformer layers to capture visual features.

**Language Model.** The visual embeddings are combined with your question and fed into Phi-1.5, a compact but capable language model that generates natural language answers.

**Efficient Architecture.** Moondream is specifically designed for edge deployment, using quantization and architectural optimizations to run efficiently in browsers and on devices with limited resources.

**Answer Generation.** The model generates answers token-by-token, allowing for flexible and natural responses to open-ended questions about image content.

**Browser-Native ML.** Transformers.js converts the model to ONNX format and runs inference via WebAssembly, with WebGL acceleration when available. The model weights are cached in IndexedDB after the first load for faster subsequent visits.

## Privacy

Since the model runs entirely in your browser, your images never leave your device. No data is sent to any server.
