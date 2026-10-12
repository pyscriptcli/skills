---
name: ui-consistency
description: "Audit the codebase for design tokens and component patterns, guard UI alignment on all new additions, and apply modern UI/UX and accessibility best practices. Trigger on /ui-consistency, /ui-align, /ui-guard, 'ui consistency', 'audit ui', or when adding/updating frontend components and pages."
---

# UI Consistency: Audit, Align & Guard

Audit the codebase to extract the existing design system, guard against UI drift on every new addition, and enforce modern UI/UX standards with strict antislop discipline.

---

## 1. Simple Names & Triggers

Use these simple aliases and slash commands based on the task:

| Name | Role | When to Use |
| :--- | :--- | :--- |
| **`ui-consistency`** | **Full Pipeline** | Default skill name. Audits codebase tokens, guards consistency, and applies UI/UX best practices. |
| **`ui-audit`** | **Scan & Discover** | Run `/ui-audit` or "audit ui" to inspect the repository for existing colors, fonts, spacing, and components. |
| **`ui-align`** | **Consistency Guard** | Run `/ui-align` or "align ui" to verify and refactor new or existing UI so it matches the design system. |
| **`ui-guard`** | **Drift Prevention** | Proactively invoked before creating any new component to block hardcoded hex values and duplicate styles. |

**Proactive Triggers**:
- Creating a new page, modal, card, form, or UI component.
- Modifying CSS, Tailwind configs, styled-components, or theme tokens.
- Refactoring frontend screens to resolve layout glitches or inconsistent styling.

---

## 2. Core Execution Lifecycle

Always follow this 3-step discipline:

```
[Phase 1: ui-audit] ────────► [Phase 2: ui-guard] ────────► [Phase 3: ui-apply]
 (Scan codebase tokens)       (Prevent drift & rogue styles)  (Implement UI/UX standards)
```

---

### Phase 1: Codebase Audit (`ui-audit`)

Before writing a single line of CSS or markup, audit the codebase to discover the established design tokens:

1. **Locate Design Token Sources**:
   - **Tailwind**: Inspect `tailwind.config.{js,ts,mjs}` or `@theme` blocks in CSS.
   - **CSS Custom Properties**: Check `:root` variables in `globals.css`, `index.css`, `theme.css`, or `styles/`.
   - **Design System Packages**: Check `package.json` for Radix UI, Shadcn/UI, Tailwind, MUI, Chakra, Ant Design, Mantine.
   - **Theme Objects**: Check `theme.ts`, `tokens.ts`, or styled-components/Emotion theme providers.

2. **Extract the 4 Core Token Scales**:
   - **Colors**: Primary, secondary, neutrals (slate/gray/zinc), background, card surface, border, semantic states (success, warning, error, info).
   - **Typography**: Font family, font sizes (`text-xs` through `text-4xl`), line heights, font weights.
   - **Spacing & Layout**: Base grid multiplier (usually 4px or 8px: `gap-2`, `p-4`, `m-6`), max-width container bounds.
   - **Radii & Elevation**: Corner radii (`rounded-sm`, `rounded-md`, `rounded-xl`), border width, box shadows.

3. **Catalog Existing Shared Components**:
   - Search `components/`, `src/components/ui/`, `common/` for existing buttons, inputs, dialogs, badges, and cards.
   - Always reuse existing shared components instead of recreating ad-hoc HTML tags.

---

### Phase 2: Alignment & Consistency Guard (`ui-guard`)

Guard every new or modified UI element against visual drift:

1. **Zero Hardcoded Styles / Arbitrary Values**:
   - ❌ Never write raw arbitrary hex codes (e.g., `color: #3b82f6` or `bg-[#1a202c]`).
   - ✅ Map directly to existing CSS variables or token classes (e.g., `text-primary`, `bg-card`, `border-border`).
   - ❌ Never invent ad-hoc font families or arbitrary font sizes (e.g., `text-[17px]`).
   - ✅ Align with the established typography scale (`text-sm`, `text-base`, `text-lg`).

