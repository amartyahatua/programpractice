class nLinkedList:
    def __init__(self,value):
        self.next = None
        self.val = value

def printLinkedList(start):
    while(start is not None):
        print(start.val)
        start = start.next


def removeLoop(start):
    slowPointer = start
    fastPointer = start

    while(slowPointer and fastPointer and fastPointer.next):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if(slowPointer == fastPointer):
            fastPointer.next = None
            print("Removing loop and pring the list:")
            printLinkedList(start)


def detectLoop(start):
    slowPointer = start
    fastPointer = start.next

    while(slowPointer and fastPointer and fastPointer.next):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if(slowPointer == fastPointer):
            print("Loop found at --> ", fastPointer.next.val)
            return True
    print("No loop")
    return False

def reverseLinkedList(start):
    current = start
    prev = None
    print("Priniting the reverse list: ")
    while(current.next != None):
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    current.next = prev
    printLinkedList(current)


node1 = nLinkedList(10)
node2 = nLinkedList(20)
node3 = nLinkedList(30)
node4 = nLinkedList(40)
node5 = nLinkedList(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

#Detect loop and remove it
if(detectLoop(node1)):
    removeLoop(node1)

#Reverse Linkedlist
reverseLinkedList(node1)


