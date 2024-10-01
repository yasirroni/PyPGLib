import os

import pytest

import pypglib

"""
pytest -rA -c pyproject.toml --cov-report term-missing --cov=pypglib
pytest -n auto -rA -c pyproject.toml --cov-report term-missing --cov=pypglib
"""


def test_import_contains_data():
    pglib_path = os.path.abspath(os.path.dirname(pypglib.__file__))

    assert os.path.isdir(os.path.join(pglib_path, "opf"))
    assert os.path.isdir(os.path.join(pglib_path, "uc"))
    assert os.path.isdir(os.path.join(pglib_path, "hvdc"))


def test_import_case():
    from pypglib import (
        case5_3_he,
        pglib_opf_case14_ieee,
        pglib_opf_case14_ieee__api,
        pglib_opf_case14_ieee__sad,
    )

    assert pglib_opf_case14_ieee.endswith("pglib_opf_case14_ieee.m")
    assert pglib_opf_case14_ieee__sad.endswith("pglib_opf_case14_ieee__sad.m")
    assert pglib_opf_case14_ieee__api.endswith("pglib_opf_case14_ieee__api.m")
    assert case5_3_he.endswith("case5_3_he.m")

    with pytest.raises(FileNotFoundError):
        from pypglib import case9  # noqa F401


def test_get_case():
    # opf
    assert pypglib.pglib_opf_case14_ieee.endswith("pglib_opf_case14_ieee.m")

    # opf-sad
    assert pypglib.pglib_opf_case14_ieee__sad.endswith("pglib_opf_case14_ieee__sad.m")

    # opf-api
    assert pypglib.pglib_opf_case14_ieee__api.endswith("pglib_opf_case14_ieee__api.m")

    # hvdc
    assert pypglib.case5_3_he.endswith("case5_3_he.m")
