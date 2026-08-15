# Chronicle — Real-Time Operational Intelligence Platform

**Status:** Architecture / active portfolio implementation track  
**Domain:** Generic logistics / operational systems  
**Purpose:** Demonstrate scalable event-driven operational intelligence without exposing employer-specific systems or rules.

## Problem

Large operational systems receive continuous changes from many domain services. If every downstream feature independently joins operational tables, polls frequently, or reconstructs the same state, the platform accumulates duplicated processing, database load, inconsistent interpretations, and slow UI refresh cycles.

Chronicle explores a generic alternative: accept domain-owned events, maintain durable event history, materialize current operational state, determine exactly what changed, and selectively trigger only affected downstream computations.

## Reference flow

```text
Domain Services
      │
      ▼
Local Transaction + Outbox
      │
      ▼
Event Broker
      │
      ▼
Canonical Event Envelope
      │
      ▼
Canonical Event Journal
      │
      ▼
Entity Timeline
      │
      ▼
Operational Projection Worker
      │
      ├── Shipment Projection
      ├── Package Projection
      ├── Container Projection
      └── Journey Projection
      │
      ▼
Projection Change
      │
      ▼
Impact Resolver
      │
      ├── Aggregate Workers
      ├── Rule Workers
      ├── View Workers
      └── Notification Hints
      │
      ▼
Read API / SSE Hint / Dashboard
```

## Design principles

1. Domain services retain business ownership.
2. The canonical envelope standardizes cross-domain metadata, not business meaning.
3. The journal is append-oriented evidence for accepted events.
4. Timelines preserve temporal evolution; projections serve current-state reads.
5. Projection workers answer "what is the current state?" rather than "what business decision should be made?"
6. Impact resolution is deterministic and change-driven.
7. Real-time notification prefers lightweight invalidation/hints; clients fetch authoritative view data.
8. Replay and recovery are first-class, not emergency scripts.

## Example domain

Public examples use logistics concepts:

- Shipment
- Package
- Container
- Vehicle
- Facility
- Journey

No employer-specific data, event names, schemas, thresholds, or internal topology are required.

## Failure scenarios to demonstrate

- Duplicate delivery
- Out-of-order events
- Late events
- Consumer restart
- Broker outage
- projection-store outage
- stale projection version
- replay after projection corruption
- poison event
- concurrent updates
- hot entity / hot partition

## NFR targets for the portfolio implementation

The implementation will define explicit targets for:

- event ingestion throughput
- projection update latency
- read latency
- replay recovery time
- duplicate processing safety
- availability under partial dependency failure
- observability coverage

Targets will be measured rather than presented as unsupported production claims.

## Planned implementation evidence

- architecture diagrams
- contract schemas
- projection state machine
- replay test
- duplicate-event test
- failure injection
- load test
- OpenTelemetry traces
- benchmark notes
- ADRs

## Related graph nodes

`transactional-outbox`, `canonical-event`, `event-journal`, `entity-timeline`, `operational-projection`, `projection-change`, `impact-resolver`, `idempotent-consumer`
