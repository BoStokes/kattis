from sys import stdin
from pprint import pprint

lines = [line.strip() for line in stdin.readlines()]
vars = dict()

for line in lines:
    line = line.split()
    # pprint(line)
    if line[0] == 'def':
        vars[line[1]] = line[2]
    elif line[0] == 'calc':
        total = 'unknown'
        if line[1] in vars:
            pprint(vars)
            total = vars[line[1]]
            for op, var in zip(line[2::2], line[3:-1:2]):
                print(var, op)
                if var not in vars:
                    total = 'unknown'
                    break
                if op == '+':
                    total += vars[var]
                elif op == '-':
                    total -= vars[var]
        print(f'{' '.join(line[1:])} {total}\n')
    elif [line[0]] == 'clear':
        vars.clear()