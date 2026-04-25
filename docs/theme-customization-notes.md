# Theme Customization Notes

This note is for maintainers. It documents the local Jupyter Book / MyST theme customizations in this repository without adding noise to the main user-facing README.

## Current Status

As of April 24, 2026, the theme customizations for the Colab button were already committed in git before this note was added.

- Commit at `HEAD` when this note was created: `42e1aaf`
- Commit message: `Added a customized theme.`

At that moment, `git status --short` was clean.

## What We Changed

We moved away from patching the downloaded `_build/templates/...` theme at build time and instead vendored the MyST book theme into this repository.

The main goals were:

- make local preview and GitHub Pages deployment deterministic
- avoid fragile runtime patching of generated theme assets
- add a Colab launch button next to the GitHub / edit / download actions on notebook pages

## Where The Custom Theme Lives

The vendored theme is stored here:

- `themes/pyomo-book-theme/`

Important files include:

- `themes/pyomo-book-theme/template.yml`
- `themes/pyomo-book-theme/server.js`
- `themes/pyomo-book-theme/build/index.js`
- `themes/pyomo-book-theme/public/build/manifest-45CD0E76.js`
- `themes/pyomo-book-theme/public/build/routes/$-L6MITV77.js`
- `themes/pyomo-book-theme/public/build/routes/_index-4AIAQW4G.js`
- `themes/pyomo-book-theme/public/build/_shared/chunk-MG6QZF7H-pyomo.js`

The MyST configuration points at the vendored theme via:

- `myst.yml`

## How The Colab Button Works

The Colab button is implemented as a theme-level header action for notebook pages.

Behavior:

- only notebook-backed pages should show the button
- the button URL is derived from the page source URL
- a GitHub notebook URL such as
  `https://github.com/dowlinglab/pyomo-doe/blob/main/notebooks/foo.ipynb`
  is converted to
  `https://colab.research.google.com/github/dowlinglab/pyomo-doe/blob/main/notebooks/foo.ipynb`

Implementation notes:

- the server-rendered theme bundle was updated so the Colab link appears in the initial HTML
- a cache-busted shared client chunk filename was introduced so Safari would not hold onto an old immutable asset after local theme edits
- the final HTML should contain exactly one Colab link per notebook page

## Build / Preview Scripts

These scripts were updated to use the vendored theme flow:

- `scripts/build_local.sh`
- `scripts/publish.sh`

The old patching helper was removed:

- `scripts/patch_book_theme.py`

## Maintenance Guidance

If we revisit this later, the preferred long-term improvement is not to patch compiled bundles by hand again. The cleaner future direction would be:

- make the Colab button a source-level theme action, similar in spirit to the built-in MyST launch button
- rebuild the vendored theme from source
- keep this repo-owned theme as the deployment artifact

That would preserve the determinism of the vendored theme while making the customization easier to reason about.
