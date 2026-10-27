---
name: sf-release
description: Prepare a Salesforce change for a controlled release by reviewing metadata, dependencies, tests, validation, deployment sequence, and rollback readiness. Use for release planning and deployment preparation.
---

# Salesforce Release Readiness

Prepare Salesforce changes for a repeatable, reviewable release. This skill plans and validates a release; it does not imply authorization to deploy or make production changes.

## Establish the release boundary

- Identify the requested change, target org/environment, deployment method, release window or constraints, and approval requirements.
- Inspect repository instructions, Git status, Salesforce project configuration, changed files, existing CI/CD pipeline, tests, and release conventions. Preserve unrelated working changes.
- Confirm the target environment using available org information; do not infer from an alias alone.
- Read the original goal and acceptance criteria from the implementation record when available. Keep release scope tied to those criteria.

## Build the release plan

Review:

- Changed metadata and source diff for unintended or environment-specific values.
- Dependencies, including objects/fields, permissions, custom metadata/settings, Apex/Flow references, packages, integrations, and activation/order requirements.
- Test coverage and results relevant to the changed behavior; identify tests that must run in the target environment.
- Deployment validation options, source tracking or manifest approach, and known metadata limitations for the project's API version and deployment path.
- Data migration or post-deploy configuration steps, if any, with explicit owner and expected result.
- Backout approach: metadata rollback, deactivation, forward fix, or data recovery as appropriate. Never claim a simple rollback where stateful data or irreversible side effects exist.

Produce a release checklist with step, owner, command/navigation, expected result, and stop condition. Separate required gates from optional recommendations. Include post-deployment checks and how to confirm the original acceptance criteria.

## Validate and deploy boundaries

- Prefer static review, local tests, CI checks, and Salesforce deployment validation before an actual deployment.
- Use only the project's established Salesforce CLI and CI/CD commands. Do not print credentials, access tokens, or secret values.
- Sandbox-first is the default. Preparing or validating a release does not itself authorize org mutation. Deploy only when the user explicitly authorizes the specific target and action.
- Before deployment, confirm the target, change set/manifest, and relevant tests. Stop if the target appears to be production but production deployment was not explicitly authorized.
- Report exactly what was validated or deployed, the verified target, test results, failures, and remaining steps. Never imply a validation-only deployment changed org metadata.

## Output

Provide a readiness assessment (Ready, Ready with conditions, or Not ready), evidence, ordered deployment/post-deployment steps, rollback limits, and unresolved blockers. Link release artifacts and cite current Salesforce documentation when deployment behavior is release-sensitive.
