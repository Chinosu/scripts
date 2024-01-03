import os
from pathlib import Path
import shutil
import sys
from paths import autotest_path
import subprocess


if __name__ == '__main__':
    print('Import this file as a module to use it.')

def parameters(
    max_cpu=None,
    files=None,
    program=None
):
    return [f'{param}={value}' for param, value in locals().items() if value is not None]

def test(
    name=None,
    command=None,
    expected_stdout=None,
    expected_stderr=None
): 
    return name, ' '.join([f'{param}={value}' for param, value in locals().items() if value is not None and param != 'name'])

def hypertest(
    name,
    parameters,
    tests
):
    dir_name = Path(f'autotest_{name}')
    file_name = 'tests.txt'
    name_i = -1
    
    def removable(path):
        files = os.listdir(path)
        return len(files) == 1 and files[0] == file_name
    
    def auto_name():
        nonlocal name_i
        name_i += 1
        return name_i
    
    if dir_name.exists():
        if not removable(dir_name):
            print(f'Error: directory {dir_name} already exists', file=sys.stderr)
            return
        shutil.rmtree(dir_name)
        
    os.makedirs(dir_name)
        
    with open(dir_name / file_name, 'w') as file:
        file.writelines(parameters)
        file.write('\n')
        file.writelines([f'{name if name is not None else auto_name()} {line}' for name, line in tests])
        file.write('\n')
    
    subprocess.run(['python3', '-I', autotest_path(), '-E', '.', '-e', dir_name]);