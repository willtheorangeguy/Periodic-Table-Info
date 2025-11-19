"""Test main.py."""

# pylint: disable=import-error, wrong-import-position, unused-argument, redefined-builtin

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestMain(unittest.TestCase):
    """Test main.py."""

    @patch("builtins.input", return_value="NotAnElement")
    @patch("builtins.print")
    def test_main_execution_with_invalid_input(self, mock_print, mock_input):
        """Test main.py execution with invalid element input."""
        # Import main module which will execute the code
        import importlib
        import main as main_module

        importlib.reload(main_module)

        # Verify input was called
        mock_input.assert_called()

        # Verify error message was printed
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("not an element" in str(call).lower() for call in calls)

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_main_execution_with_empty_input(self, mock_print, mock_input):
        """Test main.py execution with empty input."""
        # Import main module which will execute the code
        import importlib
        import main as main_module

        importlib.reload(main_module)

        # Verify input was called
        mock_input.assert_called()


if __name__ == "__main__":
    unittest.main()
