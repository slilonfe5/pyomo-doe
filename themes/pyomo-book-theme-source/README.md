# Source-Derived Theme Notes

This directory is reserved for notes related to the source-derived custom theme workflow.

The active source-derived theme now comes from the git subtree at:

- `vendor/myst-theme/themes/book`

When we revisit the Colab button customization, the plan is:

1. Make source-level edits in the separate `dowlinglab/myst-theme` fork.
2. Test the fork locally against `pyomo-doe`.
3. Pull the updated fork back into this repo with `git subtree`.

Why this exists:

- `../pyomo-book-theme/` is a preserved prototype built from compiled artifacts.
- That prototype is useful for reference, but it is not the recommended maintenance base.
- This directory marks the clean path we want to use going forward.
