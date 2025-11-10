data = input().split()
N = int(data[0])
state = 1 if data[1] == 'in' else 0

# original = list(range(1, N+1))
original = list(range(N))
deck = original[:]

split_index = N//2
if N % 2 == 1 and state == 0:
    split_index += 1
count = 0
changed = None

while changed != original:
# for _ in range(52):
    half1, half2 = deck[:split_index], deck[split_index:]
    # print(half1)
    # print(half2)

    pairs = zip(half2, half1) if state else zip(half1, half2)
    changed = [item for pair in pairs for item in pair]
    if N % 2 == 1:
        changed.append(half2[-1] if state else half1[-1])
    deck = changed
    count += 1
print(count)