<div align="center">

<span style="display: inline-block; padding: 18px 30px; background-color: #0D0D0F; border-radius: 14px;"><img src="https://raw.githubusercontent.com/Hypertrophy-app/.github/main/assets/wordmark.png" alt="Hypertrophy" width="420" style="max-width: 100%; height: auto;" /></span>

**Offline-first strength training for Android.**

<sub>[hypertrophy.app](https://hypertrophy.app) &nbsp;&middot;&nbsp; [Issues](https://github.com/Hypertrophy-app/hypertrophy-android/issues) &nbsp;&middot;&nbsp; [Releases](https://github.com/Hypertrophy-app/hypertrophy-android/releases)</sub>

</div>

# hypertrophy-site

The public face of Hypertrophy. Plain HTML and CSS, no build step, no runtime
dependencies, hosted on GitHub Pages at `hypertrophy.app`.

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

## Before going live

1. Have the privacy policy and terms reviewed. Both pages carry a visible
   draft notice that must be removed when approved.
2. Confirm the operating entity and governing jurisdiction in the terms.
3. Point DNS at GitHub Pages:
   - `A` records for the apex at `185.199.108.153`, `185.199.109.153`,
     `185.199.110.153`, `185.199.111.153`; or an `ALIAS`/`ANAME` record where
     the registrar supports it.
   - `CNAME` record for `www` pointing to `hypertrophy.app`.
   - `public/CNAME` already declares `hypertrophy.app` as the canonical host.
4. In repository settings, set Pages source to **GitHub Actions** and enable
   HTTPS enforcement.
5. Trigger **Deploy site** manually once, verify every page over HTTPS, then
   change the workflow trigger from `workflow_dispatch` to a push on `main`.

The domain is registered and delegated to Google Cloud DNS but had no A record
when this repository was created. The link is therefore aspirational until step
3 is done.

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
