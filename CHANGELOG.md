# Changelog

## 0.1.2 (2024-01-31)

### Features

### Fixed

- bug fixes

### Changed

### Removed

## 0.1.1 (2024-01-29)

### Features

### Fixed

- pre-commit hook
- bug in possible origins func

### Changed

### Removed

## 0.1.0 (2024-01-27)

### Features

- CLI tool for checking circular imports in a python package
    > Currently, supports [absolute imports](https://docs.python.org/3/reference/import.html#package-relative-imports) only
- Gets the context of the import to ignore imports within a function scope
- Ignores `.git` dir in case of git repo
- Ignores paths in `.gitignore` file
- Ability to ignore a file name, directory name, or a glob pattern

### Fixed

### Changed

### Removed
