from collections import defaultdict
from sys import stdin

candidates = []
parties = dict()
counts = defaultdict(int)
for _ in range(int(input())):
    candidate, party = input(), input()
    parties[candidate] = party
    candidates.append(candidate)

c = int(input())
for _ in range(c):
    vote = next(stdin).strip()
    counts[vote] += 1

candidates.sort(key=lambda c: -counts[c])


if counts[candidates[0]] == counts[candidates[1]]:
    print('tie')
else:
    print(parties[candidates[0]])
