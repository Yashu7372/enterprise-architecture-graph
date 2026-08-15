# Context Engineering

**Graph ID:** `context-engineering`  
**Type:** capability  
**Domain:** ai-engineering  
**Maturity:** LEARNING

## Problem

An enterprise repository landscape is too large, noisy, and security-sensitive to pass wholesale into every AI request.

## Mental model

Build the smallest trustworthy task-specific context that contains the evidence needed to reason correctly.

## Inputs

- repository relationships
- impact analysis
- task requirements
- changed files
- relevant contracts
- architecture constraints
- prior evidence

## Output

A bounded immutable context pack with provenance and explicit omissions.

## Principle

AI may request additional context when necessary, but broad rediscovery should be the exception rather than the default execution model.
