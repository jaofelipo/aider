import unittest
from aider.session_stats import SessionStats

class TestSessionStats(unittest.TestCase):
    def setUp(self):
        self.stats = SessionStats()

    def test_add_commit(self):
        self.stats.add_commit()
        self.assertEqual(self.stats.total_commits, 1)

    def test_add_modified_file(self):
        self.stats.add_modified_file("test.py")
        self.assertEqual(len(self.stats.modified_files), 1)