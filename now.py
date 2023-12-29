from sys import argv
from abc import ABC, abstractmethod
from subprocess import run
from pathlib import Path
import os

def main():
    try:
        module = Modules.match(argv[1])
        module.run()
    except:
        print_usage()

def print_usage():
    print('=x= Usage =x=')
    print()
    for usage in Modules.usages():
        print(usage)
    print()
    print('=x=       =x=')

class Module(ABC):
    @staticmethod
    @abstractmethod
    def get_name(): pass

    @staticmethod
    @abstractmethod
    def get_usage(): pass

    @abstractmethod
    def run(self): pass

class TestModule(ABC):
    @staticmethod
    def get_name():
        return 'test'
    
    @staticmethod
    def get_usage():
        return 'now test [folder]'
    
    def run(self):
        folder = argv[2]
        command = [
            'python3', '-I',
            'autotest/autotest.py',
            '-E', '.',
            '-e', folder
        ]
        run(command)

class FlyModule(ABC):
    @staticmethod
    def get_name():
        return 'fly'
    
    @staticmethod
    def get_usage():
        return 'now fly [command]?'
    
    def run(self):
        run(['make'])
        try:
            if len(argv) > 2:
                command = argv[2::]
                command[0] = './' + command[0]
            else:
                command = './' + self.latest_executable_path_in_directory('.')
            run(command);
        except Exception as e:
            print(e)

    def latest_executable_path_in_directory(self, directory):
        directory = Path(directory)

        latest_executable_path = None
        latest_mod_time = 0

        for filename in os.listdir(directory):
            path = directory / filename
            if not path.is_file() or not os.access(path, os.X_OK): continue
            mod_time = os.path.getmtime(path)
            if mod_time > latest_mod_time:
                latest_executable_path = path
                latest_mod_time = mod_time
        
        return str(latest_executable_path)

class Modules:
    items = [TestModule, FlyModule]

    @staticmethod
    def match(name):
        for module in Modules.items:
            if module.get_name() == name:
                return module()
        raise KeyError(name)

    @staticmethod
    def usages():
        return [module.get_usage() for module in Modules.items]

if __name__ == '__main__':
    main()