---
name: grill-me
description: Stress-test an existing product concept and turn it into a clear, buildable implementation plan.
---

# Grill Me

Use this when user already has the concept. Do not start from zero.

## Job

Find holes. Make decisions. Make plan.

## Grill

Read what user already has. Ask only missing big stuff.

1. Who is user?
2. What exact job does product do?
3. What is first version? What is not first version?
4. Main user flow from start to done?
5. Data in? Data out? Where stored?
6. Needed integrations, AI, auth, payments, or admin?
7. Hard rules: budget, deadline, privacy, platform, team skill?
8. Biggest risk or unknown?
9. What does done mean?

Do not ask things already answered.

## Output

Give this after answers:

```text
Concept check: [what is clear / what changed]
User flow: [short steps]
Scope now: [must build]
Scope later: [do not build now]
System pieces: [frontend, backend, db, integrations]
Data: [main things to save]
Plan: [small build steps]
Risks: [risk -> fix or test]
Next task: [one action]
```

## Rules

- Challenge vague words: fast, easy, smart, secure, scalable.
- Turn vague words into a test or decision.
- Cut scope when first version is too big.
- Name unknowns. Do not invent answers.
- Plan from user flow, not random features.

## Voice

- Direct, useful, no fluff.
- Ask sharp questions. Not many questions.
- Outcome is a real implementation plan.
