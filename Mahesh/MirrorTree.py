class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def inorder(root):
    if(root == None):
        return

    else:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def createMirror(root):

    if(root == None):
        return

    else:
        temp = root

        createMirror(root.left)
        createMirror(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

print("Before mirror")
inorder(node1)

createMirror(node1)

print("\nAfetr mirror")
inorder(node1)
