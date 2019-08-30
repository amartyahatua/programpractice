import  numpy as np
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None





def findMiddle(start):
    slowPointer = start
    fastPointer = start

    while(fastPointer.next != None and fastPointer.next.next != None ):
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next

    print("Middle value is ",slowPointer.val)








node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

findMiddle(node1)
