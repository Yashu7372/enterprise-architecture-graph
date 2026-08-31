# Architecture Vault Candidate Staging

This directory is a review boundary between experimental research acquisition in Architecture Vault and the curated public architecture graph.

Architecture Vault may discover or infer useful concepts and relationships, but it does not write directly to `graph/nodes.yaml` or `graph/relationships.yaml`.

## Flow

```text
Architecture Vault collectors
        |
        v
portfolio-candidates.v1.json
        |
        v
scripts/import_vault_candidates.py
        |
        v
graph/candidates/architecture-vault.generated.json
        |
        v
human review / rewrite / dedupe / evidence check
        |
        +--> graph/nodes.yaml
        +--> graph/relationships.yaml
        +--> knowledge/*.md
        +--> labs/*
```

The generated staging file is intentionally not canonical graph truth. Every staged record has `review_status=PENDING`, and the importer never mutates curated graph files.

## Import

```bash
python scripts/import_vault_candidates.py /path/to/architecture-vault/engineering-knowledge-base/output/exports/portfolio-candidates.v1.json
```

Reviewers should promote only material that is useful for the architect/portfolio graph, rewrite summaries in original language, preserve safe source/evidence references, and reject duplicate or weak relationships.
