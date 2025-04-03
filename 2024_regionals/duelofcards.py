from sys import stdin
n = int(input())
alice = {int(line) for line in stdin}
bob = [card for card in range(1, 2*n + 1) if card not in alice]
alice = sorted(alice)

def find_max_score(player1, player2):
    used = [False] * (2*n + 1)
    score = 0
    for p2_card in player2:
        # find lowest card better in player1
        for p1_card in player1:
            if p1_card > p2_card and not used[p1_card]:
                score += 1
                used[p1_card] = True
                break
        else:
            break
    return score

print(n - find_max_score(bob, alice), find_max_score(alice, bob))