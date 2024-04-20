for _ in range(int(input())):
    input()
    kids = int(input())
    candies = 0
    for _ in range(kids):
        candies += int(input())
    print('YES' if candies % kids == 0 else 'NO')