n = int(input())
heights = sorted(list(map(int, input().split())), reverse=True)
charges = 0

i = n - 1
curr = heights[i]
while curr < i:
    while i >= 0 and heights[i] == curr:
        i -= 1
    curr = heights[i]
    charges += 1
charges += i + 1
print(charges)