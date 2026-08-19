<!-- Logo -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Periodic-Table-Info/logo.png" height="250px" width="400px" alt="Periodic Table Info">
  <br>
  Periodic Table Info
  <br>
</h1>

<!-- Copy -->
<h4 align="center">Prints the elements of the periodic table, grouped by family, from the command line.</h4>

<!-- Badges -->
<div align="center">
  <img alt="GitHub Version" src="https://img.shields.io/github/v/release/willtheorangeguy/Periodic-Table-Info?include_prereleases">
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/willtheorangeguy/Periodic-Table-Info">
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/willtheorangeguy/Periodic-Table-Info">
  <img alt="License" src="https://img.shields.io/github/license/willtheorangeguy/Periodic-Table-Info">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#status">Status</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<!-- Screenshot -->
<div align="center">
  <img alt="Periodic Table Info" src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Periodic-Table-Info/welcome.png">
</div>

## Status

**The listing works; the lookup does not.** After printing the table the program asks which element you would like to learn more about, and **every answer** — including `Sodium`, the example its own error message gives — returns "Sorry, that is not an element of the current Periodic Table!".

The table is also incomplete: the Lanthanide heading has no elements beneath it, there is no Actinide section, and elements 113–118 still carry the placeholder names IUPAC replaced in 2016.

See [`docs/internal/known-issues.md`](docs/internal/known-issues.md) for the detail.

## Key Features

- Prints the elements grouped by family — alkali metals, halogens, noble gases, and the rest.
- Numbered by atomic number, with chemical symbols.
- Pure standard library, no dependencies.
- Cross-platform.

## Installation

```bash
git clone https://github.com/willtheorangeguy/Periodic-Table-Info
cd Periodic-Table-Info
python main.py
```

There is also a PyPI package and a Docker image, though both run a smaller program than `main.py` does — see [`docs/installation.md`](docs/installation.md).

## Usage

```bash
python main.py
```

Prints the table, then prompts for an element. The prompt does not currently work; see Status.

## Documentation

Full documentation lives in [`docs/`](docs/README.md):
[Quickstart](docs/quickstart.md) · [Installation](docs/installation.md) · [Architecture](docs/architecture.md) · [Development](docs/development.md) · [FAQ](docs/faq.md) · [Troubleshooting](docs/troubleshooting.md) · [Roadmap](docs/roadmap.md)

## Support

Open a [GitHub Discussion](https://github.com/willtheorangeguy/Periodic-Table-Info/discussions) or file an [issue](https://github.com/willtheorangeguy/Periodic-Table-Info/issues/new/choose).

## Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/willtheorangeguy/Periodic-Table-Info/compare).

See the org-wide [Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/willtheorangeguy/.github/blob/main/CODE_OF_CONDUCT.md).

## Credits

This software uses the following open source packages, projects, services or websites:

<!-- Credits Table -->
<table>
  <tr>
    <th align="center"><img src="https://applets.imgix.net/https%3A%2F%2Fassets.ifttt.com%2Fimages%2Fchannels%2F2107379463%2Ficons%2Fmonochrome_large.png?w=240&h=240&s=8a19bbc158996d098e2fb18310ba7f33" width="150" height="150" alt="GitHub"/></th>
    <th align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/182px-Python-logo-notext.svg.png" width="150" height="150" alt="PSF"/></th>
    <th align="center"><img src="https://pyinstaller.readthedocs.io/en/v4.2/_static/pyinstaller-draft1a.ico" width="150" height="150" alt="PyInstaller"/></th>
    <th align="center"><img src="https://dynamic.indigoimages.ca/v1/books/books/0753471973/1.jpg?width=614&maxheight=614&quality=85" width="150" height="150" alt="Basher"/></th>
    <th align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Wikipedia_logo_%28svg%29.svg/1200px-Wikipedia_logo_%28svg%29.svg.png" width="150" height="150" alt="Wikipedia"/></th>
  </tr>
  <tr>
    <td align="center">GitHub</td>
    <td align="center">Python Software Foundation</td>
    <td align="center">PyInstaller</td>
    <td align="center">Basher</td>
    <td align="center">Wikipedia</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/">Web</a> - <a href="https://github.com/pricing">Plans</a></td>
    <td align="center"><a href="https://www.python.org/">Web</a> - <a href="https://psfmember.org/civicrm/contribute/transact?reset=1&id=2">Donate</a></td>
    <td align="center"><a href="https://pyinstaller.readthedocs.io/en/stable/">Web</a> - <a href="https://www.pyinstaller.org/funding.html#funding-by-individuals">Donate</a></td>
    <td align="center"><a href="https://www.basherscience.com/books">Web</a></td>
    <td align="center"><a href="https://www.wikipedia.org/">Web</a> - <a href="https://donate.wikimedia.org/wiki/Ways_to_Give">Donate</a></td>
  </tr>
</table>

Sponsor [@willtheorangeguy](https://github.com/willtheorangeguy) on [PayPal](https://paypal.me/wvdg44?country.x=CA&locale.x=en_US).

## License

MIT — see [`LICENSE.md`](LICENSE.md).
