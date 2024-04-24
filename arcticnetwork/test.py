from itertools import permutations
from math import dist


perms = [*permutations(range(3),2)]
print(perms)
d = [[dist(perms[i],perms[j]),i,j] for i,j in perms]
print(*d)