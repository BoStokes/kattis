from collections import defaultdict

n = int(input())
m = int(input())
entries = [*map(int, input().split())]
exits = [*map(int, input().split())]

counts = defaultdict(int)
for entry_time in entries:
    for exit_time in exits:
        time = exit_time - entry_time
        if time < 0: continue
        counts[time] += 1
ordered = sorted([(-counts[key], key) for key in counts])
print(ordered[0][1] if ordered else 0)
