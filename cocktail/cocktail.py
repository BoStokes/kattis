N, T = map(int, input().split())

potions = []

for _ in range(N):
    potions.append(int(input()))

potions = sorted(potions, reverse=True)

output = 'YES'
if potions:
    duration = potions.pop(0)
while potions:
    duration -= T
    duration = min(duration, potions.pop(0))
    if duration <= 0:
        output = 'NO'
        break

print(output)