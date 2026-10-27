---
name: sf-documentation
description: Create or update official supporting documentation for a Salesforce automation or feature, grounded in the implementation and including real screenshots when available and authorized.
---

# Salesforce Automation Documentation

Produce maintainable official documentation that accurately describes a Salesforce automation or feature as implemented. Treat it as a supporting artifact for the automation, not a substitute for the deployed metadata or tested behavior.

## Gather accurate source material

- Inspect the implementation, Flow/Apex/metadata, tests, related configuration, and sandbox verification results. Prefer the implementation itself over assumptions or old notes.
- Use sf-tdd and sf-guide outputs when available, and resolve discrepancies against the actual metadata and tested behavior.
- Verify release-sensitive Salesforce behavior with first-party Salesforce Help, Developer documentation, or Trailhead. Cite exact sources for platform guidance.
- Never imply org access or successful verification without evidence. Mark unknowns and org-specific choices clearly.

## Document the system

Include the sections appropriate to the feature, typically:

- Purpose, business outcome, audience, scope, and owner.
- Entry conditions, trigger/source, input records, eligibility, and exclusions.
- Process flow and important decisions, including a diagram only when it helps explain branching or dependencies.
- Components and dependencies: objects/fields, Flow/Apex, permission sets, integrations, scheduled or async work, and related automation.
- Security and access behavior, including who can run it and any intended sharing/CRUD/FLS assumptions.
- Errors, fault paths, retries, notifications, and operational monitoring.
- Setup or replication reference, tests, expected outcomes, maintenance owner, and change history when requested or useful.

Use names that match Salesforce Setup and source metadata. Describe observed behavior; separate recommendations from current behavior.

## Screenshots and evidence

- Include clear screenshots of the actual sandbox Setup or user experience when they are available and authorized to capture. Capture only the information needed to explain the step, avoid exposing personal or sensitive data, and caption each image with context.
- Never invent screenshots, imply a mockup is a real org, or edit an image in a way that changes the underlying evidence. Label diagrams, annotated mockups, and placeholders accurately.
- If screenshots are unavailable, create the documentation from verified artifacts and mark the specific screenshot evidence as pending if it is required.

## Deliver and verify

Create the document in the format and location requested. Check that every described behavior maps to implementation evidence, images render and have captions, sources resolve, and unresolved assumptions are visible. Report the artifact location and any verification or screenshot gaps.
