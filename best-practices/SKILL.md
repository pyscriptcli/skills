---
name: best-practices
description: "Search first for authoritative best practices across all engineering disciplines, analyze tradeoffs, and apply them using clean antislop standards. Trigger on /best-practices, 'best practices', 'best practice', 'industry standards', or proactively when architecting, refactoring, selecting libraries, or implementing non-trivial features."
---

# Best Practices: Universal Search, Analyze & Apply

Search authoritative standards first, analyze contextual trade-offs, and apply verified best practices directly into production code while enforcing strict antislop hygiene.

---

## 1. Trigger Conditions

Activate this skill whenever:
- The user invokes `/best-practices`, "best practices", "best practice", or asks for "industry standards".
- Designing system architectures, database schemas, API contracts, or authentication boundaries.
- Selecting third-party libraries, toolchains, or core frameworks.
- Refactoring complex modules, fixing critical performance bottlenecks, or hardening security posture.
- Proactively implementing non-trivial features across any tech stack to prevent stale patterns or obsolete idioms.

---

## 2. Core Execution Lifecycle

Always follow this 3-step discipline:

```
[Phase 1: Search & Discover] ──► [Phase 2: Analyze & Trade-offs] ──► [Phase 3: Apply & Implement]
    (Authoritative sources)            (Context & anti-patterns)           (Antislop-pure code)
```

### Phase 1: Search & Discover (Authoritative First)

Never guess modern APIs or rely solely on pre-training cutoff memory when modern standards, RFCs, or library idioms evolve rapidly.

1. **Targeted Hybrid Search**:
   - **External Search**: Query current official documentation, language specs, and standard bodies using `search_web` or documentation lookups.
     - Web standards: MDN Web Docs, WHATWG, W3C.
     - Backend & Language idioms: Official language docs (e.g., Python PEPs/docs.python.org, Go dev guides, Rust Book/RFCs, Node.js/TypeScript docs).
     - Security: OWASP Top 10, ASVS, NIST, CWE, official framework security advisories.
     - Database: PostgreSQL/MySQL official reference manuals, Redis documentation.
     - Cloud & DevOps: AWS Well-Architected Framework, Google Cloud Architecture Center, Twelve-Factor App, Kubernetes official docs.
   - **Internal Cross-Referencing**:
     - Check local workspace configurations (e.g., `tsconfig.json`, `pyproject.toml`, `package.json`, `.eslintrc`, `.editorconfig`).
     - Inspect existing code patterns and installed dependency versions to prevent breaking conventions or introducing redundant dependencies.

2. **Source Validation Hierarchy**:
   - Priority 1: Official language/framework documentation and specifications.
   - Priority 2: Standard bodies (RFC, W3C, ISO, OWASP, NIST).
   - Priority 3: First-party engineering blogs and maintainer releases.
   - Excluded: Generic SEO blog spam, outdated StackOverflow posts (>3 years old for evolving frameworks), or unverified AI code snippets.

---

### Phase 2: Analyze & Trade-offs

Once candidates are identified, filter them through the project's actual context:

1. **Fit & Friction Matrix**:
   - **Context Fit**: Does this practice solve the actual problem at hand, or does it add accidental complexity?
   - **YAGNI & Simplicity**: Can this be solved natively with the standard library or platform primitive before adding an external package?
   - **Performance vs. Maintainability**: Does the performance gain justify the cognitive overhead?
   - **Backwards Compatibility**: Does it work with the project's target runtime (e.g., Node version, Python version, target browsers)?

2. **Anti-Pattern Elimination**:
   - Deprecated APIs and legacy syntax (e.g., callback hell, mutable global states, raw SQL string concatenation, unvalidated inputs).
   - Premature optimization, over-engineering, enterprise abstraction layers where simple functions suffice.
   - AI slop code habits (unnecessary wrappers, boilerplate classes, redundant try/catch blocks that swallow errors).

---

### Phase 3: Apply & Implement (Antislop Strict)

Apply the best practice directly to the solution. Adhere strictly to the workspace Antislop rules:

