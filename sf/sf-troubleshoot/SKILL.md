---
name: sf-troubleshoot
description: Diagnose Salesforce errors or unexpected behavior by tracing symptoms through metadata, automation, access, logs, and recent changes, then verify a focused fix.
---

# Salesforce Troubleshooting

Find the cause of a specific Salesforce failure or unexpected result using evidence. Avoid changing unrelated configuration or guessing from symptoms alone.

## Frame the issue

- Capture expected behavior, actual behavior, exact error text, affected users/records, frequency, first-known occurrence, and recent relevant changes.
- Protect sensitive information: redact tokens, session IDs, personal data, and customer values from logs or screenshots.
- Inspect repository instructions, Salesforce project metadata, relevant Flow/Apex/LWC, tests, and version history. Do not assume access to a connected org.
- If org evidence is needed, identify the minimum relevant logs, debug trace, Flow error, login/access details, or reproduction data and request only that evidence.

## Trace and test hypotheses

Follow the runtime path relevant to the symptom: entry point and criteria → automation order and conditions → data/permissions/sharing → limits or async/callout behavior → error handling → UI or integration result. Consider recent deployments and configuration changes where evidence supports a connection.

For each plausible cause, record supporting and contradicting evidence. Reproduce safely in a sandbox or local test context when possible. Use Salesforce CLI and diagnostic tools only when configured and authorized. Verify current, release-sensitive platform behavior in first-party Salesforce documentation.

For code changes, use sf-tdd: add a failing behavior test, make a minimal fix, and rerun relevant tests. For Flow or configuration changes, define before/after acceptance checks and validate in a sandbox. Do not use production as a test environment or alter data/configuration without authorization.

## Verify the fix

- Confirm the original failure can no longer be reproduced under the documented conditions.
- Check relevant success and failure paths and regressions at the affected boundary.
- Keep the fix limited to the supported root cause; if evidence is inconclusive, report ranked hypotheses and the next diagnostic evidence needed instead of presenting a guess as fact.
- Record whether org runtime behavior, tests, metadata validation, or only source inspection was verified.

## Report

Summarize the symptom, root cause or remaining hypotheses, evidence, fix, verification performed, affected files/configuration, and org-dependent follow-up. Distinguish facts from inference and state diagnostic limitations clearly.
