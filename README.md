# Ouro

[![OURO](https://img.shields.io/badge/OURO-1e1e1e?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB2ZXJzaW9uPSIxLjIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDEzNiAyNzciIHdpZHRoPSIxMzYiIGhlaWdodD0iMjc3Ij48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9IlAiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIi8%2BPGxpbmVhckdyYWRpZW50IGlkPSJnMSIgeDI9IjEiIGhyZWY9IiNQIiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KC05MS41OTgsNDEuNjM1LC02OC43MzEsLTE1MS4yMDksNzEuNzYsMTY3LjcxNikiPjxzdG9wIHN0b3AtY29sb3I9IiNmZmQ0M2IiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZmU4NzMiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iZzIiIHgyPSIxIiBocmVmPSIjUCIgZ3JhZGllbnRUcmFuc2Zvcm09Im1hdHJpeCgtODYuNDcyLDEyMi4zNDQsLTE1MS41MzYsLTEwNy4xMDUsMjY0LjQzNywxNDYuMzUyKSI%2BPHN0b3Agc3RvcC1jb2xvcj0iIzVhOWZkNCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzMwNjk5OCIvPjwvbGluZWFyR3JhZGllbnQ%2BPC9kZWZzPjxzdHlsZT4uYXtmaWxsOnVybCgjZzEpfS5ie2ZpbGw6dXJsKCNnMil9PC9zdHlsZT48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsYXNzPSJhIiBkPSJtMzMuOCAyNzEuM2MtMjAuMy02LjctMzMuOC0xNC0zMy44LTMzLjN2LTE2Ni42aDI5LjZjMTguMyAwIDMzLjkgMTUuMSAzMy45IDMzLjN2NjYuNmMwIDIyLjIgMTkuMyA0MS42IDQyLjIgNDEuNmgyOS43djI1LjFjMCAxOS4zLTE0LjYgMjguNS0zMy44IDMzLjMtMjYuOCA2LjctNDYuOSA2LjktNjcuOCAwem0xMC43LTE2OWMwLTYuOS01LjctMTIuNS0xMi43LTEyLjUtNy4xIDAtMTIuOCA1LjYtMTIuOCAxMi41IDAgNi45IDUuNyAxMi41IDEyLjggMTIuNSA3IDAgMTIuNy01LjYgMTIuNy0xMi41eiIvPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xhc3M9ImIiIGQ9Im0xMDEuNSA1LjFjMjAuMyA2LjcgMzMuOSAxNCAzMy45IDMzLjN2MTY2LjZoLTI5LjdjLTE4LjIgMC0zMy44LTE1LjEtMzMuOC0zMy4zdi02Ni42YzAtMjIuMi0xOS4zLTQxLjYtNDIuMy00MS42aC0yOS42di0yNS4xYzAtMTkuNCAxNC41LTI4LjUgMzMuOC0zMy4zIDI2LjgtNi43IDQ2LjktNi45IDY3LjcgMHptMTQuOCAxNjljMC02LjktNS43LTEyLjUtMTIuNy0xMi41LTcgMC0xMi43IDUuNi0xMi43IDEyLjUgMCA2LjkgNS43IDEyLjUgMTIuNyAxMi41IDcgMCAxMi43LTUuNiAxMi43LTEyLjV6Ii8%2BPC9zdmc%2B)](https://github.com/abdelrahman0w/ouro)
[![tox](https://github.com/abdelrahman0w/ouro/actions/workflows/tox.yml/badge.svg)](https://github.com/abdelrahman0w/ouro/actions/workflows/tox.yml)
[![pre-commit](https://github.com/abdelrahman0w/ouro/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/abdelrahman0w/ouro/actions/workflows/pre-commit.yml)

## Description

OURO ([**OURO**boros](https://en.wikipedia.org/wiki/Ouroboros)) is a [Python](https://www.python.org/) library that checks your code for circular (cyclic) imports.

> Currently, ouro only supports [absolute imports](https://docs.python.org/3/reference/import.html#package-relative-imports)

## Demo

[![OURO](https://img.shields.io/badge/OURO-1e1e1e?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB2ZXJzaW9uPSIxLjIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDEzNiAyNzciIHdpZHRoPSIxMzYiIGhlaWdodD0iMjc3Ij48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9IlAiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIi8%2BPGxpbmVhckdyYWRpZW50IGlkPSJnMSIgeDI9IjEiIGhyZWY9IiNQIiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KC05MS41OTgsNDEuNjM1LC02OC43MzEsLTE1MS4yMDksNzEuNzYsMTY3LjcxNikiPjxzdG9wIHN0b3AtY29sb3I9IiNmZmQ0M2IiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZmU4NzMiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iZzIiIHgyPSIxIiBocmVmPSIjUCIgZ3JhZGllbnRUcmFuc2Zvcm09Im1hdHJpeCgtODYuNDcyLDEyMi4zNDQsLTE1MS41MzYsLTEwNy4xMDUsMjY0LjQzNywxNDYuMzUyKSI%2BPHN0b3Agc3RvcC1jb2xvcj0iIzVhOWZkNCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzMwNjk5OCIvPjwvbGluZWFyR3JhZGllbnQ%2BPC9kZWZzPjxzdHlsZT4uYXtmaWxsOnVybCgjZzEpfS5ie2ZpbGw6dXJsKCNnMil9PC9zdHlsZT48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsYXNzPSJhIiBkPSJtMzMuOCAyNzEuM2MtMjAuMy02LjctMzMuOC0xNC0zMy44LTMzLjN2LTE2Ni42aDI5LjZjMTguMyAwIDMzLjkgMTUuMSAzMy45IDMzLjN2NjYuNmMwIDIyLjIgMTkuMyA0MS42IDQyLjIgNDEuNmgyOS43djI1LjFjMCAxOS4zLTE0LjYgMjguNS0zMy44IDMzLjMtMjYuOCA2LjctNDYuOSA2LjktNjcuOCAwem0xMC43LTE2OWMwLTYuOS01LjctMTIuNS0xMi43LTEyLjUtNy4xIDAtMTIuOCA1LjYtMTIuOCAxMi41IDAgNi45IDUuNyAxMi41IDEyLjggMTIuNSA3IDAgMTIuNy01LjYgMTIuNy0xMi41eiIvPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xhc3M9ImIiIGQ9Im0xMDEuNSA1LjFjMjAuMyA2LjcgMzMuOSAxNCAzMy45IDMzLjN2MTY2LjZoLTI5LjdjLTE4LjIgMC0zMy44LTE1LjEtMzMuOC0zMy4zdi02Ni42YzAtMjIuMi0xOS4zLTQxLjYtNDIuMy00MS42aC0yOS42di0yNS4xYzAtMTkuNCAxNC41LTI4LjUgMzMuOC0zMy4zIDI2LjgtNi43IDQ2LjktNi45IDY3LjcgMHptMTQuOCAxNjljMC02LjktNS43LTEyLjUtMTIuNy0xMi41LTcgMC0xMi43IDUuNi0xMi43IDEyLjUgMCA2LjkgNS43IDEyLjUgMTIuNyAxMi41IDcgMCAxMi43LTUuNiAxMi43LTEyLjV6Ii8%2BPC9zdmc%2B)](https://github.com/abdelrahman0w/ouro)

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

1. Once you have a copy of the source, you can install it with:

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

### Basic Usage

1. Navigage to your project

    ```shell
    cd path/to/your/project
    ```
1. Run `ouro`

    ```shell
    ouro
    ```

### Available Options

TO BE ADDED

### As a pre-commit hook

> Check [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

- Sample usage in `.pre-commit-config.yaml` file:

    Add ouro to repos as follows:

    ```yaml
    - repo: https://github.com/abdelrahman0w/ouro
        rev: v0.1.0
        hooks:
        - id: ouro
    ```

## Features

- [ ] CLI tool for checking circular imports in a python code
- [ ] Gets the context of the import to ignore imports within a function scope
- [ ] Ignores `.git` dir in case of git repo
- [ ] Ignores paths in `.gitignore` file
- [ ] Ability to ignore a file name, directory name, or a regex pattern
- [ ] Show imports in context with file name and line number
- [ ] Supports for absolute imports
- [ ] Supports for relative imports
