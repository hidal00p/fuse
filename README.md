# `fuse`
A dead simple script that merges a set of your PDF documents into one.
Based on https://pypdf.readthedocs.io/en/stable/index.html

### Setup
This project may easily be setup using any of the available python
methods, e.g.:

* global python and pip
* `venv` and pip
* `poetry`

The following explanation is for the setup with `poetry` only:

* Install [`poetry`](https://python-poetry.org/docs/#installation) globally.
* Make sure that your system has python `>=3.9`. If no install it, e.g. using [pyenv](https://github.com/pyenv/pyenv) or manually.
* Clone this repo with `git clone https://github.com/hidal00p/fuse.git`.
* Navigate to the cloned directory `cd fuse`.
* Tell `poetry` to create an environment based on python version `>=3.9` with `poetry env use <path to the desired python executable>`.
* Install dependencies `poetry env install`.

### Usage
The program takes in files to be merged, and fuses them into an output file
in the order provided:

```
poetry run python -m fuse.main --f 1.pdf 2.pdf ... n.pdf --o merged.pdf
```

To query for help run:

```
poetry run python -m fuse.main --help
```

**HINT:** To make this program available from anywhere in your system,
add the following to your shell configuration file, e.g. `.zshrc` or `.bashrc`:

```
alias fusepdf=poetry run --directory <path to the cloned directory> python -m fuse.main
```

Happy fusing 📚
