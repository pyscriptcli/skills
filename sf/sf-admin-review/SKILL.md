---
name: sf-admin-review
description: Perform a recurring operational review of Salesforce org health, access, data quality, automation reliability, and release readiness, then prioritize actions.
---

# Salesforce Admin Operations Review

Run a repeatable, bounded review that helps an administrator keep an org healthy. This is a periodic operational checklist; use sf-audit when the user has a specific goal or conformance question that needs a scoped, evidence-traceable audit.

## Set the review cadence and boundaries

- Confirm the orgs and review period, available access, business-critical processes, and relevant licenses/features. Use the least access needed.
- Review read-only by default. Do not change settings, grant/revoke access, deploy, edit data, or enable products as part of a review unless separately authorized.
- Compare with the last review when available. Track each item as new, recurring, improved, resolved, not applicable, or not assessed.

## Review operational areas

Select what applies to the org and available evidence:

- **Org health and capacity:** Salesforce Org Health and Usage metrics, security score, storage, licenses, performance signals, and pending release updates.
- **Security and access:** Security Health Check against an appropriate baseline; privileged users; inactive or stale users; permission sets and groups; sensitive object/field/record access; login anomalies and guest access where applicable.
- **Automation reliability:** Flow and Apex failures, unhandled fault paths, recurring support issues, scheduled/asynchronous jobs, integrations, and overlapping automations affecting business-critical processes.
- **Data quality and governance:** duplicate or incomplete critical records, ownership/retention expectations, data growth, and availability of backup/recovery evidence where relevant.
- **Change and release hygiene:** recent Setup Audit Trail changes, metadata in source control, test/deployment evidence, open release risks, and documentation freshness.

Use built-in Salesforce health/security pages and reports when available, repository metadata for source-controlled components, and current first-party Salesforce documentation for criteria. Respect edition, permission, retention, and feature limits. Do not present missing evidence as a healthy result.

## Prioritize and follow up

For each finding, capture evidence, business impact, urgency, owner, recommended next action, and due date or review cadence where known. Prioritize active security exposure, broken business-critical processes, and capacity risks ahead of housekeeping. Label inferences and unknowns. Link an operational finding to sf-troubleshoot when root-cause diagnosis is needed, sf-audit for goal-specific investigation, or sf-release for a change that needs deployment planning.

Do not label the org compliant or fully secure based on a periodic checklist. Report covered areas, inaccessible or skipped checks, and source of each status.

## Output

Provide a dated review summary, scope, evidence checked, prioritized actions, owners if known, status against the previous review, and limitations. Cite current Salesforce first-party sources for product-specific checks. Keep the format stable enough for comparison in the next review.
