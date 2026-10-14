# Using Agent Skills with Antigravity CLI

Install this folder as a local Antigravity plugin from the parent `pyscriptcli/skills` checkout:

```bash
agy plugin install ./agent-skills-antislop
```

Check the installation with `agy plugin list`. Antigravity discovers skills under `skills/`; invoke the namespaced skill directly when needed. The pack includes legacy command wrappers under `commands/`, but the supported invocation path is the native skill catalog.

Keep `references/` beside `skills/` so the shared antislop standard and workflow checklists resolve. For a single-skill copy, each `SKILL.md` includes a concise fallback antislop rule.
