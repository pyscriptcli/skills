# Using Agent Skills with Codex

The plugin manifest and the `skills/` directory live inside this folder.

From the parent `pyscriptcli/skills` checkout, install the local plugin:

```bash
codex plugin marketplace add ./agent-skills-antislop
codex plugin add agent-skills-antislop@agent-skills-antislop
```

Start a new Codex session after installation. Invoke a skill with `@skill-name` or describe the task and let Codex select it. The pack includes 25 skills.

Codex loads skill descriptions first and full instructions on demand. Keep `using-agent-skills/SKILL.md` as an on-demand skill; do not paste its full content into always-on project instructions. The shared antislop reference stays available at `references/antislop.md` when the package is installed as a whole.
