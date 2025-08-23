n = int(input())
alice = set()
for _ in range(n):
    alice.add(int(input()))
bob = [num for num in range(1, 2*n+1) if num not in alice]
alice = sorted(alice)

def max_score(player1, player2):
    score = 0
    p1_lowest, p1_highest = 0, n-1
    p2_highest = n-1

    for i in range(n):
        if player2[p2_highest] > player1[p1_highest]:
            p1_lowest += 1
            p2_highest -= 1
        else:
            score += 1
            p1_highest -= 1
            p2_highest -= 1
    return score

print(n-max_score(bob, alice), max_score(alice, bob))