T = int(input())

class node:
    def __init__(self):
        self.children = set()

for _ in range(T):
    n, m = map(int, input().split())
    nodes = [node() for _ in range(m)]
    
