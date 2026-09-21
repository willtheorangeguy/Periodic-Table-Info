# Periodic Table Info — Installation

## Requirements

Python 3.x. No dependencies.

## From source — the full program

```bash
git clone https://github.com/willtheorangeguy/Periodic-Table-Info
cd Periodic-Table-Info
python main.py
```

This is the only route that includes the element prompt, such as it is.

## From PyPI — the table only

```bash
pip install periodic-table-info
periodic-table-info
```

The console script is declared as `periodic-table-info = elements:element_print_out`, which is the
function that prints the table. It returns immediately afterwards.

So the installed command prints the list and exits. `main.py` — which adds the prompt — is not
what the entry point runs. Recorded in
[`internal/known-issues.md`](./internal/known-issues.md).

## Docker

The image runs the same entry point, with the same consequence.

## Which to use

| You want | Use |
|---|---|
| The element list | Any of them |
| The prompt as well | `python main.py` from a clone |

Given the prompt does not resolve any element, the difference is currently academic — but it is
worth knowing that the packaged program and the source program are not the same.

## Verify

```bash
python main.py
```

The table prints. If it ends at "Lanthanide Elements" with nothing after it, that is the expected
(incomplete) output, not a truncated install.

## Uninstall

```bash
pip uninstall periodic-table-info
```

Nothing is written to disk at any point.
