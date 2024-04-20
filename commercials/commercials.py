N, P = map(int, input().split())
people = map(int, input().split())
for i in range(people):
    people[i] -= P

best = -1
score = 0
for person in people:
    score += person
    if score < 0:
        score = 0
        continue
    best = max(best, score)
print(best)