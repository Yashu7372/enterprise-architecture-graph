# Durable DAG Execution

**Graph ID:** `durable-dag`  
**Type:** architecture  
**Domain:** ai-engineering  
**Maturity:** UNDERSTOOD

## Problem

Long-running engineering work cannot depend on one model session or one process surviving from start to finish.

## Mental model

Represent work as tasks connected by dependencies. Persist task state. Execute every READY task through workers. Recover after crashes without forgetting completed work.

## Core semantics

- dependency graph
- durable task state
- READY / RUNNING / BLOCKED / terminal states
- retries
- worker leases
- heartbeats
- cancellation
- approvals
- failure propagation
- evidence

## Important distinction

The workflow DAG represents execution dependencies. It is separate from the software relationship/knowledge graph.
