import subprocess

from setuptools import setup


# The version to use if there aren't any Git tags or Git is not installed.
placeholder_version: str = "0.0.0"


def get_version_from_git() -> str:
    """Attempts to retrieve the project version from Git.

    Returns:
        str: The project version from Git or a placeholder version if Git is not installed or there aren't any tags.
    """

    result = subprocess.run(["git", "describe", "--tags"], capture_output=True)

    if result.returncode != 0:
        # Failed to get the latest tag from Git.  Use the placeholder version.
        return placeholder_version

    return result.stdout.decode().partition("-")[0]


# https://python-packaging.readthedocs.io/en/latest/


setup(
    name="py_template",
    url="https://github.com/cshmookler/py_template",
    version=get_version_from_git(),
    author="Caden Shmookler",
    author_email="cshmookler@gmail.com",
    description="A modern template for Python libraries",
    packages=["py_template"],
    install_requires=["pytest"],
    classifiers=[  # The full list of classifiers is at https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
)
