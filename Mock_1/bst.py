class BST:
    C = 0
    def __init__(self, val, depth) -> None:
        self.val = val
        self.depth = depth
        self.left = None
        self.right = None
        BST.C += depth
        print(BST.C)

def insert(root, val, depth=0):
    if val < root.val:
        if root.left:
            insert(root.left, val, depth+1)
        else:
            root.left = BST(val, depth+1)
    else:
        if root.right:
            insert(root.right, val, depth+1)
        else:
            root.right = BST(val, depth+1)

N = int(input())
root = BST(int(input()), 0)
for i in range(N-1):
    insert(root, int(input()))
