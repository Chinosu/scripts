import sys
sys.path.append('/Users/megan/Code/scripts')
from hypertest import parameters, test, hypertest

hypertest(
    name='My test',
    parameters=parameters(
        max_cpu=30,
        files='target.c',
        program='target'
    ),
    tests=[
        test(command='./target', expected_stdout=r'args\n./target\n')
    ]
)
