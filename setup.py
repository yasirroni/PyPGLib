import os

from setuptools import setup


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
    package_data={
        "": extra_files,
    }
)
