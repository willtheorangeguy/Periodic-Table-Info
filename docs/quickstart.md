# Periodic Table Info — Quickstart

## Run it

```bash
git clone https://github.com/willtheorangeguy/Periodic-Table-Info
cd Periodic-Table-Info
python main.py
```

No dependencies.

## What you get

The elements printed by family:

```
--THE PERIODIC TABLE ELEMENTS--

1. Hydrogen (H)

Alkali Metals - Group 1
3. Lithium (Li)
11. Sodium (Na)
...
```

Then, at the end, a stray `None` — see below — and a prompt.

## The prompt does not work

```
Please enter the element you would like to learn more about: Sodium
Sorry, that is not an element of the current Periodic Table!
Remember to type it like this: 'Sodium' or 'sodium'. ...
```

Every input takes that branch, including the exact example the message suggests. There is no
element data behind the prompt to look anything up in.

Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

## The `None`

`main.py` does `print(element_print_out())`. The function prints the table and returns nothing,
so `print` renders its `None` on a line of its own after the table.

## What is missing from the table

- **Lanthanides** — the heading prints with no elements under it.
- **Actinides** — no section at all.
- **113–118** — shown as `Unknown Element (Uut)` and similar. IUPAC named all six by 2016:
  Nihonium, Flerovium, Moscovium, Livermorium, Tennessine, Oganesson.

## Installed from PyPI

```bash
pip install periodic-table-info
periodic-table-info
```

Prints the table and exits. The prompt is not part of the installed command — see
[Installation](./installation.md).
