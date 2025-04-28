import os

from tests.test import Test


this_dir: str = os.path.dirname(__file__)

test = Test(this_dir)

test.copy("template_config.ini")
test.run("config", "config.py")
test.call("venv", ["python", "-m", "venv", ".venv"])
test.call("pip_pytest", [".venv/bin/pip", "install", "pytest"])
test.call("pip_project", [".venv/bin/pip", "install", "."])
test.call("pytest", [".venv/bin/pytest"])
