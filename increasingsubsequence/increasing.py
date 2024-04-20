from bisect import bisect_left

while True:
    n, *a = map(int, input().split())
    if n == '0':
        break

    lis = []
    lis_idx = []
    parents = [-1]*n
    lis_end = -1

    for i, v in enumerate(a):
        pos = bisect_left(pos, v)