1. **Code Comment Hygiene**:
   - **No narrative comments**: Eliminate comments that restate what the code clearly does (e.g., `// Initialize variable`, `// Return response`, `// Step 1: validate`).
   - **No decorative banners or emoji**: No `// ==================`, `/* --- ROUTES --- */`, or `// 🚀 Performance`.
   - **Keep only high-signal rationale**: Document non-obvious business invariants, concurrency assumptions, cryptographic requirements, or specific bug workarounds.

2. **Clean Copy & Natural Prose**:
   - Eliminate AI marketing buzzwords: never use "delve", "game-changer", "tapestry", "seamless", "elevate", "cutting-edge".
   - Be direct, technical, crisp, and objective.

3. **Production Rigor**:
   - Type safety, comprehensive input validation at system boundaries, explicit error handling, and resource cleanup (connections, file handles, streams).

---

## 3. Universal Discipline Standards

### A. Architecture & System Design
- **Single Source of Truth**: Normalize state, centralize domain rules, avoid duplicated caches without invalidation strategies.
- **Fail-Fast Boundaries**: Validate at the edges (API gateway, controllers, CLI input), keep core domain models pure and trusted.
- **Loose Coupling & Explicit Contracts**: Explicit DTOs/schemas over loosely typed dictionaries or `any`.

### B. Backend & API Engineering
- **HTTP Semantics**: Correct status codes (200, 201, 204, 400, 401, 403, 404, 409, 422, 500), idempotent PUT/DELETE, safe GET/HEAD.
- **Concurrency & Resource Management**: Use connection pooling, handle backpressure on streams, cancel contexts/aborts on client disconnection.
- **Structured Observability**: Structured JSON logging (correlation ID, timestamp, log level, event name) without logging PII or secrets.

### C. Frontend & Modern Web
- **Native Platform First**: Modern CSS (`:has()`, subgrid, container queries, dialog/popover API) before JavaScript layout hacks.
- **Core Web Vitals & Performance**: Optimize Largest Contentful Paint (LCP) with `fetchpriority="high"`, minimize Cumulative Layout Shift (CLS) with aspect-ratio reservations, minimize blocking JS.
- **Accessibility (a11y)**: Semantic HTML (`<main>`, `<nav>`, `<button>`, `<dialog>`), keyboard navigation, focus trap in modals, sufficient contrast ratios (WCAG AA).

### D. Database & Persistence
- **Integrity**: Foreign key constraints, unique constraints, and atomic transactions for state mutations.
- **Query Efficiency**: Index foreign keys and filtered columns, avoid N+1 query patterns, select only required columns (avoid unbounded `SELECT *`).
- **Migrations**: Backward-compatible, non-blocking schema migrations (expand and contract pattern).

### E. Security & Auth (Zero Trust)
- **Injection Defense**: Parameterized queries / prepared statements only. Never format raw user input into SQL, shell commands, or HTML templates.
- **Defense in Depth**: Principle of least privilege, strict CORS, Content Security Policy (CSP), HTTP-only Secure SameSite cookies, CSRF protection.
- **Secret Hygiene**: Zero hardcoded keys or tokens. Load secrets exclusively from environment variables or secure vault stores.

### F. Testing & QA
- **Seam-based Testing**: Unit tests for complex domain logic, integration tests for database/API contracts, end-to-end tests for critical user journeys.
- **Deterministic & Isolated**: No flaky sleeps, mock external third-party network calls, wipe/sandbox test databases per run.
- **Meaningful Assertions**: Test behavior and invariant states, not internal implementation details or private methods.

---

## 4. Standard Response Template

When executing a task under this skill, present your findings and solution using this crisp format:

```markdown
### 1. Discovered Best Practices
- **[Practice / Standard Name]** (Source: [Official Spec/Doc URL or Reference]):
  Summary of standard pattern and why it is authoritative.

### 2. Contextual Analysis & Trade-offs
- **Context Fit**: Why this fits the target stack, dependencies, and constraints.
- **Trade-offs**: Latency, complexity, backward compatibility, or operational considerations.
- **Eliminated Anti-Patterns**: Outdated or fragile patterns avoided.

### 3. Applied Implementation
[Clean, production-grade code incorporating the practice, with antislop comment hygiene]
```
