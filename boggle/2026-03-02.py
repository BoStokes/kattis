from collections import *
from sys import stdin

input = lambda: stdin.readline().rstrip()

def rec_dd():
    return defaultdict(rec_dd)
root = rec_dd()

def insert(s):
    curr = root
    for c in s:
        curr = curr[c]
    curr['END'] = True

def search(s):
    curr = root
    for c in s:
        if c not in curr:
            return False
        curr = curr[c]
    return 'END' in curr

for _ in range(int(input())):
    insert(input())

input()
b = int(input())
boards_input = iter(stdin.read().split())
boards = [[next(boards_input) for _ in range(4)] for _ in range(b)]

def process(words):
    longest = ''
    s = 0
    for w in words:
        if len(w) > len(longest) or (len(w) == len(longest) and w < longest):
            longest = w

        if len(w) in (3,4):
            s += 1
        elif len(w) == 5:
            s += 2
        elif len(w) == 6:
            s += 3
        elif len(w) == 7:
            s += 5
        elif len(w) == 8:
            s += 11
    print(s, longest, len(words))

    # board = boards[0]
for board in boards:
    found_words = set()
    visited = [[False for _ in range(4)] for _ in range(4)]

    def dfs(r, c, word, node):
        if 'END' in node: found_words.add(word)
        for nr in range(r-1, r+2):
            for nc in range(c-1, c+2):
                if (nr,nc) == (r,c): continue
                if not (0<=nr<4 and 0<=nc<4): continue
                if visited[nr][nc]: continue
                char = board[nr][nc]
                if char not in node: continue
                visited[nr][nc] = True
                dfs(nr, nc, word+char, node[char])
                visited[nr][nc] = False

    for i in range(4):
        for j in range(4):
            c = board[i][j]
            if c in root:
                visited[i][j] = True
                dfs(i, j, c, root[c])
                visited[i][j] = False

    process(found_words)