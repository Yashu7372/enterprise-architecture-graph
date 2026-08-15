# Idempotency

**Graph ID:** `idempotency`  
**Type:** concept  
**Domain:** distributed-systems  
**Maturity:** UNDERSTOOD

## Mental model

Repeating the same logical operation should not create additional unintended effects.

## Why it matters

Distributed systems retry. Brokers redeliver. Clients retry timed-out requests. Workers can crash after side effects but before acknowledgement. Idempotency converts many of these ambiguous retries into safe repetition.

## Typical mechanisms

- idempotency key
- processed-message store
- unique database constraint
- compare-and-set/version check
- deterministic operation identifier

## Trade-off

Idempotency requires defining what constitutes the same logical operation and how long that identity must be remembered.
