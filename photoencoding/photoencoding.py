from collections import Counter
m=int(input())
nums=Counter(int(input()) for _ in range(m))
n = 0
for num, count in nums.most_common():
    if num % 2 == 0:
        current = num // 2 + 1 + count // 2
    else:
        current = ((num+1) // 2 + 1) + (count - 1) // 2
    n = max(n, current)
print(n)