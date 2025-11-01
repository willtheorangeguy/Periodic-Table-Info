"""Test print.py."""

# pylint: disable=import-error, wrong-import-position

import sys
import os
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_print_module_output(capfd):
    """Test that print.py produces the expected output."""
    # Mock print to capture output then reload the print module
    import importlib
    import print as print_module

    # Reload to capture the output
    importlib.reload(print_module)
    captured = capfd.readouterr()

    # Verify key elements are printed
    assert "--THE PERIODIC TABLE ELEMENTS--" in captured.out
    assert "1. Hydrogen (H)" in captured.out
    assert "Alkali Metals - Group 1" in captured.out
    assert "3. Lithium (Li)" in captured.out
    assert "Noble Gases - Group 18" in captured.out
    assert "Lanthanide Elements" in captured.out
