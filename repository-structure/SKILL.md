---
name: repository-structure
description: Create a clean frontend/backend repository structure with consistent names, small modules, and shared code in one place.
---

# Repository Structure

## Rule zero

Pick one naming rule. Do it everywhere.

- folders/files: `kebab-case`
- functions/variables: `camelCase`
- classes/components/types: `PascalCase`
- constants: `UPPER_SNAKE_CASE`
- tests: same file name + `.test`

No mixed naming. No random caps.

## Main shape

```text
.
├── README.md
├── docs/
├── apps/
│   ├── frontend/
│   │   └── src/
│   │       ├── pages/
│   │       ├── components/
│   │       ├── features/
│   │       ├── utils/
│   │       ├── hooks/
│   │       ├── services/
│   │       ├── state/
│   │       ├── styles/
│   │       └── assets/
│   └── backend/
│       └── src/
│           ├── api/
│           ├── auth/
│           ├── db/
│           ├── ai/
│           ├── services/
│           ├── utils/
│           ├── config/
│           └── middleware/
├── packages/
│   ├── types/
│   └── utils/
├── scripts/
└── .github/
```

## Rules

- Root is repo stuff. Not code soup.
- Folder name says what lives there.
- Keep folders small. Split before pile gets huge.
- One file = one clear job.
- One function = one clear action.
- Frontend does not import backend.
- Backend does not import frontend.
- Shared code goes in `packages/`. One home. One change.
- Test files use same naming rule as source.
- Big subsystem? Add small `README.md` inside it.

## Quick check

1. Who owns this: frontend, backend, shared?
2. What job: auth, api, db, ai, component, page, util?
3. Can folder + name explain it without opening file?
4. Does name match everything else?

If no: move or rename now.
