from sys import *
from collections import *

left = deque()
right = deque()
size = 0

input()
for line in stdin:
    command, x = line.split()

    if command == 'push_front':
        left.appendleft(x)
        size += 1
    elif command == 'push_back':
        right.append(x) += 1
    elif command == 'push_middle':
        if