# Personal Website Builder

Source repository for [jianchao-li.github.io](https://jianchao-li.github.io) - the personal website of Jianchao Li.

## Tech Stack

- **Static Site Generator**: [Hugo](https://gohugo.io/) v0.155.1
- **Theme**: [Blowfish](https://github.com/nunocoracao/blowfish)
- **Deployment**: GitHub Pages

## Local Development

```bash
# Start development server
./view.sh
# Or manually:
hugo server -D

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
│   ├── about/           # About page
│   └── post/            # Blog posts
├── static/              # Static assets (favicon)
├── themes/blowfish/     # Theme (git submodule)
└── public/              # Built site (git submodule → GitHub Pages)
```

## License

Content is copyright Jianchao Li. The [Blowfish theme](https://github.com/nunocoracao/blowfish) is MIT licensed.
