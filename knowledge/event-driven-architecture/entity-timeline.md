# Entity Timeline

**Graph ID:** `entity-timeline`  
**Type:** architecture  
**Domain:** event-driven-architecture  
**Maturity:** UNDERSTOOD

## Problem

Current-state tables answer "what is true now" but often lose the sequence of changes needed for diagnostics, replay, temporal reasoning, and lineage.

## Mental model

For each business entity, preserve the accepted sequence of events that explains how its state evolved.

## Uses

- reconstruct state
- investigate anomalies
- replay projections
- reason about late events
- preserve evidence and lineage

## Relationship to projections

The timeline is temporal history. A projection is optimized current state. They are related but not interchangeable.

## Related graph relationships

- `BUILDS_ON → event-journal`
- `FEEDS → operational-projection`
- `USED_BY → chronicle`
