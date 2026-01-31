# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal website for **Jianchao Li** hosted at https://jianchao-li.github.io.

- **Static Site Generator**: Hugo v0.155.1
- **Theme**: Congo (git submodule at `themes/congo`, stable branch)
- **Color Scheme**: Ocean (blue tones)
- **Deployment**: GitHub Pages via `public/` submodule

## Commands

```bash
# Local development server
hugo server -D
# Or use the helper script:
./view.sh

# Build production site
hugo

# Deploy to GitHub Pages (full workflow)
hugo && cd public && git add -A && git commit -m "Rebuild site" && git push origin master && cd .. && git add public && git commit -m "Update published site" && git push origin master
```

## Repository Structure

```
config/_default/           # Hugo configuration
├── config.toml            # Main config (baseURL, analytics, taxonomies)
├── params.toml            # Theme params (ocean scheme, profile layout, article settings)
├── languages.toml         # Author info, social links
├── menus.toml             # Navigation menu
└── markup.toml            # Goldmark markdown config

content/
├── _index.md              # Homepage
├── about.md               # About page (experience, education)
└── post/                  # Blog posts as page bundles
    └── [post-slug]/
        ├── index.md       # Post content with front matter
        ├── thumb.jpg      # Thumbnail image
        └── *.png          # Post images

assets/img/author.jpg      # Profile picture
static/                    # Favicon files
themes/congo/              # Theme submodule (DO NOT modify)
public/                    # Built site submodule → jianchao-li.github.io
```

## Content Conventions

**Blog posts use page bundles**: Each post is a directory containing `index.md` and its images.

**Post front matter**:
```yaml
---
title: "Post Title"
summary: "Brief description for post listings"
tags: ["tag1", "tag2"]
date: 2025-01-03T22:08:00+01:00
draft: false
---
```

## Git Submodules

| Submodule | Branch | Purpose |
|-----------|--------|---------|
| themes/congo | stable | Hugo theme (upstream: jpanther/congo) |
| public | master | Deployment repo (jianchao-li.github.io) |

After cloning, initialize submodules: `git submodule update --init --recursive`
