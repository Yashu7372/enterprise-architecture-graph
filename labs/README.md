# Enterprise Architecture Labs

Labs are not toy CRUD demos. Each lab should demonstrate one architecture property deeply and include evidence.

Labs are also first-class portfolio evidence. A lab starts as a versioned `lab-manifest.v1` design, becomes RUNNABLE only when its fixtures/evidence path exist, and may become VERIFIED only after measured evidence is available. The content generator may consume the manifest, but it must not turn a DESIGNED hypothesis into a result claim.

Machine-readable contract: [`schema/lab-manifest.schema.json`](schema/lab-manifest.schema.json)

First structured track: [`agentic-architecture-labs/`](agentic-architecture-labs/)

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

For AI/agentic evaluations, also record:

- exact versioned task fixtures
- compared strategy/model variants
- decision inputs and outputs
- evidence requirements independent of model self-judgment
- latency/cost observations where applicable
- repeatability across multiple runs
- failure/invalid-output cases
- the difference between hypothesis, measured finding and published conclusion

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

### Agentic architecture evaluation
- Deterministic Routing vs LLM Numeric Scoring — `LAB-AI-001`
- ReAct vs Plan/Execute vs PEV for repository bug fixing
- Normal execution vs Dry-Run for database changes
- Agentic RAG vs Corrective RAG vs GraphRAG
- Fresh planning vs verified workflow reuse
- Single-agent vs specialist analysis of an unfamiliar repository
- Incident diagnosis strategy comparison
- SWE-style bounded codebase change
- Fixed strategy vs constrained strategy selector
- No memory vs reusable knowledge/workflow context
