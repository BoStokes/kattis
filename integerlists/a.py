from collections import *
from sys import stdin, stdout
input = lambda:stdin.readline().rstrip()
output = []

for _ in range(int(input())):
    program = input()
    n = int(input())
    nums = input()[1:-1]
    data = deque(list(nums.split(','))) if nums != '' else deque()
    
    r = False
    error = False
    for c in program:
        if c == 'R':
            r = not r
        elif not data:
            error = True
            output.append('error\n')
            break
        elif r:
            data.pop()
        else:
            data.popleft()
    if not error:
        output.append(f'[{",".join(reversed(data) if r else data)}]\n')
stdout.writelines(output)