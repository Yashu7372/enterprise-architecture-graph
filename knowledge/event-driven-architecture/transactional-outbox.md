# Transactional Outbox

**Graph ID:** `transactional-outbox`  
**Type:** pattern  
**Domain:** event-driven-architecture  
**Maturity:** UNDERSTOOD

## Problem

A service often needs to update its database and publish an event. Those two operations cannot normally participate in one atomic transaction, creating a dual-write failure window.

## Mental model

Store the business change and a message-to-be-published in the same local transaction. A separate publisher later sends the outbox record to the broker.

## Important consequence

The pattern improves atomicity between local state and the intent to publish, but delivery is commonly at-least-once. Consumers still need duplicate safety.

## Failure modes

- publisher crash after publish but before marking sent
- duplicate broker delivery
- outbox backlog
- poison record
- ordering across partitions/entities

## Related graph relationships

- `COMPLEMENTS → idempotent-consumer`
- `USED_BY → chronicle`
