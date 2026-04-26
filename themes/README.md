# Themes

This directory is for maintainer-only theme work.

Current state:

- The preferred active theme path is the source-derived subtree at `vendor/myst-theme/themes/book`.
- `pyomo-book-theme/` is a preserved compiled-theme prototype that previously added a Colab header button.
- We are intentionally not editing `pyomo-book-theme/` further by hand, because it contains build artifacts rather than source files intended for maintenance.

Recommended future path:

1. Use `vendor/myst-theme` as the reusable source-derived theme subtree.
2. Keep source-level customization work in the separate `dowlinglab/myst-theme` fork.
3. Pull updates into this repo with `git subtree`.
4. Treat `pyomo-book-theme/` only as historical reference unless explicitly needed.

Useful maintainer helpers:

- `bash scripts/set_theme.sh stock`
- `bash scripts/set_theme.sh subtree`
- `bash scripts/set_theme.sh prototype`

Additional notes live in:

- `docs/theme-customization-notes.md`
