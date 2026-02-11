from collections import*
print(max(x//2+1+c//2 if x%2==0 else((x+1)//2+1)+(c-1)//2 for x,c in Counter(int(input())for _ in range(int(input()))).most_common()))