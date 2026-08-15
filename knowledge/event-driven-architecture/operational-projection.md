# Operational Projection

**Graph ID:** `operational-projection`  
**Type:** pattern  
**Domain:** event-driven-architecture  
**Maturity:** UNDERSTOOD

## Problem

Rebuilding current business state by repeatedly joining operational tables or replaying full history is too expensive for latency-sensitive downstream features.

## Mental model

Consume accepted events and maintain a query-optimized current-state representation for an entity or intersection of entities.

## Responsibility boundary

A projection worker answers:

> What changed in current operational state?

It should not automatically own every business alert, rule, or UI decision derived from that state.

## Output

A useful projection change contract contains the entity identity, projection version, and changed fields so downstream work can be selective.
