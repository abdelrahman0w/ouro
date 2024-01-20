#!/usr/bin/env python
"""The setup script."""
from setuptools import find_packages
from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as changelog_file:
    changelog = changelog_file.read()

description = """OUROBOROS"""

requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="Abdelrahman Abdelkhalek",
    author_email="abdelrahman.abdelkhalek@thndr.app",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description=description,
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + changelog,
    include_package_data=True,
    keywords=[
        "ouroboros",
        "circular",
        "dependency",
        "cycle",
        "cyclic",
        "import",
        "imports",
    ],
    name="ouroboros",
    packages=find_packages(include=["ouroboros", "ouroboros.*"]),
    entry_points={
        "console_scripts": [
            "ouroboros = ouroboros.__main__:main",
        ]
    },
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/abdelrahman0w/ouroboros",
    version="0.1.0",
    zip_safe=False,
)
