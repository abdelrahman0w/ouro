# Changelog

## 0.2.0 (2024-02-13)

### Features

- Enhance performance by around %60

## 0.1.3 (2024-01-31)

### Fixed

- add missing instsll requirements

## 0.1.2 (2024-01-31)

### Fixed

- bug fixes

## 0.1.1 (2024-01-29)

### Fixed

- pre-commit hook
- bug in possible origins func

## 0.1.0 (2024-01-27)

### Features

- CLI tool for checking circular imports in a python package
    > Currently, supports [absolute imports](https://docs.python.org/3/reference/import.html#package-relative-imports) only
- Gets the context of the import to ignore imports within a function scope
- Ignores `.git` dir in case of git repo
- Ignores paths in `.gitignore` file
- Ability to ignore a file name, directory name, or a glob pattern
