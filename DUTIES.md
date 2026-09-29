# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitKbCurator** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitKbCurator Automation Engine`
* **Responsibilities**:
  * Analyzes resolved support conversations, strips PII, and formats standard Markdown documentation.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitKbCurator Verification & Policy Enforcer`
* **Responsibilities**:
  * Calculates vector similarity against published articles to maintain single source of truth.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Knowledge Base Editor / Principal Support Engineer (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
