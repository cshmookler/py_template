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

## Setup

#### 1.&nbsp; Install Python and Git.

##### Windows:

1. [Python](https://python.org/downloads/) (interpreted scripting language)
    - Select the "Add python.exe to PATH" option.
    - Before closing the setup wizard after setup, click the "Disable path length limit" button.
2. [Git](https://git-scm.com/downloads/) (distributed version control)

##### MacOS:

Install [Homebrew](https://brew.sh/) (package manager for Mac) by opening a terminal and entering the following command:

```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Use Homebrew to install Git, Python, and GCC (C++ compiler):

```zsh
brew install python git
```

##### Linux (Arch):

```bash
sudo pacman -S python git
```

#### 2.&nbsp; Clone this template and enter its root directory.

Open command prompt (Windows) or a shell (Linux & Mac) and enter the commands below. The template will be downloaded to the current working directory.

```bash
git clone https://github.com/cshmookler/py_template.git
cd py_template
```

#### 3.&nbsp; Edit "template_config.ini" to suit your project

Any text editor (Notepad, TextEdit, Nano, Vim, etc.) can be used as long as the file name and format are not changed.

##### Windows:

```shell
notepad template_config.ini
```

##### Mac:

```zsh
open -t template_config.ini
```

##### Linux:

```bash
nano template_config.ini
```

#### 4.&nbsp; Configure this template

Use Python to execute the "config.py" script. Use command prompt (Windows) or a shell (Mac & Linux) so errors are shown.

```
python config.py
```

If errors occur, troubleshoot to isolate the issue and repeat steps 2-4.

If the script successfully completes without errors, re-open this README file. A new README for your project will have been generated in its place.
