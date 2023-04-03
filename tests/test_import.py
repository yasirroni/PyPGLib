import os


'''
pytest -rA -c pyproject.toml --cov-report term-missing --cov=pypglib
pytest -n auto -rA -c pyproject.toml --cov-report term-missing --cov=pypglib
'''

def test_import_contains_data():
    import pypglib


    print(pypglib.__file__)
    pglib_path = os.path.abspath(os.path.dirname(pypglib.__file__))

    assert os.path.isdir(os.path.join(pglib_path, "opf"))
    assert os.path.isdir(os.path.join(pglib_path, "uc"))
    assert os.path.isdir(os.path.join(pglib_path, "hvdc"))
