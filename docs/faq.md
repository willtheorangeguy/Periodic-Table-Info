# Periodic Table Info — FAQ

### I typed an element and it said it is not an element.

Every input does that. The only branch that matches is the empty string; everything else falls to
the error — including `Sodium`, which the error message itself offers as an example of correct
formatting.

There is no element data behind the prompt. Recorded in
[`internal/known-issues.md`](./internal/known-issues.md).

### Why is there a `None` after the table?

`main.py` does `print(element_print_out())`. The function prints the table and returns nothing, so
`print` renders that `None`.

### Where are the lanthanides?

The heading prints; no elements follow it. There is no actinide section at all. Together that is
about 30 elements missing from a program that prints "all the elements".

### Why is element 118 called "Unknown Element (Uuo)"?

Those are IUPAC's systematic placeholder names, used before an element is formally named.
Elements 113 to 118 all received permanent names by 2016:

| Number | Shown as | Actual |
|---|---|---|
| 113 | Uut | Nihonium (Nh) |
| 114 | Uuq | Flerovium (Fl) |
| 115 | Uup | Moscovium (Mc) |
| 116 | Uuh | Livermorium (Lv) |
| 117 | Uus | Tennessine (Ts) |
| 118 | Uuo | Oganesson (Og) |

### Can I rely on this as a reference?

For the first 112 elements and the family groupings, yes. For anything beyond that, no — see
above.

### Why does the pip command behave differently?

The console script runs `elements:element_print_out`, which prints the table and returns. The
prompt is only in `main.py`. See [Installation](./installation.md).

### What is `print.py`?

A second copy of the table's output, at module level, imported by nothing. See
[Architecture](./architecture.md).

### Does it need internet, or write anything?

No to both. It prints and exits.
