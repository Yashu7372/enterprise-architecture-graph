# Enterprise Architecture Graph

> A living, version-controlled knowledge graph for enterprise architecture, distributed systems, AI engineering, and production-grade software delivery.

## Why this repository exists

Enterprise architecture knowledge is often fragmented across books, courses, diagrams, codebases, incidents, and implementation experience. This repository connects those ideas into one navigable graph: concepts are linked to the problems they solve, the failure modes they introduce, the patterns that mitigate those failures, and the labs and reference architectures that demonstrate them.

The long-term goal is to build a practical body of evidence for designing and operating modern enterprise systems — from business requirement to architecture, implementation, deployment, observability, incident response, and AI-assisted remediation.

## Current status

**Version:** V0.1 Foundation  
**Status:** Active build  
**Focus:** architecture graph + first reference architectures + learning paths

V0.1 intentionally starts small. The graph currently contains a curated foundation of high-value concepts that will be expanded through implementation, testing, benchmarks, architecture decision records, and public write-ups.

## Core knowledge domains

1. Architecture Foundations
2. Distributed Systems
3. Microservices
4. Event-Driven Architecture
5. Data Architecture
6. Cloud & Platform Engineering
7. Reliability & Production Operations
8. Security Architecture
9. AI Engineering
10. Enterprise GenAI
11. Agentic Systems
12. Enterprise AI Platforms

## Flagship reference architectures

### 1. Chronicle — Real-Time Operational Intelligence

A generic high-volume operational architecture based on canonical events, entity timelines, current-state projections, impact resolution, aggregates, rules, and real-time UI hints.

See: [`architectures/chronicle-operational-intelligence.md`](architectures/chronicle-operational-intelligence.md)

### 2. Forge — AI Engineering Control Plane

A durable engineering orchestration architecture that combines workflow/DAG execution, repository intelligence, relationship graphs, impact analysis, bounded context construction, AI reasoning, deterministic execution, verification, and evidence.

See: [`architectures/forge-ai-engineering-control-plane.md`](architectures/forge-ai-engineering-control-plane.md)

## The long-term combined system

```text
Business Runtime
      │
      ▼
Operational Events
      │
      ▼
Chronicle
      │
      ▼
Operational Knowledge / Incident
      │
      ▼
Forge
      │
      ▼
Investigation → Change → Verification → Deployment
      │
      ▼
Business Runtime
```

The goal is not to build an unconstrained autonomous coding agent. AI is one reasoning capability inside a governed engineering system:

```text
AI reasons
Control plane coordinates
Workers execute
Verifiers prove
Evidence records
```

## Knowledge graph model

Human-readable explanations live in Markdown. Machine-readable graph data lives in YAML.

- [`graph/nodes.yaml`](graph/nodes.yaml) — concepts, patterns, architectures, failure modes, labs, projects
- [`graph/relationships.yaml`](graph/relationships.yaml) — typed edges between graph nodes

Example:

```text
Transactional Outbox
  ├── SOLVES → Dual Write Problem
  ├── MAY_CAUSE → Duplicate Delivery
  ├── COMPLEMENTS → Idempotent Consumer
  └── USED_BY → Chronicle
```

Git remains the canonical source of truth. A graph database or GraphRAG layer may later be generated from these files for visualization and retrieval.

## Learning paths

The same graph supports different role-oriented paths:

- [`AI Engineer`](learning-paths/ai-engineer.md)
- [`AI Solution Architect`](learning-paths/ai-solution-architect.md)
- [`Solution Architect`](learning-paths/solution-architect.md)
- [`Principal Engineer`](learning-paths/principal-engineer.md)

## Knowledge maturity

Every node can move through the following lifecycle:

```text
DISCOVERED → LEARNING → UNDERSTOOD → IMPLEMENTED → TESTED → PUBLISHED → MASTERED
```

A topic is not considered mature merely because it has notes. Strong evidence includes implementation, failure testing, benchmark results, ADRs, architecture diagrams, production reasoning, and interview-ready explanations.

## 69-day build journey

The public journey builds one coherent engineering story instead of 69 unrelated tutorials.

See [`ROADMAP-69-DAYS.md`](ROADMAP-69-DAYS.md).

The final target is an end-to-end demonstration:

```text
Requirement
  → Architecture
  → Repository Analysis
  → Impact Resolution
  → AI-Assisted Plan
  → Deterministic Change
  → Verification
  → Deployment
  → Observability
  → Incident
  → Investigation
  → Remediation
  → Evidence
```

## Repository principles

- Generalize enterprise patterns; never publish employer-confidential implementation details.
- Prefer runnable evidence over opinion-only content.
- Treat failures, security, resilience, observability, and operations as first-class architecture concerns.
- Separate AI reasoning from deterministic execution.
- Keep knowledge graph data portable and version controlled.
- Make trade-offs explicit; avoid presenting one architecture as universally correct.
- Mark architecture, prototype, implemented, and production-ready states accurately.

## V0.1 contents

- Machine-readable graph schema and initial nodes
- Initial graph relationships
- Chronicle architecture specification
- Forge architecture specification
- Four role-oriented learning paths
- 69-day roadmap
- Knowledge-node template
- ADR template
- Lab quality bar

## Planned evolution

```text
V0.1  Knowledge foundation
V0.2  50+ connected architecture nodes
V0.3  First production-shaped labs
V0.4  Chronicle reference implementation
V0.5  Forge reference implementation
V0.6  Interactive graph UI
V0.7  Hybrid graph + semantic retrieval
V0.8  Production operations / incident scenarios
V1.0  Integrated requirement-to-production demonstration
```

## Portfolio intent

This repository is being built as both a learning system and a public architecture portfolio focused on enterprise AI engineering, solution architecture, distributed systems, platform engineering, and production operations.

---

**Current build:** V0.1 — Foundation.
