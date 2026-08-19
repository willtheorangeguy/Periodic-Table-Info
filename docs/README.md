# Periodic Table Info — Documentation

A command-line reference that prints the elements of the periodic table grouped by family.

```
Periodic-Table-Info/
├── main.py       prints the table, then prompts for an element
├── elements.py   element_print_out() — the table itself
├── print.py      a module-level copy of the same output, imported by nothing
└── docs/         this documentation
```

## Pages

- [Quickstart](./quickstart.md) — run it
- [Installation](./installation.md) — source, PyPI, Docker, and how they differ
- [Architecture](./architecture.md) — three files, one of them dead
- [Development](./development.md) — where to start if you fix it
- [FAQ](./faq.md) — the lookup, the missing elements, the old names
- [Troubleshooting](./troubleshooting.md) — what each symptom means
- [Roadmap](./roadmap.md) — direction and non-goals
- [Known issues](./internal/known-issues.md) — recorded defects

## What works, and what does not

**Works:** printing the element list, grouped by family, with atomic numbers and symbols.

**Does not:**

| | |
|---|---|
| The element lookup | Every input returns the "not an element" error, including the example the error itself gives |
| Lanthanides | The heading prints; no elements follow it |
| Actinides | No section at all |
| Elements 113–118 | Still named `Uut`, `Uup`, `Uus`, `Uuo` — placeholders IUPAC replaced in 2016 |

All recorded in [`internal/known-issues.md`](./internal/known-issues.md).

## Two entry points, two behaviours

| How you run it | What happens |
|---|---|
| `python main.py` | Prints the table, then prompts |
| `periodic-table-info` (PyPI) | Prints the table and exits — no prompt |

The console script points at `elements:element_print_out`, which is the table-printing function
alone. The prompt exists only in `main.py`, which the installed package does not run.

So the pip and Docker paths are a strictly smaller program than the source one. See
[Installation](./installation.md).

## As a reference

Worth being plain: a periodic table that omits the lanthanides and actinides and uses element
names withdrawn in 2016 should not be relied on for anything that matters. The grouping and the
first 112 elements are correct.
