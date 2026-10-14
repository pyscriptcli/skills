# Agent Skills with Antislop

A Codex and Antigravity focused package of 25 engineering workflow skills derived from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills). It keeps the upstream workflows and license, removes integrations for unrelated hosts, and applies one shared antislop quality standard across every skill.

## Install

Codex plugin:

```sh
codex plugin marketplace add ./agent-skills-antislop
codex plugin add agent-skills-antislop@agent-skills-antislop
```

Antigravity plugin:

```sh
agy plugin install ./agent-skills-antislop
```

For project-local/manual use, install or copy the `skills/` directory according to the host's skill discovery rules. Keep `references/` beside `skills/` so all skill links resolve. Each skill also carries a short fallback standard for single-skill installs.

## What is included

- `skills/` - 25 lifecycle skills, each with a mandatory antislop check.
- `references/` - shared engineering checklists and the pack-wide antislop standard.
- `.codex-plugin/` and `.agents/plugins/` - Codex plugin metadata.
- `plugin.json` and `commands/` - Antigravity plugin metadata and command wrappers.
- `docs/` - setup notes for Codex and Antigravity.

## Antislop behavior

Every skill points to `references/antislop.md`. Apply only checks relevant to the task. The standard favors specific, evidence-backed work, clear language, working interfaces, and simple implementations. It does not require visual-design checks for non-UI tasks.

## Attribution

This package is derived from Addy Osmani's MIT-licensed [agent-skills](https://github.com/addyosmani/agent-skills). See [UPSTREAM.md](UPSTREAM.md) and [LICENSE](LICENSE) for attribution and terms.

