# CLAUDE.md

## Project Overview

Periodic Table Info is a Python CLI application for exploring periodic table elements. Users select an element and view its properties (atomic number, symbol, mass, etc.). Published to PyPI as `periodic-table-info`.

## Repository Structure

```
elements.py      # Core module: element data, display logic, element_print_out() entry point
main.py          # CLI entry point, imports from elements
print.py         # Standalone element printing utility
setup.py         # Package configuration (setuptools)
pyproject.toml   # Build system config
tests/           # pytest test suite (test_elements.py, test_main.py, test_print.py, test___main__.py)
docs/            # Documentation and images
.github/workflows/  # CI: pytest, pylint, Docker publish, PyPI publish, CodeQL
```

## Commands

- **Run**: `python main.py`
- **Test**: `pytest --cov=. --cov-report=term-missing -v`
- **Lint**: `pylint elements.py main.py print.py`
- **Install deps**: `pip install -r requirements.txt`
- **Docker**: `docker compose up`

## Code Conventions

- **Indentation**: 4 spaces (never tabs)
- **Comments**: Heavy commenting is expected per CONTRIBUTING.md
- **Docstrings**: Required on all functions
- **Versioning**: Semantic Versioning (currently v0.3.0)
- **Python**: Supports 3.9, 3.10, 3.11, 3.12
- **No external runtime dependencies** — only pytest/pytest-cov for testing
- **Pylint**: Some warnings are suppressed via inline directives (`# pylint: disable=...`)

## Git Workflow

- **Main branch**: `master`
- **Workflow**: GitHub Flow (branch from master, PR back)
- **CI runs**: pytest on Python 3.9–3.12, pylint on 3.9

## Adding Elements

New elements are added in `elements.py`. Follow the existing pattern of `elif` blocks in `element_print_out()`, printing element properties in the established format.

## License

MIT
