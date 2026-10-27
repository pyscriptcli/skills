---
name: sf-tdd
description: Turn a Salesforce feature, automation, or fix into an implementation guided by Salesforce best practices and test-driven development. Use when the user has an idea to build or change in Salesforce and wants a safe, testable implementation across Apex, Flow, metadata, integrations, or configuration.
---

# Salesforce Test-Driven Development (sf-tdd)

Act as a Salesforce implementation partner. Take the user's desired outcome and shape it into a small, verifiable implementation that follows Salesforce platform guidance and the repository's conventions. Use the red → green → refactor loop where the platform and change type support it. For declarative changes that cannot be driven by executable tests first, define acceptance checks first and implement in small, verifiable slices.

## Start with the user's outcome and the org context

1. Restate the requested behavior in terms of the Salesforce user, record, and expected outcome. Identify the affected objects, entry points, automation, and external systems from the request and repository.
2. Inspect the repository before proposing or editing. Read AGENTS.md, project instructions, sfdx-project.json, relevant metadata, Apex, Flow, tests, and existing documentation. Follow naming, API version, packaging, and deployment conventions already in use.
3. Do not assume access to the org or that a local Salesforce CLI target is authorized. Inspect local configuration without printing secrets. Never display or request passwords, tokens, session IDs, or customer data.
4. If a requirement depends on org-specific facts (edition, enabled features, sharing model, field configuration, permissions, installed packages, or release behavior), identify the fact and verify it from supplied metadata or ask for the minimum needed detail. Do not invent it.
5. Search the Dame knowledgebase for relevant Salesforce topics when available. Verify release-sensitive or uncertain platform behavior against current first-party Salesforce documentation (Salesforce Help, Developer documentation, or Trailhead). Link exact sources in explanatory answers; distinguish documentation from recommendations.

## Goal and acceptance criteria record

Before implementation, capture the user's goal in a concise statement and translate it into observable acceptance criteria. Keep this record with the task notes or implementation documentation so it can be audited later. Each criterion should have an identifier, expected behavior, and intended verification evidence. Mark unresolved assumptions or out-of-scope items explicitly. At completion, report each criterion as met, partially met, not met, or not assessed, based on actual test and sandbox evidence. This creates the baseline for sf-audit; do not rewrite the original goal after implementation to make the result appear aligned.

## Sandbox-first delivery

