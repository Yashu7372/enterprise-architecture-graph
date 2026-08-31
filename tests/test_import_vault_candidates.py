import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_vault_candidates.py"
SPEC = importlib.util.spec_from_file_location("import_vault_candidates", SCRIPT)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class VaultCandidateImportTests(unittest.TestCase):
    def export(self):
        return {
            "schema_version": "portfolio-candidates.v1",
            "producer": "architecture-vault",
            "generated_at": "2026-08-31T00:00:00+00:00",
            "authority": "candidate-only",
            "concepts": [
                {
                    "candidate_id": "candidate-concept-outbox",
                    "kind": "concept",
                    "concept_id": "transactional-outbox",
                    "name": "Transactional Outbox",
                    "domain": "architecture-patterns",
                    "status": "CANDIDATE",
                    "evidence_state": "EXTRACTED",
                    "confidence": 0.9,
                    "statistics": {"source_documents": 2},
                    "evidence": [{"document_id": "d1", "chunk_id": "c1"}],
                }
            ],
            "relationships": [
                {
                    "candidate_id": "rel-1",
                    "kind": "relationship",
                    "subject_concept_id": "idempotency",
                    "predicate": "STRONGLY_RELATED_TO",
                    "object_concept_id": "transactional-outbox",
                    "status": "CANDIDATE",
                    "evidence_state": "INFERRED",
                    "confidence": 0.7,
                    "statistics": {},
                    "chunk_ids": ["c1", "c2", "c3"],
                    "document_ids": ["d1", "d2"],
                }
            ],
        }

    def test_import_stages_candidates_without_promoting_them(self):
        staged = module.stage_candidates(self.export())
        self.assertEqual("graph-candidate-stage.v1", staged["schema_version"])
        self.assertEqual("review-staging-only", staged["authority"])
        self.assertFalse(staged["promotion_policy"]["automatic_promotion"])
        self.assertEqual("PENDING", staged["concepts"][0]["review_status"])
        self.assertEqual("DISCOVERED", staged["concepts"][0]["suggested_node"]["maturity"])
        self.assertIsNone(staged["concepts"][0]["suggested_node"]["summary"])

    def test_import_rejects_candidate_without_evidence(self):
        export = self.export()
        export["concepts"][0]["evidence"] = []
        with self.assertRaises(ValueError):
            module.stage_candidates(export)

    def test_import_rejects_non_candidate_authority(self):
        export = self.export()
        export["authority"] = "canonical"
        with self.assertRaises(ValueError):
            module.stage_candidates(export)


if __name__ == "__main__":
    unittest.main()
