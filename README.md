<!-- Logo -->
<h1 align="center">
  <img src="https://github.com/Dog-Face-Development/Periodic-Table-Info/blob/master/docs/images/logo.png" height="350px" width="400px" alt="Periodic Table Info">
  <br>
  Periodic Table Info
  <br>
</h1>

<!-- Copy -->
<h4 align="center">Print all the elements in the Periodic Table of the Elements, with an interactive prompt to learn more.</h4>

<!-- Badges -->
<div align="center">
  <!-- Stability -->
  <img alt="Docker Build State" src="https://github.com/Dog-Face-Development/Periodic-Table-Info/actions/workflows/docker-publish.yml/badge.svg">
  <!-- Stability -->
  <img alt="PyPI Build State" src="https://github.com/Dog-Face-Development/Periodic-Table-Info/actions/workflows/push-to-pypi.yml/badge.svg">
  <!-- Stability -->
  <img alt="Pylint State" src="https://github.com/Dog-Face-Development/Periodic-Table-Info/actions/workflows/pylint.yml/badge.svg">
  <!-- CodeQL -->
  <img alt="CodeQL State" src="https://github.com/Dog-Face-Development/Periodic-Table-Info/actions/workflows/codeql-analysis.yml/badge.svg">
  <!-- Version -->
  <img alt="GitHub Version" src="https://img.shields.io/github/v/release/Dog-Face-Development/Periodic-Table-Info?include_prereleases">
  <!-- Issues -->
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/Dog-Face-Development/Periodic-Table-Info">
  <!-- Pull Requests -->
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/Dog-Face-Development/Periodic-Table-Info">
  <!-- Discord -->
  <img alt="Discord Server ID" src="https://img.shields.io/discord/1015866225827520543">
  <!-- Downloads -->
  <img alt="Downloads" src="https://img.shields.io/github/downloads/Dog-Face-Development/Periodic-Table-Info/total">
  <!-- Language Count -->
  <img alt="GitHub Languages" src="https://img.shields.io/github/languages/count/Dog-Face-Development/Periodic-Table-Info">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#download">Download</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#changelog">Changelog</a> •
  <a href="#credits">Credits & Contributors</a>
</p>

<!-- Screenshot(s) -->
![screenshot](https://github.com/Dog-Face-Development/Periodic-Table-Info/blob/master/docs/images/welcome.png)

## Key Features

* Prints a list of Periodic Table elements.
* Sorts elements by group.
* Offers extended information on each element.
* Cross platform.

## Download

You can **[download](https://github.com/Dog-Face-Development/Periodic-Table-Info/releases/latest) the source code** to run the scripts from the command line on Windows, macOS and Linux. **This will require [Python](https://www.python.org/downloads/).**

You can **[download](https://github.com/Dog-Face-Development/Periodic-Table-Info/releases/latest) the latest executable version** of Periodic Table Info for Windows. **This does not require Python.**

## How To Use

To run the application, you can use [Git and the Python Interpreter](https://github.com/Dog-Face-Development/Periodic-Table-Info/main/README.md#git), which allows you to clone and run the application, [`pip`](https://github.com/Dog-Face-Development/Periodic-Table-Info/main/README.md#pip) to create a command line application, or [Docker](https://github.com/Dog-Face-Development/Periodic-Table-Info/main/README.md#docker) to create a container of the application.

### Git

To clone and run this application, you'll need [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) installed on your computer. If you would rather not use Git, you can just download the script from GitHub above. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/Dog-Face-Development/Periodic-Table-Info

# Go into the repository
$ cd Periodic-Table-Info

# Run the CLI
$ python main.py
```

### `pip`

You can install the program from the [Python Package Index](https://pypi.org/project/Periodic-Table-Info/) through `pip`.

```bash
# Install via pip
$ pip install periodic-table-info

# Run the CLI
$ periodic-table-info
```

### Docker

You can pull the [Docker](https://www.docker.com/) image from GitHub Packages. From your command line:

```bash
# Pull image
$ docker pull ghcr.io/dog-face-development/periodic-table-info:master

# Run container
$ docker run -i -t ghcr.io/dog-face-development/periodic-table-info:master python send.py
```

## Support

More documentation is available in the **[Documentation](https://github.com/Dog-Face-Development/Periodic-Table-Info/tree/master/docs)** and on the **[Wiki](https://github.com/Dog-Face-Development/Periodic-Table-Info/wiki)**. If more support is required, please open a **[GitHub Discussion](https://github.com/Dog-Face-Development/Periodic-Table-Info/discussions)** or join our **[Discord](https://discord.gg/JF2cgABFPw)**.

## Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/Dog-Face-Development/Periodic-Table-Info/compare).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us (including how to sign our CLA).

## Changelog

See the [`CHANGELOG`](CHANGELOG.md) file for details.

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

## Contributors

* [@willtheorangeguy](https://github.com/willtheorangeguy) - Sponsor on [PayPal](https://paypal.me/wvdg44?country.x=CA&locale.x=en_US)

## You may also like...

* [ProgramVer](https://github.com/Dog-Face-Development/ProgramVer) - An open-source, Python GUI version window to show copyright info and licenses.
* [PyWorkout](https://github.com/Dog-Face-Development/PyWorkout) - A minimal CLI to keep you inspired during your workout!
* [PyAvatar](https://github.com/Dog-Face-Development/PyAvatar) - Easily display all of your creative avatars to keep them consistent across websites.

## License

This project is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html) - see the [`LICENSE`](LICENSE.md) file for details. See the [Privacy Policy](https://github.com/Dog-Face-Development/Periodic-Table-Info/blob/master/docs/legal/PRIVACY.md), [Terms and Conditions](https://github.com/Dog-Face-Development/Periodic-Table-Info/blob/master/docs/legal/TERMS.md), and [EULA](https://github.com/Dog-Face-Development/Periodic-Table-Info/blob/master/docs/legal/EULA.md) for legal information.
