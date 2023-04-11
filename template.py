import os
from random import randint


os.mkdir('tests')

start = 1
end = 100
for i in range(start, end + 1):
    n = randint(1, 1000)
    with open(f'tests/{i:04}.in', 'w') as f:
        # input here
        f.write(f'{n}')
    with open(f'tests/{i:04}.out', 'w') as f:
        # output here
        f.write(f'')