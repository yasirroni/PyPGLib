import os
import re

from setuptools import setup

PACKAGE_NAME = "pypglib"
current_path = os.path.abspath(os.path.dirname(__file__))
version_line = open(
    os.path.join(current_path, PACKAGE_NAME, "__init__.py"), "rt"
).read()

m = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)
__version__ = m.group(1)


def package_files(directory_list):
    paths = []
    for directory in directory_list:
        for path, _, filenames in os.walk(directory):
            for filename in filenames:
                paths.append(os.path.join("..", path, filename))
    return paths


extra_files = package_files(
    [
        "pypglib/hvdc",
        "pypglib/opf",
        "pypglib/uc",
    ]
)

setup(
    version=__version__,
    package_data={
        "": extra_files,
    },
)
