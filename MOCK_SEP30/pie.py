from math import pi
for _ in range(int(input())):
    N, F = map(int, input().split())
    volumes = [*sorted(map(lambda n: pi * int(n)**2, input().split()), reverse=True)]
    # print(N, F+1, volumes)

    upper = 2 * volumes[0]
    lower = 0

    while len(volumes) > F + 1:
        volumes.pop()

    while abs(upper - lower) > 1e-3:
        guess = (upper + lower) / 2

        pieces_needed = F + 1
        for volume in volumes:
            pieces_needed -= volume // guess
        if pieces_needed <= 0:
            lower = guess
        else:
            upper = guess
    print(lower)
