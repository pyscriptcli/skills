# skills

Small reusable agent skills.

## Layout

Standalone skill: root folder.
Related skills: one group folder.

```text
benchmark-comparison/
├── SKILL.md
caveman/
├── SKILL.md
grill-me/
├── SKILL.md
└── no-idea/
    └── SKILL.md
prime-pitch-agy/
├── SKILL.md
├── scripts/
└── templates/
repository-structure/
└── SKILL.md
prime-design/
├── SKILL.md
└── references/
    └── project-echo-ui.md
prime-pitch-codex/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── anti-slop.md
    ├── grill-me.md
    ├── prime-brand.md
    └── voice-and-jargon.md
deck_generator_skill/
├── SKILL.md
├── branding.json
├── templates/
├── scripts/
└── examples/
matt-pocock/
├── LICENSE
└── skills/
    ├── engineering/
    ├── productivity/
    ├── misc/
    └── in-progress/
```

## Skills

- `benchmark-comparison` - compare tools, vendors, or products.
- `caveman` - make work short, plain, and direct.
- `grill-me` - stress-test an existing concept and make a build plan.
- `grill-me/no-idea` - turn a vague thought into concept and plan.
- `prime-pitch-agy` - all-in-one executive pitch deck studio (grill-me + anti-slop + PRIME brand + 16:9 HTML & 1-to-1 PDF pipeline).
- `repository-structure` - make clean frontend/backend project structure.
- `prime-design` - apply the PRIME Philippines Project Echo UI system.
- `prime-pitch-codex` - grill, shape, and build persuasive PRIME-branded pitch decks with clear voice, terminology, and evidence standards.
- `deck_generator_skill` - create branded, editable PRIME Philippines commercial & warehouse proposal decks from unstructured notes, screenshots, or existing presentations.
- `matt-pocock/skills` - attributed mirror of Matt Pocock's MIT-licensed agent skill collection.

## Third-party skills

The `matt-pocock` directory mirrors the skill source from
[`mattpocock/skills`](https://github.com/mattpocock/skills). Its original MIT
license and copyright notice are preserved in `matt-pocock/LICENSE`.
