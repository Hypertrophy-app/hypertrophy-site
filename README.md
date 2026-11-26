<div align="center">

<img src="https://raw.githubusercontent.com/Hypertrophy-app/.github/main/assets/wordmark.png" alt="Hypertrophy" width="420" />

**Offline-first strength training for Android.**

<sub>[hypertrophy.app](https://hypertrophy.app) &nbsp;&middot;&nbsp; [Issues](https://github.com/Hypertrophy-app/hypertrophy-android/issues) &nbsp;&middot;&nbsp; [Releases](https://github.com/Hypertrophy-app/hypertrophy-android/releases)</sub>

</div>

# hypertrophy-site

The public face of Hypertrophy. Plain HTML and CSS, no build step, no runtime
dependencies. Deployed on Cloudflare Pages at
`https://hypertrophy-app.pages.dev`.

```
public/   The site root. Everything in here is published.
scripts/  Deploy-time checks.
```

## What is here

- `/` - landing page
- `/privacy/` - privacy policy, required by Play Console
- `/terms/` - terms of use
- `/support/` - contact and bug reporting
- `/404.html` - fallback page

The typefaces and their SIL Open Font License texts are copied from the app's
`android/core/designsystem` module so the web and the product use the same
faces. If the app changes its fonts, update them here too.

## Deploy

Publish the `public/` directory as a static upload. No build step runs on
Cloudflare.

```powershell
python scripts/check_links.py
wrangler pages deploy public --project-name hypertrophy-app --branch main
```

The command needs a Wrangler login with Pages write access on the Hypertrophy
Cloudflare account. The production alias is
`https://hypertrophy-app.pages.dev`; every deploy is immutable and the alias
moves to the newest upload.

## Custom domain

`hypertrophy.app` is the canonical host. The domain is delegated to Google
Cloud DNS, not Cloudflare, so the apex cannot be attached to the Pages project
yet. An apex custom domain must be a zone on the Cloudflare account that owns
the Pages project.

To switch hosts:

1. Move the `hypertrophy.app` zone to Cloudflare and add it as a custom domain
   on the `hypertrophy-app` Pages project.
2. Have the privacy policy and terms reviewed and remove the draft notices.
3. Confirm the operating entity and governing jurisdiction in the terms.
4. Update the Play Console privacy URL, store listing, and repository links.

Until then, use `https://hypertrophy-app.pages.dev` for review and testing.

## Local preview

Any static server works:

```powershell
python -m http.server 8000 -d public
```

Then open `http://localhost:8000`. The link checker can be run the same way the
deploy workflow runs it:

```powershell
python scripts/check_links.py
```

## Contributions

Changes to legal pages need a review from the same person who approves the
store submission. Cosmetic changes follow the brand rules in the
[`hypertrophy-brand`](https://github.com/Hypertrophy-app/hypertrophy-brand)
repository.
