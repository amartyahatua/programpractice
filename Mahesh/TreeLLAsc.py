class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

class nLinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None











def inorder(root):

    if(root == None):
        return
    else:
        inorder(root.left)
        print(root.val)
        inorder(root.right)




def createNodeDLL(head, node):
    #prev = None
    if(node == None):
        return
    else:
        createNodeDLL(head, node.left)
        if(head == node):
            head = node
        else:
            node.left = prev
            prev.right = node

        prev = node
        createNodeDLL(head, node.right)

node1 = Node(60)
node2 = Node(50)
node3 = Node(40)
node4 = Node(55)
node5 = Node(70)
node6 = Node(65)
node7 = Node(75)

node1.left = node2
node1.right = node5

node2.left = node3
node2.right = node4

node5.left = node6
node5.right = node7

prev = Node(None)
createNodeDLL(node1, node1)
head = node1
while(head != None):
    print(head.val)
    head = head.right

print("Full list:")
inorder(node1)
