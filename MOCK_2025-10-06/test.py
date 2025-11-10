from functools import cache

while True:
    k = 2
    @cache
    def dfs(length, i):
        if i < 0 or i > k or length == 0:
            return 0
        if length == 1:
            return 1
        return dfs(length-1, i-1) + dfs(length-1, i) + dfs(length-1, i+1)
    
    print(sum(dfs(2, i) for i in range(k+1)))
    # print(dfs(3, 0))
    break