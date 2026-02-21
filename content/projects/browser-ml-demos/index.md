---
title: "Browser ML Demos"
summary: "Interactive machine learning demos that run entirely in your browser using Transformers.js. No server required — all inference happens locally on your device."
tags: ["Transformers.js", "Machine Learning", "Computer Vision"]
weight: 2
showDate: false
showReadingTime: false
showComments: false
---

A collection of interactive demos showcasing machine learning models running directly in your browser. These demos use [Transformers.js](https://huggingface.co/docs/transformers.js) to run inference locally — **your data never leaves your device**.

<style>
.demo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}
.demo-card {
  border: 1px solid var(--color-neutral-200);
  border-radius: 0.75rem;
  padding: 1.5rem;
  background: var(--color-neutral-50);
  transition: transform 0.2s, box-shadow 0.2s;
}
.dark .demo-card {
  border-color: var(--color-neutral-700);
  background: var(--color-neutral-800);
}
.demo-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}
.dark .demo-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}
.demo-card h3 {
  margin: 0 0 0.75rem 0;
  font-size: 1.25rem;
}
.demo-card p {
  margin: 0 0 1rem 0;
  color: var(--color-neutral-600);
  font-size: 0.95rem;
  line-height: 1.5;
}
.dark .demo-card p {
  color: var(--color-neutral-400);
}
.demo-card .tech {
  font-size: 0.8rem;
  color: var(--color-neutral-500);
  margin-bottom: 1rem;
}
.demo-btn {
  display: inline-block;
  padding: 0.6rem 1.5rem;
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  color: white !important;
  font-weight: 600;
  font-size: 0.95rem;
  border-radius: 0.5rem;
  text-decoration: none !important;
  box-shadow: 0 4px 14px rgba(59, 130, 246, 0.3);
  transition: transform 0.2s, box-shadow 0.2s;
}
.demo-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
}
</style>

<div class="demo-grid">
  <div class="demo-card">
    <h3>Visual Question Answering</h3>
    <p>Ask questions about images and get natural language answers powered by the Moondream vision-language model.</p>
    <div class="tech">Moondream2 · SigLIP · Phi-1.5</div>
    <a href="/demos/vqa/" target="_blank" class="demo-btn">Try Demo</a>
  </div>
  <div class="demo-card">
    <h3>Image Captioning</h3>
    <p>Generate natural language captions for any image using a Vision Transformer and GPT-2 decoder.</p>
    <div class="tech">ViT-GPT2 · ~100MB cached</div>
    <a href="/demos/image-captioning/" target="_blank" class="demo-btn">Try Demo</a>
  </div>
</div>

## Privacy

Since these models run entirely in your browser, your images never leave your device. No data is sent to any server.
