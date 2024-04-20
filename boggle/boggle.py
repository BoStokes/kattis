from functools import cache

w = int(input())
words = [input() for _ in range(w)]

root = dict()
for word in words:
    curr = root
    for letter in word:
        if letter not in curr:
            curr[letter] = dict()
        curr = curr[letter]
    curr['END'] = word


input()
b = int(input())
boards = []
for i in range(b):
    boards.append(tuple(input() for _ in range(4)))
    if i < b-1: input()

@cache
def find_words(board):
    def in_bounds(r, c):
        return 0 <= r <= 3 and 0 <= c <= 3
    used = [[False for _ in range(4)] for _ in range(4)]
    directions = ((-1,-1),(-1,0),(-1,1),
                  (0,-1),        (0,1),
                  (1,-1), (1,0), (1,1))
    found = set()
    
    def dfs(r, c, curr):
        used[r][c] = True
        if 'END' in curr and curr['END'] not in found:
            found.add(curr['END'])
        for dir in directions:
            nextR, nextC = r + dir[0], c + dir[1]
            if in_bounds(nextR, nextC) and not used[nextR][nextC] and board[nextR][nextC] in curr:
                dfs(nextR, nextC, curr[board[nextR][nextC]])
        used[r][c] = False

    for r in range(4):
        for c in range(4):
            let = board[r][c]
            if let in root:
                dfs(r, c, root[let])
    return list(found)

def get_score(words):
    score = 0
    scores = {3:1, 4:1, 5:2, 6:3, 7:5, 8:11}
    for word in words:
        score += scores.get(len(word), 0)
    return score

for board in boards:
    words_on_board = sorted(find_words(board))
    print(f'{get_score(words_on_board)} {max(words_on_board, key=len)} {len(words_on_board)}')
