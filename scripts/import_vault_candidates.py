from __future__ import annotations

from argparse import ArgumentParser
from datetime import datetime, timezone
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "graph" / "candidates" / "architecture-vault.generated.json"
INPUT_SCHEMA = "portfolio-candidates.v1"
OUTPUT_SCHEMA = "graph-candidate-stage.v1"


def _required_text(value, field: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise ValueError(f"missing required field: {field}")
    return text


def validate_export(export: dict) -> None:
    if export.get("schema_version") != INPUT_SCHEMA:
        raise ValueError(f"unsupported Architecture Vault export schema: {export.get('schema_version')!r}")
    if export.get("authority") != "candidate-only":
        raise ValueError("Architecture Vault import must be candidate-only")

    for index, candidate in enumerate(export.get("concepts", [])):
        if candidate.get("kind") != "concept" or candidate.get("status") != "CANDIDATE":
            raise ValueError(f"concept candidate {index} is not a CANDIDATE concept")
        _required_text(candidate.get("concept_id"), f"concepts[{index}].concept_id")
        _required_text(candidate.get("name"), f"concepts[{index}].name")
        if not candidate.get("evidence"):
            raise ValueError(f"concept candidate {candidate.get('concept_id')} has no evidence")

    for index, candidate in enumerate(export.get("relationships", [])):
        if candidate.get("kind") != "relationship" or candidate.get("status") != "CANDIDATE":
            raise ValueError(f"relationship candidate {index} is not a CANDIDATE relationship")
        _required_text(candidate.get("subject_concept_id"), f"relationships[{index}].subject_concept_id")
        _required_text(candidate.get("predicate"), f"relationships[{index}].predicate")
        _required_text(candidate.get("object_concept_id"), f"relationships[{index}].object_concept_id")


def stage_candidates(export: dict) -> dict:
    validate_export(export)

    concepts = []
    for candidate in export.get("concepts", []):
        concepts.append(
            {
                "candidate_id": candidate["candidate_id"],
                "source_concept_id": candidate["concept_id"],
                "review_status": "PENDING",
                "confidence": candidate.get("confidence"),
                "evidence_state": candidate.get("evidence_state"),
                "suggested_node": {
                    "id": candidate["concept_id"],
                    "name": candidate["name"],
                    "type": "concept",
                    "domain": candidate.get("domain"),
                    "maturity": "DISCOVERED",
                    "summary": None,
                },
                "statistics": candidate.get("statistics", {}),
                "evidence": candidate.get("evidence", []),
            }
        )

    relationships = []
    for candidate in export.get("relationships", []):
        relationships.append(
            {
                "candidate_id": candidate["candidate_id"],
                "review_status": "PENDING",
                "confidence": candidate.get("confidence"),
                "evidence_state": candidate.get("evidence_state"),
                "suggested_relationship": {
                    "source": candidate["subject_concept_id"],
                    "type": candidate["predicate"],
                    "target": candidate["object_concept_id"],
                },
                "statistics": candidate.get("statistics", {}),
                "chunk_ids": candidate.get("chunk_ids", []),
                "document_ids": candidate.get("document_ids", []),
            }
        )

    return {
        "schema_version": OUTPUT_SCHEMA,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "producer": "enterprise-architecture-graph",
        "source": {
            "producer": export.get("producer"),
            "schema_version": export.get("schema_version"),
            "generated_at": export.get("generated_at"),
        },
        "authority": "review-staging-only",
        "promotion_policy": {
            "automatic_promotion": False,
            "target_nodes": "graph/nodes.yaml",
            "target_relationships": "graph/relationships.yaml",
            "requires": [
                "human-review",
                "original-summary",
                "portfolio-safe-wording",
                "evidence-and-provenance-check",
                "duplicate-and-conflict-check",
            ],
        },
        "concepts": concepts,
        "relationships": relationships,
    }


def main() -> int:
    parser = ArgumentParser(description="Stage Architecture Vault candidates without mutating the curated graph.")
    parser.add_argument("input", type=Path, help="Architecture Vault portfolio-candidates.v1.json export")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    export = json.loads(args.input.read_text(encoding="utf-8"))
    staged = stage_candidates(export)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(staged, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PASS",
                "concept_candidates": len(staged["concepts"]),
                "relationship_candidates": len(staged["relationships"]),
                "output": str(args.output),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
