class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def inorder(current):
    print("Inorder")
    nstack = []
    while((current != None) or (len(nstack)>0)):
        while(current != None):
            nstack.append(current)
            current=current.left

        if(current == None and len(nstack) > 0):
            tos=nstack.pop()
            print(tos.val)
            current=tos.right


def preorder(current):
    print("Preorder")
    nstack.append(current)
    while((current != None) and (len(nstack)>0)):
        if(current != None):
            value = nstack.pop()
            print(value.val)

            if(value.right != None):
                nstack.append(value.right)

            if(value.left != None):
                nstack.append(value.left)
    # while((current != None) or (len(nstack)>0)):
    #     while(current != None):
    #
    #         nstack.append(current)
    #         current=current.left


node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node5.left=node6


current=node1
nstack = []
inorder(node1)

print("**********************")
preorder(node1)
#nstack.append(current)




