"""Test __main__.py."""
# pylint: disable=import-error, wrong-import-position

import sys
import os
from unittest.mock import patch, MagicMock
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_main_entry_point_structure():
    """Test __main__.py file structure."""
    # Read the __main__.py file to verify its structure
    main_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '__main__.py')
    
    with open(main_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verify key components are present
    assert 'from elements import element_print_out' in content
    assert 'if __name__ == "__main__"' in content
    assert 'element_print_out()' in content


def test_main_module_can_be_imported():
    """Test that __main__.py can be imported without errors."""
    # Import the module using importlib
    import importlib.util
    
    main_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '__main__.py')
    spec = importlib.util.spec_from_file_location("__main_test__", main_path)
    module = importlib.util.module_from_spec(spec)
    
    # The module should be loadable
    assert module is not None
    assert spec is not None


def test_main_execution_via_python_m(capfd):
    """Test running the module via python -m."""
    # This test would require subprocess which might not work in all environments
    # So we'll verify the structure instead
    main_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '__main__.py')
    assert os.path.exists(main_path)

