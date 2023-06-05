import os
from random import randint


try:
    os.mkdir('tests')
except FileExistsError:
    pass


start = 1
end = 100
for i in range(start, end + 1):
    A = randint(1, int(1e9))
    B = randint(1, int(1e9))
    with open(f'tests/{i:04}.in', 'w') as f:
        # input here
        f.write(f'{A} {B}')
    with open(f'tests/{i:04}.out', 'w') as f:
        # output here
        f.write(f'{A + B}')
