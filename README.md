# ivyzhao.ca

Professional portfolio for Ivy Zhao, built as a dependency-free static site and hosted with GitHub Pages.

## Structure

- `index.html` - positioning and overview
- `about.html` - professional approach and working principles
- `experience.html` - detailed experience timeline
- `projects.html` - selected work and case-study index
- `warframe-publishing-communications.html` - Warframe publishing and communications case study
- `community-leadership.html` - BlightFall and earlier community-leadership case study
- `blightfall-operations.html` - BlightFall operations and product-infrastructure case study
- `resume.html` - prominent resume access
- `contact.html` - contact links
- `changelog.html` - major public content milestones
- `style.css` - shared design system and responsive layouts
- `script.js` - mobile navigation, current year, and reveal behavior
- `assets/ivy-zhao-resume.pdf` - current public resume PDF
- `assets/ivy-zhao-resume-page-1.png` - generated first-page resume preview
- `assets/ivy-zhao-resume-page-1.webp` - optimized first-page resume preview served by the site
- `assets/favicon.svg` and `assets/apple-touch-icon.png` - current browser and device icons
- `assets/fonts/` - locally hosted DM Sans and Newsreader font files with their licenses
- `archive/` - retired site assets and the legacy games/content portfolio reference
- `scripts/validate_site.py` - dependency-free content, link, metadata, UTF-8, and sitemap checks

## Updating the resume

Replace `assets/ivy-zhao-resume.pdf` with the new PDF using the same filename. Also regenerate both first-page preview formats and update the date shown on `resume.html`.

The editable source for the current public resume is stored with Ivy's career materials rather than in this public repository.

## Validation

Run `python scripts/validate_site.py` before publishing. The same validation runs automatically through GitHub Actions on pushes to `main` and pull requests.

## Local preview

Open `index.html` directly or serve the folder with any static file server.

## Publishing

The custom domain is stored in `CNAME`. Keep that file in the repository root when publishing through GitHub Pages.

Files under `archive/` are still public through GitHub Pages. Keep private source material outside this repository.
