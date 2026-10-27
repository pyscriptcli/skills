---
name: sf-guide
description: Create a detailed, accurate step-by-step guide for replicating an implemented Salesforce automation or feature in a target org. Use when the user asks how to reproduce a completed Salesforce implementation.
---

# Salesforce Implementation Guide

Create a practical runbook that lets the intended Salesforce administrator or developer reproduce the implementation that was actually built and sandbox-verified.

## Ground the guide in evidence

- Inspect the implementation, metadata, tests, and sandbox verification notes. Use sf-tdd context or its deliverables when available.
- Verify current Salesforce Setup labels, prerequisites, permissions, limits, and release-sensitive behavior using first-party Salesforce Help, Developer documentation, or Trailhead. Link the exact sources.
- Distinguish verified facts from org-specific values the reader must supply. Never invent org IDs, record IDs, credentials, secrets, endpoints, profiles, permission assignments, or data.
- If screenshots are available and authorized, use them to clarify the relevant UI steps. Caption and reference them. Do not fabricate UI evidence.

## Write an executable sequence

Order the guide so readers can follow it without guessing:

1. State the purpose, outcome, intended audience, and what is in scope.
2. List prerequisites: edition/features, licenses, permissions, dependencies, source package or metadata, and sandbox access.
3. Give the exact ordered steps. For Setup tasks, include navigation path, setting/field names, values, and choices. For metadata deployment, identify the project artifacts and the repository's actual deploy/validate command pattern.
4. Explain required assignments, activation, execution order, entry criteria, and interactions with existing automation.
5. Provide validation steps, test commands or Setup actions, expected results, and a small acceptance checklist.
6. Include likely failure symptoms and evidence-based troubleshooting, plus a rollback or deactivation procedure where applicable.
7. Call out production-specific review separately. Sandbox-first is the default; this guide does not authorize a production deployment.

Keep steps specific to this implementation. Mark decisions that depend on org configuration and explain how the administrator should resolve each one. Avoid a generic Salesforce tutorial.

## Completion check

Check that every implementation dependency has a setup step, every step has a clear expected result where useful, values are traceable to source artifacts, and the guide does not claim a deployment or test that did not occur. Deliver in the format and location requested.
