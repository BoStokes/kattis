from sys import stdin
input = lambda: next(stdin).rstrip()

class WordNode:
    def __init__(self, word):
        self.word = word
        self.next = None
        self.tail = self
    def add(self, node):
        self.tail.next = node
        self.tail = node.tail
    def __repr__(self):
        return self.word

n = int(input())
words = {i:WordNode(input()) for i in range(1, n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    words[a].add(words[b])
    del words[b]

for node in words.values():
    while node is not None:
        print(node, end='')
        node = node.next
    print()
