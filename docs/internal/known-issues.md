# Known Issues — Periodic-Table-Info

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.

**6 open:** 1 high, 3 medium, 2 low.

## 1. Every element lookup fails, including the example the error message gives

**Severity:** High
**Where:** `main.py`

**What:**     if input_from_user.lower() == "":
        print("")
    else:
        print("Sorry, that is not an element of the current Periodic Table!")

The only branch that matches is the empty string. Every element name falls to the `else`. Verified by running it: entering `Sodium` -- the exact example the error message offers as correctly-formatted input -- produces the error. There is no element data anywhere in the project to look anything up in; the table is 100 hardcoded `print()` calls.

**Why it matters:** 'Offers extended information on each element' was the third of four Key Features, and it is the only interactive thing the program does. What exists is the shape of the feature -- the prompt, the validation message, and formatting advice about capitalisation and punctuation -- with nothing behind it. The error is worse than a plain 'not implemented' would be, because it tells the user they typed it wrong and then demonstrates the format they supposedly should have used. Someone will retype `sodium`, then `Na`, then `11` before concluding the program is broken rather than themselves.

**Suggested fix:** The prompt needs element data to query. A dict of name to properties would serve both it and `element_print_out`, which currently hardcodes the same information as print statements -- see the entry below on the duplicate table. Until then, saying so in the message would be kinder than the current advice.

## 2. The table omits the lanthanides and actinides, about 30 elements

**Severity:** Medium
**Where:** `elements.py` -> `element_print_out`

**What:** The function's final statement is `print("Lanthanide Elements")`. Nothing follows it -- no lanthanides, and no actinide section at all. Verified by running it: the output ends with that heading. The README described the program as printing 'a list of Periodic Table elements' and the module docstring says 'Print all the elements in the Periodic Table of the Elements'.

**Why it matters:** A heading with nothing under it is worse than an omission, because it reads as a rendering failure rather than missing content -- a user sees 'Lanthanide Elements' and reasonably assumes their terminal truncated the output. Thirty of 118 elements is a quarter of the table, including every element anyone looks up for a chemistry course. For a reference tool the correctness of the data is the whole product.

**Suggested fix:** Add both series. If the table becomes a data structure (see above), this is a data edit rather than 30 more print statements in two files.

## 3. Elements 113 to 118 use placeholder names withdrawn in 2016

**Severity:** Medium
**Where:** `elements.py`

**What:** The table lists `Element 113 - Unknown Element (Uut)`, `(Uup)`, `(Uus)`, and `(Uuo)`. These are IUPAC systematic placeholders used before an element is formally named. All six of elements 113 to 118 were named by 2016: Nihonium (Nh), Flerovium (Fl), Moscovium (Mc), Livermorium (Lv), Tennessine (Ts), and Oganesson (Og).

**Why it matters:** The tool's purpose is being a correct reference, and this is a decade of drift on the part of the table most likely to be looked up out of curiosity -- nobody consults a CLI to find out about hydrogen. 'Unknown Element' is also actively wrong rather than merely dated: these elements are synthesised, characterised, and named. Anyone using this to check a homework answer gets a wrong one.

**Suggested fix:** Replace all six with their current names and symbols. Worth checking the rest of the table against a current source at the same time, since the same vintage applies to all of it.

## 4. The installed command runs a smaller program than the source does

**Severity:** Medium
**Where:** `setup.py`, `setup.cfg` -> `console_scripts`; `main.py`

**What:** Both declare `periodic-table-info = elements:element_print_out`. That function prints the table and returns. The prompt, and everything after it, lives in `main.py`, which the entry point does not reference -- so `pip install periodic-table-info && periodic-table-info` prints the list and exits. The Docker image runs the same entry point.

**Why it matters:** The README documented pip and Docker alongside the source checkout as three ways to run the same application, and they are not: two of them silently drop the interactive half. It currently matters little because the prompt does not work -- but it means fixing the prompt would not reach any installed user, and the packaged program would still be missing the feature after the bug was closed.

**Suggested fix:** Point the entry point at a `main()` in `main.py` that does both, and have `main.py` guard it with `if __name__ == "__main__"` so importing it stays side-effect free.

## 5. print.py is a second copy of the table, imported by nothing

**Severity:** Low
**Where:** `print.py`, `elements.py`

**What:** 109 lines reproducing `element_print_out`'s output as module-level `print()` calls, with no function wrapper. Nothing imports it -- `main.py` uses `elements`, and both packaging files point at `elements`. The filename also shadows the builtin for any module doing `import print`.

**Why it matters:** Two copies of the same 100-line table will drift, and the drift is invisible: correcting the missing lanthanides in `elements.py` would leave `print.py` wrong, and nothing would report it. Because it executes at import rather than defining a function, importing it for any reason prints the whole table as a side effect. Anyone grepping for an element finds two hits and no indication which is live.

**Suggested fix:** Delete it. If the intent was a script-style variant, `python -c 'from elements import element_print_out; element_print_out()'` covers it without a second copy.

## 6. A stray None is printed after the table

**Severity:** Low
**Where:** `main.py` -> `print(element_print_out())`

**What:** `element_print_out` prints the table and returns `None` implicitly. Wrapping the call in `print()` renders that `None` on its own line between the table and the prompt.

**Why it matters:** Cosmetic, and the smallest thing here -- but it is the last line of output before the program asks the user a question, so it is on screen at the moment they are deciding whether the program is working. Combined with the table ending on an empty heading, the closing impression is of something half-finished.

**Suggested fix:** Call it without wrapping: `element_print_out()`. Or have it return the string and print that, which would also make it testable.

---

## Also, across every repository

**`.bandit` is present on disk but untracked in git.** Verified in PyWorkout, treklogger,
skyscanner-cli, booking-cli, piggy, and aibot — the config file exists locally in each but
`git ls-files` does not know about it, so none of it reached GitHub.

The August 2026 security sweep therefore looks complete locally and landed nowhere. Worth
checking across all 44 repositories it covered.
