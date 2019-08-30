class Node:
    def __init__(self,value):
        self.val = value
        self.right = None
        self.left = None

def traverseInorder(node):
    if(node != None):
        traverseInorder(node.left)
        print(node.val)
        traverseInorder(node.right)

def printLeafNodes(node):

    if(node != None):
        printLeafNodes(node.left)
        if(node.right == None and node.left == None):
            print(node.val)
        printLeafNodes(node.right)



node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)
node7 = Node(70)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

traverseInorder(node1)

print("Leaf nodes")
printLeafNodes(node1)

