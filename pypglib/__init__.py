import os

PATH_PYPGLIB = os.path.dirname(os.path.abspath(__file__))


__version__ = "0.0.3"


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
