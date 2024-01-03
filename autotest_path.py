from pathlib import Path


def autotest_path():
    return Path(__file__).resolve().parent / 'submodules' / 'autotest' / 'autotest.py'
