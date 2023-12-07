"""Test main.py."""
# pylint: disable=import-error, wrong-import-position, unused-argument, redefined-builtin

import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import element_print_out


class TestMain(unittest.TestCase):
    """Test main.py."""
    @patch("builtins.input", return_value="NotAnElement")
    def test_input_invalid(self, input):
        """Test input invalid element."""
        self.assertEqual(element_print_out(), None)


if __name__ == "__main__":
    unittest.main()
