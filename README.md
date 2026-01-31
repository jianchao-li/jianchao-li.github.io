# Personal Website Builder

Source repository for [jianchao-li.github.io](https://jianchao-li.github.io) - the personal website of Jianchao Li.

## Tech Stack

- **Static Site Generator**: [Hugo](https://gohugo.io/) v0.155.1
- **Theme**: [Congo](https://github.com/jpanther/congo)
- **Deployment**: GitHub Pages

## Local Development

```bash
# Start development server
./view.sh
# Or manually:
hugo server --printI18nWarnings

# Visit http://localhost:1313
```

## Build & Deploy

```bash
# Build the site
hugo

# Deploy to GitHub Pages
cd public
git add -A
git commit -m "Rebuild site"
git push origin master
cd ..

# Update main repo
git add public
git commit -m "Update published site"
git push origin master
```

## Repository Structure

```
website-builder/
├── config/_default/     # Hugo configuration
├── content/
│   ├── post/            # Blog posts
│   └── publication/     # Academic publications
├── static/              # Static assets (favicon)
├── themes/congo/        # Theme (git submodule)
└── public/              # Built site (git submodule → GitHub Pages)
```

## License

Content is copyright Jianchao Li. The [Congo theme](https://github.com/jpanther/congo) is MIT licensed.
