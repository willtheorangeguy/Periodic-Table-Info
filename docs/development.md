# Periodic Table Info — Development

## Setup

```bash
git clone https://github.com/willtheorangeguy/Periodic-Table-Info
cd Periodic-Table-Info
pip install -r requirements.txt
python main.py
```

No runtime dependencies; `requirements.txt` is the tooling.

## Tests

```bash
pytest
```

`tests/` covers the printing. There is nothing else to cover — the lookup branch has no
behaviour to assert.

## Where to start

Everything on the known-issues list has the same root: **the table is hardcoded as `print()`
calls, so there is no data to query.**

A dict keyed by element name — symbol, atomic number, group, and whatever the "extended
information" is meant to be — would let you:

1. Render the table from it, replacing `elements.py`'s 100 print statements.
2. Implement the lookup in `main.py` as a dictionary access.
3. Fix the missing lanthanides and actinides as data rather than code.
4. Correct elements 113–118 in one place.
5. Delete `print.py`, whose only reason to exist is being a second copy of the same output.

That is one change addressing five recorded issues, which is why it is the recommendation rather
than patching them individually.

## Conventions

- **Module docstring and copyright header** on every file.
- **Pylint**, with per-file disables at the top.
- Standard library only.

## Entry points

`setup.py` and `setup.cfg` declare `periodic-table-info = elements:element_print_out`. If the
prompt is ever meant to be part of the installed command, that needs to point at a function in
`main.py` — see [`internal/known-issues.md`](./internal/known-issues.md).

## Recording defects

Bugs found while working here go in [`internal/known-issues.md`](./internal/known-issues.md)
rather than being fixed in passing, unless fixing them is the job you are on.
