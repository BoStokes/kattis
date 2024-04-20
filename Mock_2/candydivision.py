n = int(input())

# ans = set(factor-1 for i in range(1, int(n**0.5) + 1) if n % i == 0 
#           for factor in (i, n//i))
ans = []
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        ans.append(i-1)
        ans.append(n//i - 1)
ans = set(ans)
ans = [str(num) for num in sorted(ans)]
print(' '.join(ans))
