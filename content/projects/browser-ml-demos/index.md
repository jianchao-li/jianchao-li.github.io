---
title: "Browser ML Demos"
summary: "Interactive machine learning demos that run entirely in your browser using Transformers.js. No server required — all inference happens locally on your device."
tags: ["Transformers.js", "Machine Learning", "Computer Vision"]
showDate: false
showReadingTime: false
showComments: false
---

A collection of interactive demos showcasing machine learning models running directly in your browser. These demos use [Transformers.js](https://huggingface.co/docs/transformers.js) to run inference locally — **your data never leaves your device**.

---

## Visual Question Answering

Ask questions about images and get natural language answers using the Moondream vision-language model.

<div class="project-links" style="text-align: center; margin: 1.5rem 0;">
  <a href="/demos/vqa/" target="_blank" style="display: inline-block; padding: 0.75rem 2rem; background: linear-gradient(135deg, #3b82f6, #8b5cf6); color: white; font-weight: 600; font-size: 1.1rem; border-radius: 0.5rem; text-decoration: none; box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4); transition: transform 0.2s, box-shadow 0.2s;">Try the Demo</a>
</div>

The demo uses [Moondream2](https://huggingface.co/vikhyatk/moondream2), a lightweight vision-language model designed for efficient inference. Moondream combines SigLIP (a vision encoder) with Phi-1.5 (a compact language model) to understand images and generate natural language answers to your questions.

---

## Image Captioning

Generate natural language captions for images using the ViT-GPT2 model.

<div class="project-links" style="text-align: center; margin: 1.5rem 0;">
  <a href="/demos/image-captioning/" target="_blank" style="display: inline-block; padding: 0.75rem 2rem; background: linear-gradient(135deg, #3b82f6, #8b5cf6); color: white; font-weight: 600; font-size: 1.1rem; border-radius: 0.5rem; text-decoration: none; box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4); transition: transform 0.2s, box-shadow 0.2s;">Try the Demo</a>
</div>

The demo uses [ViT-GPT2](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning), which combines a Vision Transformer (ViT) for image encoding with GPT-2 for caption generation. The model weights (~100MB) are cached in IndexedDB after the first load for faster subsequent visits.

---

## Privacy

Since these models run entirely in your browser, your images never leave your device. No data is sent to any server.