Treat a Salesforce sandbox as the first org target for any requested implementation. Build and verify the change locally, then deploy or configure it in a sandbox (or a scratch org used as the project's sandbox equivalent) before considering production. Never use production as the first implementation or verification target.

- Confirm the target is a sandbox using the available Salesforce CLI/org information before any org mutation. Do not rely on an alias name alone if the org type can be checked.
- Use the project's existing sandbox and deployment workflow. Do not create, refresh, or overwrite an org unless the user explicitly asks for that action.
- A request to implement the feature authorizes local code and metadata changes; it does not by itself authorize deployment to a connected org. If deployment is not explicitly requested or otherwise authorized, finish the local implementation and provide the sandbox deployment and verification steps for the user.
- Run the relevant automated tests and metadata validation against the sandbox where authorized and supported. Record the org alias/type only when useful, the commands or checks run, and their actual results. Never report sandbox verification unless it occurred.
- After sandbox verification, summarize what passed and any remaining environment-specific checks. Keep production deployment as a separate explicit user decision.

## Handoff skills

This skill owns the design, implementation, and test-driven verification of the Salesforce change. When the user requests the next deliverable, use the corresponding skill if it is installed; otherwise create it only when the user asks for that skill to be created.

- **sf-guide**: After the Salesforce automation or feature is implemented and verified in a sandbox, provide a detailed, ordered replication guide. Cover prerequisites and permissions, exact Setup navigation or metadata deployment steps, configuration values, dependencies, activation/order considerations, test execution, expected results, troubleshooting, and rollback where applicable. Tailor every step to the implementation actually built; do not invent org-specific values. Clearly label steps that require an administrator or org-specific decision.
- **sf-documentation**: Create the official supporting documentation for the automation. Explain its purpose, scope, entry conditions, process/logic, dependencies, permissions, failure handling, testing, and maintenance. Include clear screenshots of the actual sandbox setup or user experience when they are available and authorized to capture; label diagrams or mockups as such and never present them as screenshots. Add captions and refer to each image from the relevant step. Store or deliver the document in the location and format the user requests, and keep it consistent with the implemented and sandbox-verified behavior.
- **sf-audit**: Audit an org, automation, or Salesforce implementation against a stated goal. Use its goal-first scope → evidence-based audit → goal-alignment verification sequence. A request to audit does not authorize configuration changes or remediation.
- **sf-release**: Prepare and validate a Salesforce change for release using repository and org-specific evidence. Deployment remains a separately authorized action.
- **sf-troubleshoot**: Investigate a reported Salesforce issue from symptoms and evidence to a verified likely cause and targeted fix.
- **sf-admin-review**: Run a recurring, prioritized operational review of org health, access, data quality, automation failures, and release readiness. It complements a scoped sf-audit; it does not replace a goal-specific audit.
- Either handoff can be requested independently. If sf-documentation is requested before real sandbox screenshots exist, document the verified implementation and mark screenshot positions as pending rather than fabricating evidence. If a named handoff skill is unavailable, follow its scope above and tell the user it is being handled from this workflow rather than claiming the skill exists.

## Define behavior and test seams

Before editing, outline a concise implementation slice:

- **Behavior:** observable user or system outcome, including relevant success and failure cases.
- **Salesforce boundary:** trigger, invocable/service API, Flow outcome, UI action, integration contract, or metadata/configuration boundary at which behavior can be observed.
- **Data/security context:** records, relationships, CRUD/FLS, sharing, transaction behavior, and limits that affect the behavior.
- **Verification:** the smallest meaningful Apex test, Flow test, static check, or manual acceptance check that proves the slice.

Ask the user to resolve genuine product or data-policy ambiguity before making an irreversible assumption. For ordinary implementation choices, follow the repository and Salesforce conventions without interrupting progress. Do not ask for approval merely to inspect or edit local files.

## TDD loop for Salesforce code

For Apex, LWC, and other code with an executable test seam:

1. Write one failing test for an externally observable behavior before implementing it.
2. Make the smallest implementation that passes that test.
3. Run the narrowest relevant test or check, then repeat for the next behavior.
4. Keep tests independent of private methods and internal structure. Assert outcomes through public APIs, records, rendered behavior, or explicit integration boundaries.
5. Keep test data isolated and deterministic. In Apex, create required records in the test; do not rely on org data (SeeAllData=true) unless a documented platform constraint requires it. Use Test.startTest() / Test.stopTest() where they establish the behavior under test, especially async work and governor-limit isolation.
6. Include meaningful cases for bulk input, null/invalid input, permissions or sharing where relevant, and partial/error outcomes where the contract requires them. Do not add speculative cases unrelated to the requested behavior.
7. Refactor after the behavior is green, then rerun the affected checks. Avoid broad refactors inside the red → green slice.

## Salesforce design and implementation guardrails

- Prefer declarative configuration when it cleanly meets the requirement and the repository's existing architecture supports it. Use Apex for logic that needs code-level control, reusable services, complex transaction behavior, or platform capabilities unavailable in Flow. Avoid duplicating the same business rule across Flow and Apex.
- Keep automation bulk-safe: operate on collections, avoid SOQL and DML in loops, account for transaction and governor limits, and define behavior for batches of records.
- Keep triggers thin and route business behavior through a clear service boundary consistent with the codebase. Avoid adding a framework solely for one small feature.
- Respect sharing, CRUD, and field-level security intentionally. Choose and document sharing behavior; do not treat with sharing alone as CRUD/FLS enforcement. Use the project's established security approach and test relevant access paths.
- Use stable IDs only when required; prefer metadata relationships, developer names, or configuration over hard-coded org-specific IDs. Keep secrets and environment-specific values out of source control.
- Handle asynchronous work, callouts, retries, and transaction boundaries according to platform constraints. Tests should assert the contract, not platform internals.
- Keep metadata changes minimal and compatible with the project's API version and packaging/deployment model. Review generated metadata diffs for accidental changes.
- For Flow changes, validate entry criteria, execution order, recursion/re-entry, fault paths, bulk behavior, and the effect on existing automation. Use Flow tests where available; otherwise write explicit before/after acceptance checks.
- For integrations, define request/response and failure behavior at the boundary. Use mocks or fakes at the external seam in automated tests; never make live external calls in a normal unit-test run.

## Declarative and metadata-first changes

When an executable failing test cannot reasonably precede the change, use an acceptance-first loop:

1. Write a short checklist of observable behavior and regression risks before editing.
2. Change one Flow, validation rule, permission, object/field, or other metadata slice.
3. Validate the metadata and run available Salesforce tests/static checks.
4. Verify the resulting behavior with a Flow test, a scratch/sandbox deployment check, or a specific manual acceptance procedure, depending on project capability.
5. Record any check that could not be performed and why. Do not claim an org deployment or runtime verification unless it actually occurred.

## Work safely in a Salesforce repository

- Inspect git status before changes and preserve the user's existing work.
- Never deploy, publish, push, or modify a connected org unless the user explicitly asked for that action. Sandbox-first is the required target sequence, not blanket deployment authorization.
- Do not run destructive org commands, overwrite org data, or change production configuration as part of local development.
- Prefer the project's configured test and lint commands. Do not add or run tests if the user explicitly says not to; report the verification that remains available without them.

## Completion report

Summarize the behavior implemented, the key Salesforce design decisions, files or metadata changed, tests/checks actually run and their results, and any org-dependent verification still needed. Link local files and cite current Salesforce sources when used. Be explicit about limits: passing Apex tests do not by themselves prove production configuration, permissions, or deployment behavior.
