# **Python Library Template**

A template for modern Python libraries. Uses pytest for unit testing and setuptools for packaging.

This project template includes:

- An example package and test that follow [Google's style guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) for documenting modules.
- A setup.py file for installation with pip.
- Automatic versioning through introspection of the latest [Git](https://git-scm.com/) tag.
    - Set by creating a [Git tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) (the name of the tag is the version).
    - Accessible within the code via the "version" namespace.
    - A placeholder version "0.0.0" is used when there are no Git tags or Git is not installed.
- Prewritten [README.md](https://en.wikipedia.org/wiki/README), [CONTRIBUTING.md](https://github.blog/news-insights/the-library/contributing-guidelines/),  and [gitignore](https://github.com/github/gitignore) files.

## Configure this template

Configurable fields are labelled with "TODO" tags.  Delete each TODO tag and configure each field that they refer to.  Use Ctrl-F "TODO" in each file to find these tags.

The following files contain TODO tags for fields that need to be configured:
- setup.py
- README.md

Once all TODO tags have been removed:
- Rename the 'example' directory to the name of your package.
    - Make sure the 'packages' field in setup.py matches the name of this directory.
    - Any importable (functions or classes) that are imported in the '\_\_init\_\_.py' file will be made top-level importables in the package.
- Delete the LICENSE file and replace it with your own license.
    - (Optional) Add a 'license' field to the setup() call in setup.py.
- Delete the '.git' directory and [initialize a new Git repository](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
    - NOTE: Declare versions by creating [Git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) (you need at least one commit in the Git repository to create a tag).

Finally, delete these instructions from the README.





# TODO: SET THE PROJECT NAME
# **Example**

# TODO: Write the project description
Write a description of your project here.

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

# TODO: SET THE GIT LINK AND PROJECT NAME
```bash
git clone https://gitlab.com/user/proj_name.git
cd proj_name
```

#### 3.&nbsp; Install this library globally.

```bash
pip install .
```

#### 4.&nbsp; (Optional) Run all tests.

```bash
pytest
```
