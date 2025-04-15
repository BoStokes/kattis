T = int(input())
for _ in range(T):
    print(len({input() for _ in range(int(input()))}))
    
