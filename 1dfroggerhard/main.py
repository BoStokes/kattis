n = int(input())
board = list(map(int, input().split()))
ans = 0
for i in range(n):
    visited = [False] * n
    position = i
    while 0 <= position < n and not visited[position]:
        ans += 1
        visited[position] = True
        position += board[position]
print(ans)