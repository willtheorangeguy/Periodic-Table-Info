# Periodic Table Info — Architecture

Three files, 250 lines, and one of them is unused.

```
main.py       print(element_print_out())  →  input()  →  a branch that never matches
elements.py   element_print_out()          the table, as a sequence of print() calls
print.py      the same output again, at module level, imported by nothing
```

## `elements.py`

`element_print_out()` is 100 lines of `print()` calls — the elements, grouped by family, in
atomic-number order within each group.

Hardcoding the table as print statements is a reasonable choice for a program that only ever
displays it. It becomes the problem the moment anything needs to *look up* an element, because
there is no data structure to look one up in.

The function returns `None`, which is why `main.py` prints a stray `None` after the table.

It also stops at `print("Lanthanide Elements")` — the heading with nothing beneath it — and there
is no actinide section. Elements 113 to 118 carry the placeholder names IUPAC replaced in 2016.
See [`internal/known-issues.md`](./internal/known-issues.md).

## `main.py`

```python
print(element_print_out())
input_from_user = input("Please enter the element you would like to learn more about: ")
if input_from_user.lower() == "":
    print("")
else:
    print("Sorry, that is not an element of the current Periodic Table!")
```

The only matching branch is the empty string, which prints an empty line. Everything else — every
element name — falls to the error.

This is the shape of a feature that was scaffolded and never filled in: the prompt, the
validation message, and the formatting advice all exist; the lookup does not.

## `print.py`

109 lines reproducing `elements.py`'s output at module level, with no function. Nothing imports
it, and `main.py` uses `elements`.

Two copies of the same table will drift, and correcting the missing lanthanides in one would
leave the other wrong. The filename also shadows the builtin `print` for anything that does
`import print`.

## Entry points

| Route | Runs |
|---|---|
| `python main.py` | The table and the prompt |
| `periodic-table-info` | `elements:element_print_out` — the table alone |

## What implementing the lookup would need

A data structure — a dict of name to properties — which `element_print_out` could also render
from, replacing both hardcoded copies. That single change would fix the lookup, remove the
duplication, and make the missing lanthanides a data edit rather than a code one.