2. **Reuse Before Reinvent**:
   - If the codebase already has `<Button variant="...">`, use it. Do not write a custom `<button className="...">` with custom padding and hover colors.
   - If icons are sourced from Lucide Icons, use Lucide. Do not pull in raw inline SVGs or a second icon library.

3. **Structural Alignment**:
   - Keep layout margins, card padding, and grid gaps identical across screens.
   - Ensure header heights, sidebars, and navigation patterns follow established layout templates.

---

### Phase 3: UI/UX Standards & Application (`ui-apply`)

Build the interface with production-grade UI/UX best practices and Antislop visual hygiene:

#### A. The 5 Essential UI States
Every interactive element and data container must account for 5 distinct states:
1. **Default**: Clean resting appearance aligned with tokens.
2. **Hover / Focus**: Subtle visual feedback (`hover:bg-muted`, visible `focus-visible:ring-2` outline).
3. **Active / Pressed**: Tactile depression or micro-scale (`active:scale-[0.98]`).
4. **Disabled**: Clear reduced opacity (`opacity-50 pointer-events-none`) with accessible `aria-disabled`.
5. **Loading & Empty**: Skeleton loaders or spinners during async fetching; clean, zero-slop empty states when no data is present.

#### B. Layout Immunity & Responsive Reflow
- **No Overlapping / Absolute Layouts**: Avoid `position: absolute` for page layout. Use Flexbox and CSS Grid.
- **Defensive Sizing**: Always use `min-w-0` on flex children to prevent text truncations or container overflows.
- **Mobile Touch Targets**: Interactive elements must meet a minimum hit target of $44 \times 44\text{px}$ on touch devices.
- **Responsive Breakpoints**: Design mobile-first (`sm:`, `md:`, `lg:`, `xl:`). Ensure smooth reflow from phone screens to ultrawide displays.

#### C. Accessibility & Contrast (WCAG AA Standards)
- **Contrast**: Text and key UI elements must achieve at least a 4.5:1 contrast ratio against their background (3:1 for large text $\ge 24\text{px}$).
- **Semantic HTML**: Prefer native elements (`<button>`, `<dialog>`, `<nav>`, `<aside>`, `<main>`) over `<div onClick=...>` soup.
- **Keyboard Navigation**: Ensure tab order is logical and all interactive elements are reachable and operable via keyboard.

#### D. Antislop Visual Discipline
- **No Generic AI Slop**: Avoid stereotypical purple/indigo neon gradients, gratuitous glassmorphism, or unmotivated bento grids.
- **Meaningful Whitespace**: Let content breathe without artificial floating decorative blobs or random particle animations.
- **Micro-Interactions**: Keep transitions fast ($\le 200\text{ms}$) with ease curves. Respect `prefers-reduced-motion`.

---

## 3. Quick Audit Script / Shell Patterns

When initiating Phase 1, run quick non-destructive commands to extract existing tokens:

```powershell
# 1. Find theme and stylesheet files
Get-ChildItem -Recurse -Depth 3 -Include "*tailwind*.js","*tailwind*.ts","*theme*.ts","*globals.css","*tokens*.json"

# 2. Check installed UI and Icon packages
Select-String -Path "package.json" -Pattern "lucide|radix|shadcn|tailwind|mui|chakra|styled"

# 3. Scan for existing shared UI components
Get-ChildItem -Path "src/components","components" -Directory -Depth 2
```

---

## 4. Standard Delivery Template

Present UI work with this structured, professional format:

```markdown
### 1. Codebase UI Audit Findings
- **Theme & Token Source**: `globals.css` / `tailwind.config.ts` (CSS variables detected)
- **Palette & Typography**: Primary (`--color-primary`), Slate Neutrals, Font: Inter / System Font
- **Reused Components**: `<Button />`, `<Card />`, `<Input />` from `src/components/ui`

### 2. Alignment & Consistency Guard
- **Drift Prevented**: Replaced proposed hardcoded `#1e293b` with `bg-card` token; mapped custom button to shared `<Button variant="secondary">`.
- **States Verified**: Default, Hover, Focus-visible, Disabled, and Skeleton Loading implemented.

### 3. Applied Implementation
[Clean, production-grade, token-aligned component markup and styles]
```
