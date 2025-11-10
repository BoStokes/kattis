N = int(input())

ranges = sorted(tuple(map(int, input().split())) for _ in range(N))

rooms = 0
curr_end = -1

for start, end in ranges:
    if end < curr_end:
        curr_end = end
    elif start > curr_end:
        rooms += 1
        curr_end = end
print(rooms)