# Ouro

<p align="center">
    <img
        width="5%"
        src="https://raw.githubusercontent.com/abdelrahman0w/ouro/main/assets/ouro-icon.svg"
    />
</p>

[![python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://python.org/)
[![ouro](https://img.shields.io/badge/OURO-1e1e1e?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB2ZXJzaW9uPSIxLjIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDEzNiAyNzciIHdpZHRoPSIxMzYiIGhlaWdodD0iMjc3Ij48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9IlAiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIi8%2BPGxpbmVhckdyYWRpZW50IGlkPSJnMSIgeDI9IjEiIGhyZWY9IiNQIiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KC05MS41OTgsNDEuNjM1LC02OC43MzEsLTE1MS4yMDksNzEuNzYsMTY3LjcxNikiPjxzdG9wIHN0b3AtY29sb3I9IiNmZmQ0M2IiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZmU4NzMiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iZzIiIHgyPSIxIiBocmVmPSIjUCIgZ3JhZGllbnRUcmFuc2Zvcm09Im1hdHJpeCgtODYuNDcyLDEyMi4zNDQsLTE1MS41MzYsLTEwNy4xMDUsMjY0LjQzNywxNDYuMzUyKSI%2BPHN0b3Agc3RvcC1jb2xvcj0iIzVhOWZkNCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzMwNjk5OCIvPjwvbGluZWFyR3JhZGllbnQ%2BPC9kZWZzPjxzdHlsZT4uYXtmaWxsOnVybCgjZzEpfS5ie2ZpbGw6dXJsKCNnMil9PC9zdHlsZT48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsYXNzPSJhIiBkPSJtMzMuOCAyNzEuM2MtMjAuMy02LjctMzMuOC0xNC0zMy44LTMzLjN2LTE2Ni42aDI5LjZjMTguMyAwIDMzLjkgMTUuMSAzMy45IDMzLjN2NjYuNmMwIDIyLjIgMTkuMyA0MS42IDQyLjIgNDEuNmgyOS43djI1LjFjMCAxOS4zLTE0LjYgMjguNS0zMy44IDMzLjMtMjYuOCA2LjctNDYuOSA2LjktNjcuOCAwem0xMC43LTE2OWMwLTYuOS01LjctMTIuNS0xMi43LTEyLjUtNy4xIDAtMTIuOCA1LjYtMTIuOCAxMi41IDAgNi45IDUuNyAxMi41IDEyLjggMTIuNSA3IDAgMTIuNy01LjYgMTIuNy0xMi41eiIvPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xhc3M9ImIiIGQ9Im0xMDEuNSA1LjFjMjAuMyA2LjcgMzMuOSAxNCAzMy45IDMzLjN2MTY2LjZoLTI5LjdjLTE4LjIgMC0zMy44LTE1LjEtMzMuOC0zMy4zdi02Ni42YzAtMjIuMi0xOS4zLTQxLjYtNDIuMy00MS42aC0yOS42di0yNS4xYzAtMTkuNCAxNC41LTI4LjUgMzMuOC0zMy4zIDI2LjgtNi43IDQ2LjktNi45IDY3LjcgMHptMTQuOCAxNjljMC02LjktNS43LTEyLjUtMTIuNy0xMi41LTcgMC0xMi43IDUuNi0xMi43IDEyLjUgMCA2LjkgNS43IDEyLjUgMTIuNyAxMi41IDcgMCAxMi43LTUuNiAxMi43LTEyLjV6Ii8%2BPC9zdmc%2B)](https://github.com/abdelrahman0w/ouro)
[![tox](https://github.com/abdelrahman0w/ouro/actions/workflows/tox.yml/badge.svg)](https://github.com/abdelrahman0w/ouro/actions/workflows/tox.yml)
[![pre-commit](https://github.com/abdelrahman0w/ouro/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/abdelrahman0w/ouro/actions/workflows/pre-commit.yml)

- [Ouro](#ouro)
  - [Description](#description)
  - [Name Origin](#name-origin)
  - [Demo](#demo)
  - [Installation](#installation)
    - [Using PIP](#using-pip)
    - [Using Poetry](#using-poetry)
    - [From Source](#from-source)
  - [Usage](#usage)
    - [Using the CLI tool](#using-the-cli-tool)
      - [Basic Usage](#basic-usage)
      - [Entry Point](#entry-point)
      - [Available Options](#available-options)
    - [As a pre-commit hook](#as-a-pre-commit-hook)
  - [Features](#features)

## Description

OURO ([**OURO**boros](https://en.wikipedia.org/wiki/Ouroboros)) is a [Python](https://www.python.org/) package that checks your code for circular (cyclic) imports.

> Currently, ouro only supports [absolute imports](https://docs.python.org/3/reference/import.html#package-relative-imports)

## Name Origin

The name **"ouro"** is derived from the term [**"ouroboros"**](https://en.wikipedia.org/wiki/Ouroboros), a symbol from ancient mythology depicting a snake consuming its own tail, representing the concept of infinity and cyclicality. This name was chosen for its apt metaphorical representation of the package's functionality. Just as the ouroboros symbolizes a cycle, the "ouro" package checks for circular imports in Python. The connection to Python, a language named after a type of snake, further reinforces this symbolic link.

## Demo

![OURO](https://raw.githubusercontent.com/abdelrahman0w/ouro/main/assets/ouro-demo.gif)

## Installation

You can install ouro in multiple ways, as follows.

### Using PIP

```shell
pip install ouro
```

### Using Poetry

```shell
poetry add ouro
```

### From Source

1. Clone [this repo](https://github.com/abdelrahman0w/ouro)

    ```shell
    git clone https://github.com/abdelrahman0w/ouro
    ```

    > Or you can download it as a zip file
1. Naviage to the repo directory

    ```shell
    cd ouro
    ```

1. Once you have a copy of the source, you can install it as follows:

    - Using `make`

        ```shell
        make install
        ```
    - Using `pip`

        ```shell
        pip install .
        ```
    - Or directly from the `setup.py` file

        ```shell
        python setup.py install
        ```

## Usage

### Using the CLI tool

#### Basic Usage

1. Navigage to your project

    ```shell
    cd path/to/your/project
    ```
1. Run `ouro`

    ```shell
    ouro
    ```

#### Entry Point

```shell
ouro [-h] [-v] [--verbose] [--no-categorize] [-e] [-i IGNORE [IGNORE ...]] [path]
```

#### Available Options

```
<path>             path to the Python project to be checked (default: current working directory)

-h, --help         show this help message and exit
-v, --version      show version number and exit
--verbose          increase output verbosity (print report to console)
--no-categorize    don't categorize cycles (mark all cycles as critical)
-e, --export       export the report to a json file
-i. --ignore       list of files, directories, or glob patterns to ignore
```

### As a pre-commit hook

> Check [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

- Sample usage in `.pre-commit-config.yaml` file:

    Add ouro to repos as follows:

    ```yaml
    - repo: https://github.com/abdelrahman0w/ouro
        rev: v0.1.1
        hooks:
        - id: ouro
    ```

## Features

> Current features are checked

- [X] CLI tool for checking circular imports in a Python code
- [X] Get the context of the import to ignore imports within a function scope
- [X] Ignore `.git` dir in case of git repo
- [X] Ignore paths and patterns in `.gitignore` file
- [X] Ability to ignore a file name, directory name, or a glob pattern
- [X] Show imports in context with file name and line number
- [X] Support for absolute imports
- [ ] Support for relative imports
