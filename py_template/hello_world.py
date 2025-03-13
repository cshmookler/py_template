"""An example module for the Python library template"""


def hello_world(sep: str = " ") -> str:
    """
    Generates a hello world string.

    Args:
        sep (str): The separator to use instead of a space.

    Returns:
        str: The generated hello world string.
    """

    return f"Hello{sep}World!"
