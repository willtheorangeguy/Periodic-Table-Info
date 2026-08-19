# Periodic Table Info — Troubleshooting

## "Sorry, that is not an element of the current Periodic Table!"

Every input produces this, including the example the message gives. The lookup is not
implemented — see [`internal/known-issues.md`](./internal/known-issues.md).

Nothing you type will work. Press Enter on an empty line to exit without the error.

## A stray `None` after the table

`print(element_print_out())` printing the function's `None` return. Cosmetic.

## The list stops at "Lanthanide Elements"

That is the end of the output. The lanthanides were never added, and there is no actinide
section. Not a truncated install.

## Elements 113–118 have odd names

`Uut`, `Uup`, `Uus`, `Uuo` are IUPAC placeholder names, superseded in 2016. See [FAQ](./faq.md)
for the real ones.

## `periodic-table-info` prints the table and exits

Expected. The console script runs the table-printing function; the prompt lives in `main.py`. Run
from a clone if you want it.

## `ModuleNotFoundError: No module named 'elements'`

`main.py` does `from elements import element_print_out`, a flat import that needs the repository
root on `sys.path`. Run it from the repository root:

```bash
cd Periodic-Table-Info
python main.py
```

## Something imported `print.py` instead of the builtin

`print.py` shadows the builtin name for anything doing `import print`. Nothing in this project
does, and nothing imports the file at all — it is dead.

## Still stuck

[Open an issue](https://github.com/willtheorangeguy/Periodic-Table-Info/issues/new/choose) with
the command and the output.
