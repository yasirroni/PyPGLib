import os
import re

PATH_PYPGLIB = os.path.dirname(os.path.abspath(__file__))
PATH_PYPGLIB_HVDC = os.path.join(PATH_PYPGLIB, "hvdc")
PATH_PYPGLIB_OPF = os.path.join(PATH_PYPGLIB, "opf")
PATH_PYPGLIB_UC = os.path.join(PATH_PYPGLIB, "uc")

__version__ = "0.0.3"

with open(
    os.path.join(PATH_PYPGLIB_HVDC, "CHANGELOG.md"), "rt", encoding="utf-8"
) as file:
    version_line = file.read()
    m = re.search(r"^### v([0-9.]+)", version_line, re.M)
    __VERSION_PYPGLIB_HVDC__ = m.group(1)

with open(
    os.path.join(PATH_PYPGLIB_OPF, "CHANGELOG.md"), "rt", encoding="utf-8"
) as file:
    version_line = file.read()
    m = re.search(r"^### v([0-9.]+)", version_line, re.M)
    __VERSION_PYPGLIB_OPF__ = m.group(1)

with open(
    os.path.join(PATH_PYPGLIB_UC, "CHANGELOG.md"), "rt", encoding="utf-8"
) as file:
    version_line = file.read()
    m = re.search(r"^### v([0-9.]+)", version_line, re.M)
    __VERSION_PYPGLIB_UC__ = m.group(1)


def __getattr__(filename):
    """Automatically creates a string to case path."""

    # replace extension
    root, _ = os.path.splitext(filename)
    filename = root + ".m"

    for root, _, files in os.walk(PATH_PYPGLIB):
        for name in files:
            if name == filename:
                return os.path.join(root, name)

    msg = f"No file with name {filename}!"
    raise FileNotFoundError(msg)
