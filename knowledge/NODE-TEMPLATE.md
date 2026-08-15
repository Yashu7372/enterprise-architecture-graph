# <Node Name>

**Graph ID:** `<id>`  
**Type:** concept | pattern | architecture | capability | failure_mode | practice  
**Domain:** `<domain>`  
**Maturity:** DISCOVERED | LEARNING | UNDERSTOOD | IMPLEMENTED | TESTED | PUBLISHED | MASTERED

## Problem

What problem does this concept solve?

## Mental model

Explain it in the simplest technically accurate way.

## Functional behavior

What does it do?

## Non-functional concerns

Latency, throughput, consistency, durability, availability, recoverability, cost, security.

## Architecture / runtime flow

```text
Component A → Component B → Component C
```

## Contracts and state

APIs, events, state, schemas, keys, ownership.

## Failure modes

What breaks and how does failure propagate?

## Resilience

Retries, idempotency, timeouts, fallback, bulkheads, circuit breakers, replay, recovery.

## Security

Trust boundaries, identity, authorization, data exposure, secrets.

## Observability

Logs, metrics, traces, business signals, SLOs.

## Scaling and performance

What becomes the bottleneck at 10x and 100x?

## Trade-offs and alternatives

What alternatives exist, and when should this not be used?

## Lab / evidence

Runnable proof, tests, benchmark, failure injection, ADR.

## Interview explanation

A concise explanation suitable for an architecture interview.

## Graph relationships

- `SOLVES →`
- `REQUIRES →`
- `MAY_CAUSE →`
- `MITIGATED_BY →`
- `USED_BY →`
- `DEMONSTRATED_BY →`
