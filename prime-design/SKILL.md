---
name: prime-design
description: Apply the PRIME Philippines Project Echo visual system when creating or editing Streamlit pages, components, styling, themes, charts, navigation, forms, or other user-facing UI. Use for design reviews and UI consistency work in Project Echo.
---

# Prime Design

Build interfaces that look native to Project Echo rather than introducing a parallel design system.

## Process

1. Read [the complete Project Echo UI guide](references/project-echo-ui.md) before making UI decisions.
2. Inspect the existing page and shared theme components before editing.
3. Reuse the guide's color tokens, typography, spacing, component classes, layout patterns, and interaction conventions.
4. Route shared page chrome through the existing layout helpers.
5. Use monochrome Material icons or established SVG assets; do not use emoji as UI icons.
6. Keep Streamlit widgets outside raw HTML wrapper elements.
7. Check responsive layout, contrast, focus states, and consistent styling across every edited control.
8. If the implementation changes an established token or pattern, update the reference guide in the same change.

## Constraints

- Do not invent colors or component patterns when an existing token or component fits.
- Do not add a UI framework to reproduce styles already provided by the app.
- Do not leave default Streamlit controls visually inconsistent with surrounding controls.
- Do not claim a pattern exists in code without inspecting it.

