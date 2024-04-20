n = int(input())
problems = [int(input()) for _ in range(n)]

ans = []
for k in range(1, n+1):
    if n % k != 0:
        continue

    size = n // k
    smallest_lefts = []
    biggest_rights = []

    for i in range(k):
        interval = problems[i*size:(i+1)*size]
        smallest_lefts.append(min(interval))
        biggest_rights.append(max(interval))
    if all(smallest_lefts[i] > biggest_rights[i-1] for i in range(k)):
        ans.append(i)