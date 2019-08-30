class Node:
    def __init__(self,val):
        self.value = val
        self.right = None
        self.left = None
        self.leftLen = 0
        self.rightLen = 0
        self.diameter = 1

def traversingTree(root):
    if(root != None):
        traversingTree(root.left)
        print(root.value)
        traversingTree(root.right)

def calculateDiameter(root):
    if(root != None):
        calculateDiameter(root.left)
        calculateDiameter(root.right)
        if(root.left != None):
            root.leftLen = max(root.left.leftLen, root.left.rightLen) + 1
            root.diameter = root.leftLen + root.rightLen + 1
        if(root.right != None):
            root.rightLen = max(root.right.leftLen, root.right.rightLen) + 1
            root.diameter = root.leftLen + root.rightLen + 1


def calculateMaxDiameter(root):
    if(root == None):
        return -999
    else:

        rdia = root.diameter
        ldia = calculateMaxDiameter(root.left)
        ridia = calculateMaxDiameter(root.right)

        return max(rdia, ldia, ridia)



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)


node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node4.left = node6
node4.right = node7

node5.right = node8

node7.left = node9

node8.left = node10
node8.right = node11

node11.left = node13

node9.right = node12

traversingTree(node1)
calculateDiameter(node1)

print("Diameter -->")

print(node7.diameter)
print(node6.diameter)
print(node4.diameter)
print(node2.diameter)


print("Find max diameter -->")
print(calculateMaxDiameter(node1))
