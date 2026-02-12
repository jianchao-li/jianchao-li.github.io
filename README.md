# Personal Website Builder

Source repository for [jiaochao.xyz](https://jianchao.xyz) — the personal website and blog of Jianchao Li.

## Tech Stack

- **Static Site Generator**: [Hugo](https://gohugo.io/) v0.155.1
- **Theme**: [Blowfish](https://github.com/nunocoracao/blowfish)
- **Styling**: Tailwind CSS (via Blowfish)
- **Deployment**: GitHub Pages via GitHub Actions
- **Analytics**: Google Analytics
- **Comments**: [Giscus](https://giscus.app/) (GitHub Discussions)

## Local Development

```bash
# Start development server
./view.sh
# Or manually:
hugo server --printI18nWarnings

# Visit http://localhost:1313
```

## Build & Deploy

Pushes to the `master` branch automatically trigger a [GitHub Actions workflow](.github/workflows/hugo.yml) that builds the site with `hugo --minify` and deploys it to GitHub Pages.

## Repository Structure

```
website-builder/
├── .github/workflows/   # GitHub Actions deployment workflow
├── assets/
│   ├── css/custom.css   # Custom style overrides
│   └── img/             # Author image
├── config/_default/     # Hugo configuration (site, params, menus, languages)
├── content/
│   ├── about/           # About page with professional timeline
│   ├── post/            # Blog posts
│   └── projects/        # Project showcases
├── layouts/
│   ├── partials/        # Custom partials (analytics, comments)
│   ├── 404.html         # Custom 404 page
│   └── robots.txt       # robots.txt template
├── static/              # Favicons and static assets
└── themes/blowfish/     # Blowfish theme (git submodule)
```

## License

Content is copyright Jianchao Li. The [Blowfish theme](https://github.com/nunocoracao/blowfish) is MIT licensed.
