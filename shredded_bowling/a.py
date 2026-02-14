from itertools import *

goal, third_bowl = map(int, input().split())

game = [] # holds a permutation of a game as tuples: (first_bowl, second_bowl)

# returns the total score inside game, or -1 if game is invalid
def score_game():
    global third_bowl

    if third_bowl > 0 and sum(game[9]) < 10: return -1

    total = 0
    for i in range(8):
        r1, r2 = game[i]

        total += r1+r2

        if r1+r2 == 10:
            total += game[i+1][0]

        if r1 == 10:
            total += game[i+1][1] if game[i+1][0] != 10 else game[i+2][0]
    
    # frame 9
    r1, r2 = game[8]
    total += r1+r2
    if r1+r2 == 10:
        total += game[9][0]
    if r1 == 10:
        total += game[9][1]

    # frame 10
    r1, r2 = game[9]
    total += r1+r2
    if r1+r2 >= 10:
        total += third_bowl

    return total

frames = [tuple(map(int, input().split())) for _ in range(10)]
highest_lesser = -1
lowest_greater = 301
for perm in permutations(frames):
    game = [*perm]

    score = score_game()
    if score == -1:continue

    if score < goal:
        highest_lesser = max(highest_lesser, score)
    elif score > goal:
        lowest_greater = min(lowest_greater, score)
    else:
        print(goal, 'Yes')
        exit()

ans = [goal]
if highest_lesser >= 0:
    ans.append(highest_lesser)
if lowest_greater <= 300:
    ans.append(lowest_greater)
print(*ans)