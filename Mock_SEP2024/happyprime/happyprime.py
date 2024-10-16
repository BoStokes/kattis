primes = set()
is_prime = [True] * 10_001
is_prime[0] = is_prime[1] = False
for num in range(2, 10_001):
    if is_prime[num]:
        primes.add(num)
        for n in range(num*num, 10_001, num):
             is_prime[n] = False

P = int(input())
data = [list(map(int, input().split())) for _ in range(P)]

from functools import cache
@cache
def func(num):
    visited = set()
    def isHappy(num):
        if num == 1:
            return True
        if num in visited:
            return False
        visited.add(num)

        return isHappy(sum(map(lambda n: int(n)**2, str(num))))
    if num in primes and isHappy(num):
        return "YES"
    return "NO"

for K, candidate in data:
    print(K, candidate, func(candidate))