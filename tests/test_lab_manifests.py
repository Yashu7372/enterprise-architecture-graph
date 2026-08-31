from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
LAB_ROOT = ROOT / "labs"
ALLOWED_STATUS = {"DESIGNED", "RUNNABLE", "EXECUTED", "VERIFIED", "PUBLISHED"}


class LabManifestTests(unittest.TestCase):
    def manifests(self):
        return sorted(path for path in LAB_ROOT.glob("**/lab.json") if "schema" not in path.parts)

    def test_repository_has_structured_lab_manifest(self):
        self.assertTrue(self.manifests())

    def test_lab_manifests_keep_evidence_and_publication_boundaries(self):
        for path in self.manifests():
            with self.subTest(path=path):
                lab = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual("lab-manifest.v1", lab.get("schema_version"))
                self.assertIn(lab.get("status"), ALLOWED_STATUS)
                self.assertTrue(lab.get("question"))
                self.assertTrue(lab.get("hypothesis"))
                self.assertGreaterEqual(len(lab.get("variants", [])), 2)
                self.assertTrue(lab.get("task_fixtures"))
                self.assertTrue(lab.get("evidence_requirements"))
                self.assertTrue(lab.get("metrics"))
                self.assertTrue(lab.get("success_criteria"))
                publication = lab.get("publication", {})
                self.assertTrue(publication.get("publish_results_only_after_verification"))
                self.assertTrue(publication.get("content_angles"))

                if lab.get("status") not in {"VERIFIED", "PUBLISHED"}:
                    self.assertNotIn("verified_result", lab)
                    self.assertNotIn("conclusion", lab)


if __name__ == "__main__":
    unittest.main()
