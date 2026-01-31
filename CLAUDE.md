# CLAUDE.md - Project Context for Claude

## Project Overview

This is a personal website for **Jianchao Li** hosted at https://jianchao-li.github.io.

- **Static Site Generator**: Hugo v0.155.1
- **Theme**: Congo (git submodule at `themes/congo`)
- **Color Scheme**: Ocean (blue tones)
- **Deployment**: GitHub Pages via `public/` submodule

## Repository Structure

```
website-builder/
├── assets/img/author.jpg      # Profile picture
├── config/_default/           # Hugo configuration
│   ├── config.toml            # Main config
│   ├── params.toml            # Theme params (ocean scheme, profile layout)
│   ├── languages.toml         # Author info, social links
│   ├── menus.toml             # Navigation menu
│   └── markup.toml            # Goldmark markdown config
├── content/
│   ├── _index.md              # Homepage
│   ├── about.md               # About page (experience, education)
│   └── post/                  # Blog posts (8 posts on ML/DL topics)
├── static/                    # Favicon files
├── themes/congo/              # Theme submodule
└── public/                    # Built site (submodule → jianchao-li.github.io)
```

## Deployment Workflow

```bash
# 1. Build the site
hugo

# 2. Deploy to GitHub Pages
cd public
git add -A
git commit -m "Rebuild site"
git push origin master
cd ..

# 3. Update main repo
git add public
git commit -m "Update published site"
git push origin master
```

## Local Development

```bash
hugo server -D
# Visit http://localhost:1313
```

## Git Submodules

| Submodule | URL | Purpose |
|-----------|-----|---------|
| themes/congo | https://github.com/jpanther/congo.git | Hugo theme |
| public | git@github.com:jianchao-li/jianchao-li.github.io.git | GitHub Pages deploy |

## Content Notes

- Blog posts are in `content/post/*/index.md` (page bundles with images)
- Posts cover: deep learning, PyTorch, computer vision, investing
- Navigation: Posts → About
