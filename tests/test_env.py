#!/usr/bin/env python
from ouroboros import __version__


def test_absolute_import():
    assert __version__ is not None
