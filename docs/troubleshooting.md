# Aegis Troubleshooting

## Wrong Agent Routing

### Symptom

Question is sent to the wrong specialist.

### Investigation

Check supervisor instructions and agent descriptions.

### Fix

Improve routing instructions and evaluation cases.

---

## Wrong RAG Answer

### Symptom

Retrieved documents are irrelevant.

### Investigation

Check chunking, embeddings, metadata and retrieval.

### Fix

Improve chunking/retrieval and add evaluation cases.

---

## Unauthorized Document

### Symptom

Restricted document appears in response.

### Investigation

Check ACL filtering before retrieval/context construction.

### Fix

Enforce identity-aware filtering before Gemini receives context.

---

## Dangerous SQL

### Symptom

Agent generates non-SELECT SQL.

### Fix

Reject all non-SELECT statements and enforce allow-lists.

---

## Agent Loop

### Symptom

Agent repeatedly calls tools.

### Fix

Add iteration limits, timeout and fallback.
