# Forge — AI Engineering Control Plane

**Status:** Architecture / active portfolio implementation track  
**Purpose:** Demonstrate a governed engineering system where AI reasons, durable orchestration coordinates, deterministic workers execute, and verification produces evidence.

## Problem

AI coding assistants often operate as a loop around a terminal: inspect some files, propose a change, run commands, read failures, and try again. That can be useful locally, but enterprise engineering needs stronger guarantees around scope, repository knowledge, concurrency, retries, approvals, reproducibility, security, verification, and auditability.

Forge separates reasoning from execution.

## Reference flow

```text
Engineering Request
        │
        ▼
Governance / Policy
        │
        ▼
Workflow Engine
        │
        ▼
Durable DAG Scheduler
        │
        ▼
Worker Registry
        │
 ┌──────┼──────────┬───────────┐
 ▼      ▼          ▼           ▼
Repo  Workspace  Intelligence Runtime
                         │
                         ▼
               Relationship Graph
                         │
                         ▼
                  Impact Resolver
                         │
                         ▼
                    Working Set
                         │
                         ▼
                   Context Builder
                         │
                         ▼
                    AI Reasoning
                         │
                         ▼
              Deterministic Workers
                         │
                         ▼
                    Verification
                         │
                         ▼
                      Evidence
```

## Core separation

```text
AI decides / reasons
Control plane coordinates
Workers perform mechanics
Verifiers independently check outcomes
Evidence records what happened
```

The model should not be responsible for durable process control, locking, retries, task-state persistence, or truthfully claiming that a build/test succeeded.

## Two graphs remain separate

### Workflow DAG

Controls execution dependencies:

```text
Analyze A ─┐
Analyze B ─┼─► Build Graph ─► Resolve Impact ─► Plan ─► Change ─► Verify
Analyze C ─┘
```

### Knowledge / relationship graph

Represents software relationships:

```text
Service A ─CALLS_API→ Service B
Service B ─READS_TABLE→ Customer
Service C ─CONSUMES→ OrderCreated
```

A workflow DAG answers **what work can run now?**  
A relationship graph answers **what is connected and what may be affected?**

## Durable execution requirements

- persisted workflow and task state
- dependencies
- READY / RUNNING / BLOCKED / FAILED / SUCCEEDED semantics
- retry policy
- worker leases
- heartbeats
- cancellation
- approval gates
- resource locks where needed
- typed failures
- partial/degraded success
- evidence capture

## Repository intelligence

The platform should progressively understand:

- modules
- services
- APIs
- event producers/consumers
- database reads/writes
- configuration dependencies
- tests
- build relationships
- framework semantics

Facts should preserve evidence, source location, confidence, and unresolved state.

## Context engineering

The AI receives a bounded immutable task context assembled from deterministic knowledge and impact analysis. It should not independently rediscover the entire organization for every task.

## Verification

AI reasoning is not proof. Verification should include appropriate deterministic checks such as:

- compile/build
- unit tests
- integration tests
- contract tests
- static analysis
- security scanners
- policy checks
- runtime smoke tests
- deployment health checks

## Configurable delivery workflows

Forge should support organization-specific lifecycle models without hard-coding Agile or Waterfall.

```yaml
workflow:
  methodology: agile
  stages:
    - requirement
    - refinement
    - architecture
    - implementation
    - verification
    - review
    - deployment
    - production_validation
```

The same engine can execute a regulated or waterfall workflow with different stages and approval gates.

## Planned task scenarios

- feature implementation
- bug repair
- dependency upgrade
- migration
- security remediation
- test generation
- incident investigation
- documentation and architecture analysis

## Related graph nodes

`durable-dag`, `repository-relationship-graph`, `impact-resolver`, `context-engineering`, `deterministic-verification`, `evidence-model`
