from itertools import permutations

x = int(input())
best_p = float('inf')

for possibility in permutations(str(x)):
    num_p = int(''.join(possibility))
    if num_p > x:
        best_p = min(best_p, num_p)
print(0 if best_p == float('inf') else best_p)

