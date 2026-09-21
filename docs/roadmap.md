# Periodic Table Info — Roadmap

Direction, not a schedule. Defects are in
[`internal/known-issues.md`](./internal/known-issues.md); `PLANNING.md` has the version
checklist.

## Where it is

Prints the elements grouped by family, correctly, for the first 112 of them. The lookup prompt
exists and does nothing.

## Considered

**Element data as data.** The single change everything else depends on: a dict of element name to
properties, rendered into the table and queried by the prompt. It fixes the lookup, removes the
duplicate table in `print.py`, and turns the missing lanthanides and the outdated names into data
edits.

**The lanthanides and actinides.** About 30 elements, currently absent behind a heading that
promises them.

**Current element names.** 113–118 still carry IUPAC placeholders replaced in 2016.

**One entry point.** The installed command runs a smaller program than the source does.

**What "extended information" should be.** The prompt asks; nothing defines what it would show.
Atomic mass, electron configuration, discovery, and uses are the obvious candidates — worth
deciding before building the lookup, since it determines the data model.

## Non-goals

**Becoming a chemistry library.** There are good ones. This prints a table and answers simple
questions about it.

**Fetching data at runtime.** The appeal is that it works offline with no dependencies. Element
data does not change often enough to justify a network call.

**A GUI.** It is a CLI reference; the terminal is the right place for it.

**Inventing the extended information.** Whatever the lookup returns should come from a real
source — the credits already name Wikipedia and Basher — rather than being written to fill the
field.

## Contributing

Issues and pull requests welcome — see the
[Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md).

Converting the table to a dict is the change that makes the rest straightforward.
