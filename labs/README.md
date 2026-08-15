# Enterprise Architecture Labs

Labs are not toy CRUD demos. Each lab should demonstrate one architecture property deeply and include evidence.

## Quality bar

A strong lab should include, where relevant:

- clear problem statement
- architecture diagram
- runnable implementation
- automated tests
- explicit failure scenario
- idempotency / recovery behavior
- security assumptions
- observability
- load or latency measurement
- trade-offs
- README reproduction steps
- ADR for non-obvious choices

## Initial lab backlog

### Distributed systems
- Idempotent Consumer
- Transactional Outbox
- Retry / DLQ
- Backpressure
- Circuit Breaker
- Fencing Token

### Event architecture
- Event Journal
- Entity Timeline
- Projection Engine
- Projection Replay
- Impact Resolver
- SSE Hint Gateway

### AI engineering
- Repository Relationship Graph
- Bounded Context Builder
- Durable DAG Worker
- Policy-Gated Tool Runtime
- Deterministic Verification
- Evidence Capture

### AI platform
- AI Gateway
- Model Router
- Hybrid RAG
- RAG Evaluation
- Semantic Cache
- MCP Security Gateway
