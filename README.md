# Personal Website Builder

Source repository for [jianchao.xyz](https://www.jianchao.xyz) — the personal website and blog of Jianchao Li.

## Tech Stack

- **Static Site Generator**: [Hugo](https://gohugo.io/) v0.155.1 (pinned in CI). Blowfish declares support for Hugo up to 0.154.5, so builds print a harmless module-compatibility warning.
- **Theme**: [Blowfish](https://github.com/nunocoracao/blowfish)
- **Styling**: Tailwind CSS (via Blowfish)
- **Deployment**: GitHub Pages via GitHub Actions
- **Analytics**: Google Analytics
- **Comments**: [Giscus](https://giscus.app/) (GitHub Discussions)

## Local Development

```bash
# Start development server
hugo server --printI18nWarnings

# Visit http://localhost:1313
```

## Build & Deploy

Pushes to the `master` branch automatically trigger a [GitHub Actions workflow](.github/workflows/hugo.yml) that builds the site with `hugo --minify` and deploys it to GitHub Pages.

## Repository Structure

```
jianchao-li.github.io/
├── .github/workflows/   # GitHub Actions deployment workflow
├── assets/
│   ├── css/custom.css   # Custom style overrides
│   └── img/             # Author image
├── config/_default/     # Hugo configuration (site, params, menus, languages)
├── content/
│   ├── about/           # About page with professional timeline
│   ├── posts/           # Blog posts
│   ├── projects/        # Project showcases
│   └── tags/            # Tag display titles and aliases
├── layouts/
│   ├── _default/_markup/  # Math passthrough render hooks (KaTeX)
│   ├── partials/
│   │   ├── _funcs/get-page-images.html  # Social images (og:image) served at 1200x630
│   │   ├── comments.html                # Giscus comments
│   │   └── home/profile.html            # Homepage profile with projects grid
│   ├── 404.html         # Custom 404 page
│   ├── home.rss.xml     # Home RSS feed: posts only
│   └── robots.txt       # robots.txt template
├── static/
│   ├── demos/           # Standalone interactive demos (math, browser ML)
│   └── ...              # Favicons, CNAME
└── themes/blowfish/     # Blowfish theme (git submodule)
```

## License

Content is copyright Jianchao Li. The [Blowfish theme](https://github.com/nunocoracao/blowfish) is MIT licensed.
