from sys import stdin
from itertools import permutations

print(*sorted(set(a+b for a, b in permutations(stdin.read().split(), 2))), sep='\n')