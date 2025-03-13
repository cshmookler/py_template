# **Python Library Template**

A template for modern Python libraries. Uses pytest for unit testing and setuptools for packaging.

This project template includes:

- A prewritten setup.py file for installation with pip.
- Automatic versioning through introspection of the latest [Git](https://git-scm.com/) tag.
    - Set by creating a [Git tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) (the name of the tag is the version).
    - Accessible within the code via the "version" namespace.
    - A placeholder version "0.0.0" is used when there are no Git tags or Git is not installed.
- An prewritten [README.md](https://en.wikipedia.org/wiki/README) file with detailed installation instructions.
- An example sub-project to demo how other programs can use your project (if it's a library).
- A [gitignore](https://github.com/github/gitignore) file for Python.

## Configure this template

##### README.md:

1. Replace the project name with the name of your project.
2. Replace the first section with a description of your project.
3. Completely remove the "Setup" section (do this last if you are still following these instructions).
4. Edit the "Quickstart" section to suite your project.

##### setup.py:

1. Edit the fields in the call to "setup" to suite your project.
2. The list of classifiers is optional and only relevant if you are uploading your project to [PyPI](https://pypi.org/).

##### py_template/:

1. Rename this folder to the name of your project.
2. Within this folder, rename the "hello_world.py" file and edit it to suite your project.

##### tests/:

1. Within this folder, rename the "test_hello_world.py" file and edit it to suite your project.
2. Add more tests to this folder when needed.  All tests must have the "test_" prefix in their name.

## Quickstart

#### 1.&nbsp; Install Python and Git.

##### Windows:

2. [Python](https://python.org/downloads/) (interpreted scripting language)
    - Select the "Add python.exe to PATH" option.
    - Before closing the setup wizard after setup, click the "Disable path length limit" button.
1. [Git](https://git-scm.com/downloads/) (distributed version control)

##### MacOS:

```zsh
brew install python git
```

##### Linux (Arch):

```bash
sudo pacman -S python git
```

#### 2.&nbsp; Clone this project and enter its root directory.

```bash
git clone https://github.com/cshmookler/py_template
cd py_template
```

#### 3.&nbsp; Install this library globally.

```bash
pip install .
```

#### 4.&nbsp; (Optional) Run all tests.

[pytest](https://pypi.org/project/pytest/) must be installed to run tests.

```bash
pytest
```
