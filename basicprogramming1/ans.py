from statistics import median
from string import ascii_lowercase

N, t = map(int, input().split())
A = map(int, input().split())

if t == 1:
    print(7)
elif t == 2:
    print('Bigger' if A[0] > A[1] else 'Equal' if A[0] == A[1] else 'Smaller')
elif t == 3:
    print(median(A[:3]))
elif t == 4:
    print(sum(A))
elif t == 5:
    print(sum(filter(lambda num: num % 2 == 0, A)))
elif t == 6:
    mod = list(map(lambda n: n % 26, A))
    print(*map(lambda n: ascii_lowercase[n], mod), sep='')
elif t == 7:
    i = 0
    visited = set()
    while True:
        visited.add(i)
        i = A[i]
        if i in visited:
            print('Cyclic')
            break
        if i < 0 or N <= i:
            print('Out')
            break
        if i == N - 1:
            print('Done')
            break
