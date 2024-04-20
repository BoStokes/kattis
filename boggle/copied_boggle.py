from functools import cache

@cache
def findWords(board, word):
    def dfs(r, c, curr):
        original = board[r][c]
        board[r][c] = '.'
        for dir in directions:
            if 'END' in curr:
                wordsBoard.append(curr['END'])
                del curr['END']
            nextR = r + dir[0]
            nextC = c + dir[1]
            if nextR < 0 or nextR >= len(board) or nextC < 0 or nextC >= len[board[r]]:
                continue
            if board[nextR][nextC] not in curr:
                continue
            next = curr[board[r][c]]
            dfs(nextR, nextC, next)
        board[r][c] = original
        



    root = dict()
    wordsBoard = []
    for word in words:
        curr = root
        for let in word:
            if let not in curr:
                curr[let] = dict()
            curr = curr[let]
        curr['END'] = word

    directions = ((-1,-1),(-1,0),(-1,1),
                  (0,-1),        (0,1),
                  (1,-1), (1,0), (1,1))
    
w = int(input())
words = [input() for _ in range(w)]

input()

b = int(input())
boards = []
for i in range(b):
    boards.append([input() for _ in range(4)])
    if i < b-1: input()

def score(word):
    n = len(word)
    if 3 <= n <= 4:
        return 1
    if n == 5:
        return 2
    if n == 6:
        return 3
    if n == 7:
        return 5
    if n == 8:
        return 11
    
for board in boards:
    w = findWords(board)