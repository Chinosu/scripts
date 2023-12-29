from sys import argv
from abc import ABC, abstractmethod
from subprocess import run

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
            '/usr/local/share/autotest/autotest.py',
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
        return 'now fly [command]'
    
    def run(self):
        run(['make'])
        if len(argv) > 2:
            try:
                command = argv[2::]
                run(command)
            except:
                pass

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