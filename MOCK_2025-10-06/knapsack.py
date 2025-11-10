from sys import stdin, stdout
data = stdin.read().split()

idx = 0
while idx < len(data):
    C = int(data[idx]); idx+=1
    n = int(data[idx]); idx+=1

    values = []
    weights = []
    for _ in range(n):
        values.append(int(data[idx])); idx+=1
        weights.append(int(data[idx])); idx+=1

    dp = [0] * (C + 1)

    for i in range(1, n+1):
        for j in range(C, weights[i-1] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i-1]] + values[i-1])
    print(dp[C])