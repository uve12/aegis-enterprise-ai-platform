# Aegis Architecture

## User

Employees interact through the enterprise AI interface.

## Supervisor

Routes requests to specialized agents.

## Knowledge Agent

Uses enterprise RAG and Workspace search.

## Data Agent

Queries approved BigQuery datasets.

## Incident Agent

Investigates incidents and operational evidence.

## Multimodal Agent

Processes image, audio and video input.

## MCP

Provides controlled enterprise tools.

## Gemini

Provides reasoning and generation.

## Agent Runtime

Runs deployed agents.

## Security

IAM, authorization, Secret Manager and approval controls.

## Observability

Logs, metrics, traces and evaluation.

## Data flow

User
→ Supervisor
→ Specialist Agent
→ Tool/RAG
→ Gemini
→ Response
