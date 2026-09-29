# Explainability, Auditability & Decision Logic: GitKbCurator

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitKbCurator**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitKbCurator** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Resolved**: Resolved support ticket conversation threads (Zendesk, Jira Service Desk, Freshdesk).
- **Existing**: Existing corporate knowledge base documentation articles and Markdown repositories.
- **Technical**: Technical glossary and component architectural naming conventions.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **summarize_ticket_resolution**: Uses `resolution-summarizer` to calculate extracts problem symptom and verified root-cause resolution from ticket thread.
   - **format_runbook_markdown**: Uses `runbook-markdown-formatter` to calculate formats troubleshooting guide into standard markdown with code blocks.
   - **detect_duplicate_articles**: Uses `duplicate-article-detector` to calculate calculates semantic cosine similarity against published knowledge base articles.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When a resolved ticket is nominated for KB curation, the agent runs resolution_summarizer, runbook_markdown_formatter, and duplicate_article_detector. If the solution is novel and verified, it issues APPROVED. If overlapping partial articles exist, it issues NEEDS_REVIEW. If the resolution is unverified or contains unmasked customer data, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on technical documentation standards.
- **Does**: Does not publish draft articles directly to public customer-facing portals without editorial review.
- **Requires**: Requires at least one verified customer confirmation of issue resolution.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
