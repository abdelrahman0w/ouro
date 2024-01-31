#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup


with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as changelog_file:
    changelog = changelog_file.read()

requirements = [
    "pathspec>=0.12.1",
]
test_requirements = [
    "pytest>=3",
]


description = """
ouro is a Python package that checks your code for circular (cyclic) imports.
"""


setup(
    author="Abdelrahman Abdelkhalek",
    author_email="abdelrahman.abdelkhalek@thndr.app",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
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
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=[
        "python",
        "ouro",
        "circular",
        "dependency",
        "cycle",
        "cyclic",
        "import",
        "imports",
    ],
    name="ouro",
    packages=find_packages(include=["ouro", "ouro.*"]),
    entry_points={
        "console_scripts": [
            "ouro = ouro.__main__:main",
        ]
    },
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/abdelrahman0w/ouro",
    version="0.1.3",
    zip_safe=False,
)
