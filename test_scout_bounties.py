import unittest

from scout_bounties import (
    has_bounty_signal,
    is_clean_candidate,
    pluralize_opportunity,
)


class BountySignalTests(unittest.TestCase):
    def test_rejects_generic_bounty_mentions_without_concrete_signal(self):
        item = {
            "title": "MRWK bounty: code health and app.main expansion readiness",
            "body": "Tracking internal bounty scanner output.",
            "comments": 2,
            "labels": [],
        }

        self.assertFalse(has_bounty_signal(item))
        self.assertFalse(is_clean_candidate(item))

    def test_accepts_monetary_bounty_signal(self):
        item = {
            "title": "[Bounty $7k] Enforce workspace scope in analytics queries",
            "body": "Reward paid after accepted PR.",
            "comments": 2,
            "labels": [],
        }

        self.assertTrue(has_bounty_signal(item))
        self.assertTrue(is_clean_candidate(item))

    def test_accepts_bounty_label_signal(self):
        item = {
            "title": "Fix Swagger UI asset configuration",
            "body": "Help wanted.",
            "comments": 0,
            "labels": [{"name": "bounty"}],
        }

        self.assertTrue(has_bounty_signal(item))
        self.assertTrue(is_clean_candidate(item))

    def test_rejects_assigned_or_overcrowded_candidates(self):
        assigned = {
            "title": "[Bounty $100] Fix bug",
            "body": "",
            "comments": 0,
            "labels": [],
            "assignees": [{"login": "developer"}],
        }
        overcrowded = {
            "title": "[Bounty $100] Fix bug",
            "body": "",
            "comments": 26,
            "labels": [],
        }

        self.assertFalse(is_clean_candidate(assigned))
        self.assertFalse(is_clean_candidate(overcrowded))

    def test_pluralizes_opportunity(self):
        self.assertEqual(pluralize_opportunity(1), "opportunity")
        self.assertEqual(pluralize_opportunity(2), "opportunities")


if __name__ == "__main__":
    unittest.main()
