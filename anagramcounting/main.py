from sys import stdin
from collections import Counter

factorials = [1] * 101
for i in range(1, 101):
    factorials[i] = i * factorials[i - 1]


for word in [line.strip() for line in stdin]:
    permutations = factorials[len(word)]
    counts = Counter(word)
    
    for let in counts:
        permutations //= factorials[counts[let]]
    print(permutations)