---
title: "Interactive Math Demos"
summary: "Explore fascinating mathematical concepts through interactive visualizations and simulations — right in your browser."
tags: ["Math", "Visualization", "Interactive"]
weight: 3
showDate: false
showReadingTime: false
showComments: false
---

A collection of interactive demos that bring mathematical concepts to life. Play with numbers, run simulations, and see the math unfold visually.

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
  cursor: pointer;
  text-decoration: none !important;
  color: inherit !important;
  display: block;
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
  background: linear-gradient(135deg, #0d9488, #2563eb);
  color: white !important;
  font-weight: 600;
  font-size: 0.95rem;
  border-radius: 0.5rem;
  text-decoration: none !important;
  box-shadow: 0 4px 14px rgba(13, 148, 136, 0.3);
  transition: transform 0.2s, box-shadow 0.2s;
}
.demo-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(13, 148, 136, 0.4);
}
</style>

<div class="demo-grid">
  <a href="/demos/collatz/" target="_blank" class="demo-card">
    <h3>Collatz Conjecture</h3>
    <p>Enter any positive integer and watch its Collatz sequence unfold. Will it always reach 1? One of math's most famous unsolved problems.</p>
    <div class="tech">Chart.js &middot; Animated visualization</div>
    <span class="demo-btn">Try Demo</span>
  </a>
  <a href="/demos/monty-hall/" target="_blank" class="demo-card">
    <h3>Monty Hall Problem</h3>
    <p>Play the classic game show puzzle interactively. Pick a door, decide whether to switch, and watch the probabilities converge.</p>
    <div class="tech">Interactive simulation &middot; Statistics tracker</div>
    <span class="demo-btn">Try Demo</span>
  </a>
  <a href="/demos/galton-board/" target="_blank" class="demo-card">
    <h3>Galton Board</h3>
    <p>Drop balls through a grid of pegs and watch them pile up into a bell curve. See the binomial distribution emerge from pure randomness.</p>
    <div class="tech">Canvas animation &middot; Normal distribution</div>
    <span class="demo-btn">Try Demo</span>
  </a>
</div>
