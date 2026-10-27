---
name: sf-audit
description: Define and execute a Salesforce audit against a stated goal, then verify every goal item against evidence and report gaps. Use when the user asks for an audit, assessment, or conformance review of a Salesforce org, automation, security posture, or implementation.
---

# Salesforce Goal-Aligned Audit

An audit has three required stages: define what to audit from the user's goal, perform the agreed audit using evidence, then verify that the audit covered and answered the original goal. Keep these stages distinct so the scope cannot silently drift.

## 1. Establish the goal and audit plan

1. Capture the user's goal in a short, testable statement. Preserve the original wording or a traceable restatement.
2. Turn the goal into audit questions and observable criteria. Identify what evidence would support each criterion and what would count as a gap.
3. Inventory candidate audit areas, then select only those relevant to the goal. Salesforce areas can include:
   - Security posture and org settings (for example, Security Health Check against an appropriate Salesforce or approved custom baseline).
   - Identity, user access, permissions, and object/field/record sharing.
   - Setup/configuration changes and audit history.
   - Data quality, retention, and governance.
   - Flows, Apex, LWC, validation rules, and automation interactions.
   - Code quality, secure coding, bulk behavior, and platform limits.
   - Integrations, secrets handling, monitoring, and error recovery.
   - Release, deployment, test, and documentation practices.
4. Define in-scope components, environments, dates, populations, exclusions, access needed, and any constraints. State whether the audit is read-only. Obtain missing scope details only when they materially affect what can be concluded.
5. Produce an audit plan before execution: criterion, evidence source, method, owner/access, and planned status. For broad goals, present a candidate inventory and a recommended bounded scope so the user can steer it.

Do not treat every candidate category as automatically in scope. Do not expand the audit after seeing findings without recording the scope change and its reason.

## 2. Perform the agreed audit literally

- Inspect only the approved scope and use the least access needed. Prefer source metadata, test results, configuration exports, Salesforce setup reports, and documented evidence.
- Use relevant Salesforce tools where available: Security Health Check / Security Center for posture signals, Setup Audit Trail for recent configuration changes, login or event monitoring evidence where authorized, and Salesforce Code Analyzer for supported source artifacts (including Apex, Flow, and Lightning components).
- Use current first-party documentation for platform criteria. Confirm edition, feature availability, API version, and org configuration when they affect a finding.
- Record evidence for each criterion: source/artifact, location or query/report, observation, date/context, and limitations. Separate observed fact from inference and recommendation.
- Classify findings by severity and explain impact, likelihood/context, and evidence. Use Critical/High/Medium/Low/Informational only when the evidence supports the rating; otherwise label severity as unassessed and explain why.
- Identify evidence gaps, inaccessible areas, sampling, false-positive possibilities, and items that could not be tested. Mark them as unknown or not assessed, never as pass.
- An audit is assessment, not remediation. Do not change Salesforce configuration, assign permissions, deploy metadata, alter data, or suppress scanner findings unless separately requested and authorized.

## 3. Verify alignment to the original goal

At the end, revisit the original goal and create a traceability table with one row per original criterion:

| Goal criterion | Evidence reviewed | Result | Finding/reference | Limitation |
| --- | --- | --- | --- | --- |

Use clear result labels: **Met**, **Partially met**, **Not met**, **Not assessed**, or **Not applicable** (with rationale). Confirm that:

- Every item in the original goal maps to an audit criterion and a result.
- Every in-scope criterion has evidence or is explicitly marked not assessed.
- Conclusions follow from the recorded evidence, and recommendations do not masquerade as observed facts.
- Any out-of-scope work or scope change is disclosed.
- The summary answers the original goal directly and states confidence and limitations.

If a goal item was omitted or the evidence cannot answer it, identify that gap and extend the audit only when authorized and feasible. Do not silently declare the goal achieved.

## Deliverable

Report the goal, scope, method, date/context, evidence sources, prioritized findings, goal-to-evidence traceability, recommendations, and limitations. Keep recommendations actionable and linked to findings. Cite current Salesforce first-party sources when used. Never claim certification, compliance, complete coverage, or a clean org based only on partial checks.

## Salesforce references

- [Security Health Check](https://help.salesforce.com/s/articleView?id=sf.security_health_check.htm&language=en_US)
- [Salesforce data security overview and audit system use](https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_overview)
- [Salesforce Code Analyzer](https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/code-analyzer.html)
- [Monitor Setup Changes with Setup Audit Trail](https://help.salesforce.com/s/articleView?id=admin_monitorsetup.htm&language=en_US&type=5)
- [Protect Your Application from CRUD/FLS Vulnerabilities](https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-crud-fls-vulnerabilities.html)
- [Protect Your Application from Sharing Violations](https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-sharing-violations.html)
