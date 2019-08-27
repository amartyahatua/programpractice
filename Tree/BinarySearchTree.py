class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

def insert(root,node):

    if(root is None):
        root = Node

    else:
        if(root.val < node.val):
            if(root.right is None):
                root.right = node
            else:
                insert(root.right, node)
        else:
            if(root.left is None):
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):

    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50)

insert(r, Node(60))
insert(r, Node(20))
insert(r, Node(30))
insert(r, Node(90))

inorder(r)


