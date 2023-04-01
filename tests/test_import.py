import os


'''
pytest -rA -c pyproject.toml --cov-report term-missing --cov=pglib
pytest -n auto -rA -c pyproject.toml --cov-report term-missing --cov=pglib
'''

def test_import_contains_data():
    import pglib


    print(pglib.__file__)
    pglib_path = os.path.abspath(os.path.dirname(pglib.__file__))

    assert os.path.isdir(os.path.join(pglib_path, "opf"))
    assert os.path.isdir(os.path.join(pglib_path, "uc"))
    assert os.path.isdir(os.path.join(pglib_path, "hvdc"))
