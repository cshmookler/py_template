"""Configure this template project"""

import json
import os
import shutil
import stat
import subprocess
import time
from ast import literal_eval
from configparser import ConfigParser
from dataclasses import dataclass
from importlib import import_module
from os import listdir, remove, rename
from os.path import dirname, join
from typing import Callable, Dict, KeysView, List, Union


this_dir: str = dirname(__file__)


def valid_identifier_name(name: str) -> bool:
    """Verify that a given string is a valid Python identifier name."""

    # At least one character and starts with a letter.
    if len(name) == 0 or not name[0].isalpha():
        return False
    # All characters are either a letter, number, or underscore.
    for c in name:
        if not c.isalnum() and c != "_":
            return False
    return True


def valid_list(list_str: str) -> bool:
    """Verify that a given string represents a valid Python list."""

    try:
        if type(literal_eval(list_str)) != list:
            return False
    except SyntaxError:
        return False
    return True


def optional(_: str) -> bool:
    """Return True regardless of the given string value."""

    return True


def required(given_str: str) -> bool:
    """Verify that a given string is not empty."""

    return given_str != "" and given_str is not None


@dataclass
class ConfigInfo:
    """Information relating to a specific configuration."""

    default: str = ""
    constraint: Callable[[str], bool] = required


def assert_none_missing(
    expected: Union[List[str], KeysView[str]],
    parsed: Union[List[str], KeysView[str]],
    classification: str,
) -> None:
    """Ensure that all items in the expected list are in the parsed list."""

    missing_sections: List[str] = [k for k in expected if k not in parsed]
    if len(missing_sections) <= 0:
        return
    print("Error: The following " + classification + " were not found:")
    for k in missing_sections:
        print(k + " ", end="")
    print(end="\n")
    exit(1)


def get_config() -> Dict[str, str]:
    """Retrieve configuration information"""

    ini_file: str = join(this_dir, "template_config.ini")
    section_name: str = "template_config"
    expected_configs: Dict[str, ConfigInfo] = {
        "project_name": ConfigInfo(default="example", constraint=valid_identifier_name),
        "description": ConfigInfo(default=""),
        "project_type": ConfigInfo(
            default="application",
            constraint=lambda s: s
            in [
                "application",
                "library",
            ],
        ),
        "author": ConfigInfo(default=""),
        "email": ConfigInfo(default=""),
        "website_url": ConfigInfo(default=""),
        "git_url": ConfigInfo(default=""),
        "license": ConfigInfo(default=""),
        "dependencies": ConfigInfo(default="[]", constraint=valid_list),
        "classifiers": ConfigInfo(default="[]", constraint=valid_list),
        "current_year": ConfigInfo(default=str(time.localtime().tm_year)),
    }

    # Read the configuration file.
    parser = ConfigParser()
    parser.read(ini_file)
    assert_none_missing([section_name], parser.sections(), "sections")
    parsed_configs = parser[section_name]

    # Verify that the given values meet their cooresponding constraints.
    configs: Dict[str, str] = {}
    for key, value in expected_configs.items():
        try:
            parsed_value: str = parsed_configs[key]
        except KeyError:
            parsed_value = value.default

        if not value.constraint(parsed_value):
            configs[key] = value.default
            raise RuntimeError(
                "Invalid option '" + parsed_value + "' for '" + key + "'."
            )

        configs[key] = parsed_value

    return configs


def shutil_onerror(func, path, exc_info) -> None:
    """On access error, add write permissions and try again"""

    if os.access(path, os.W_OK):
        raise
    os.chmod(path, stat.S_IWUSR)
    func(path)


def configure() -> None:
    """Configure this template project"""

    config = get_config()

    # Remove unnecessary files.
    shutil.rmtree(join(this_dir, ".git"), onerror=shutil_onerror)
    shutil.rmtree(join(this_dir, "tests"))
    remove(join(this_dir, ".gitignore"))
    remove(join(this_dir, ".gitattributes"))
    remove(join(this_dir, "LICENSE"))
    remove(join(this_dir, "README.md"))

    # Create a fresh git repository.
    subprocess.run(["git", "init", "--initial-branch", "main", this_dir], check=True)

    # Unpack template files.
    for file in listdir(join(this_dir, "template_files")):
        shutil.move(join(this_dir, "template_files", file), join(this_dir, file))
    shutil.rmtree(join(this_dir, "template_files"))

    # Rename the source directory.
    shutil.move(
        join(this_dir, "{{project_name}}"), join(this_dir, config["project_name"])
    )

    # Create the virtual environment.
    venv = import_module("this_venv")
    venv.create()
    subprocess.run([venv.pip(), "install", "jinja2"], check=True)

    # Configure templates.
    subprocess.run(
        [
            venv.python(),
            join(this_dir, "configure_templates.py"),
            json.dumps(config),
        ],
        check=True,
    )

    # Remove this configuration script, the templater script, and the cooresponding .ini file once project configuration is complete.
    remove(join(this_dir, "this_venv.py"))
    remove(join(this_dir, "config.py"))
    remove(join(this_dir, "configure_templates.py"))
    remove(join(this_dir, "template_config.ini"))

    # Remove the virtual environment and pre-compiled Python bytecode
    shutil.rmtree(join(this_dir, venv.name))
    shutil.rmtree(join(this_dir, "__pycache__"))


if __name__ == "__main__":
    configure()
