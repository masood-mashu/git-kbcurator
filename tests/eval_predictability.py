"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitKbCurator.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.resolution_summarizer import *
from tools.runbook_markdown_formatter import *
from tools.duplicate_article_detector import *

class TestGitKbCuratorPredictability(unittest.TestCase):
    def test_resolution_summarizer(self):
        res = summarize_ticket_resolution("Customer reported 504 gateway timeout. Issue resolved after Nginx reload.")
        self.assertIn("Resolved", res["resolution_summary"])
        self.assertEqual(res["status"], "SUMMARY_CREATED")

    def test_runbook_markdown_formatter(self):
        res = format_runbook_markdown('{"title": "Redis Connection Reset", "steps": ["Verify Redis cluster status", "Flush stale connections"]}')
        self.assertIn("# Redis Connection Reset", res["markdown_content"])
        self.assertEqual(res["status"], "RUNBOOK_FORMATTED")

    def test_duplicate_article_detector(self):
        res = detect_duplicate_articles('{"candidate_title": "How to reset API key", "existing_titles": ["How to setup SSO", "How to manage teams"]}')
        self.assertFalse(res["duplicate_found"])
        self.assertEqual(res["status"], "NO_DUPLICATE_FOUND")


if __name__ == "__main__":
    unittest.main()
