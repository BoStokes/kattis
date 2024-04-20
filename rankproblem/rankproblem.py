n, m = map(int, input().split())
teams = [f'T{i}' for i in range(1, n+1)]
# games = [tuple(map(int, [int(team[1]) for team in input().split()])) for i in range(m)]
games = [tuple([team for team in input().split()]) for i in range(m)]

rankings = {s:int(s[1]) for s in teams}

print(teams)
print(games)
print(rankings)