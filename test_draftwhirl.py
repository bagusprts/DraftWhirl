# test_draftwhirl.py
"""
Tests for DraftWhirl module.
"""

import unittest
from draftwhirl import DraftWhirl

class TestDraftWhirl(unittest.TestCase):
    """Test cases for DraftWhirl class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftWhirl()
        self.assertIsInstance(instance, DraftWhirl)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftWhirl()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
