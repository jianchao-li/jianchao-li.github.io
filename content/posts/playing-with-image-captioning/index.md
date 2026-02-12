---
title: "Image Captioning Demo"
summary: "An interactive browser-based demo that generates natural language captions for images using Transformers.js and the ViT-GPT2 model."
tags: ["Transformers.js", "Machine Learning", "Computer Vision"]
date: 2018-08-08T20:12:45+08:00
lastmod: 2026-02-12
draft: false
---

<div class="project-links" style="text-align: center; margin: 2rem 0;">
  <a href="/demos/image-captioning/" target="_blank" style="display: inline-block; padding: 0.75rem 2rem; background: linear-gradient(135deg, #3b82f6, #8b5cf6); color: white; font-weight: 600; font-size: 1.1rem; border-radius: 0.5rem; text-decoration: none; box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4); transition: transform 0.2s, box-shadow 0.2s;">🚀 Try the Demo</a>
</div>

This demo runs a vision-language model entirely in your browser to generate captions for images. Upload your own image or try one of the sample images to see it in action.

## How It Works

The demo uses [Transformers.js](https://huggingface.co/docs/transformers.js) to run the [ViT-GPT2 image captioning model](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) directly in your browser. No server is required — all inference happens locally on your device.

**Vision Encoder (ViT).** The image is processed by a Vision Transformer that extracts visual features from the image, breaking it into patches and encoding spatial relationships.

**Text Decoder (GPT-2).** The visual features are fed into a GPT-2 language model that generates a natural language caption word by word.

**Browser-Native ML.** Transformers.js converts the model to ONNX format and runs inference via WebAssembly, with WebGL acceleration when available. The model weights (~100MB) are cached in IndexedDB after the first load for faster subsequent visits.

## Privacy

Since the model runs entirely in your browser, your images never leave your device. No data is sent to any server.
