# Aegis Threat Model

## T1 — Prompt Injection

A malicious document may contain instructions intended to manipulate the agent.

Mitigation:
- Treat retrieved content as untrusted data.
- Keep system instructions separate.
- Evaluate retrieval content.
- Add adversarial tests.

## T2 — Unauthorized Data Access

A user may request a document outside their permissions.

Mitigation:
- Identity-aware retrieval.
- ACL filtering before model context.
- Least privilege.

## T3 — Tool Abuse

An agent may call a sensitive tool.

Mitigation:
- Narrow tool schemas.
- Authorization.
- Human approval.
- Audit logging.

## T4 — SQL Injection

The model may generate dangerous SQL.

Mitigation:
- SELECT-only.
- Table allow-list.
- Query validation.
- Read-only identity.
- Maximum bytes billed.

## T5 — Secret Leakage

Secrets may accidentally reach prompts or responses.

Mitigation:
- Secret Manager.
- Redaction.
- No secrets in source control.
- Logging restrictions.

## T6 — Agent Loop

An agent may repeatedly call tools.

Mitigation:
- Maximum iterations.
- Timeouts.
- Tool limits.
- Fallback behavior.

## T7 — Excessive Cost

A request may cause excessive model/tool usage.

Mitigation:
- Budget.
- Quotas.
- Token limits.
- Maximum tool calls.
- Monitoring.
