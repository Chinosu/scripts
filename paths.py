from pathlib import Path


def autotest_path():
    return Path(__file__).resolve().parent / 'submodules' / 'autotest' / 'autotest.py'

def hypertest_module_path():
    return Path(__file__).resolve().parent
