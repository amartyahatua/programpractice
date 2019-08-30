class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def printLL(head):
    while(head != None):
        print(head.val)
        head = head.next

def LLtoStack(list):
    stackList = []
    while(list !=None):
        stackList.append(list.val)
        list = list.next
    return stackList

def StacktoLL(stackList):
    for i in range(len(stackList)):
        #print(stackList.pop())
        tos = stackList.pop()
        if(i ==0):
            head = Node(tos)
            lastnode = head
        else:
            presentnode = Node(tos)
            lastnode.next = presentnode
            lastnode = presentnode
    #printLL(head)
    return head


def additionOfLL(node1, node2):
    ansList = []
    carry = 0
    sum = 0
    while(node1 != None and node2 != None):
        val1 = node1.val
        val2 = node2.val
        sum = val1 + val2 + carry
        if(sum > 9):
            carry = 1
            sum = int(sum%10)
        else:
            carry = 0
        ansList.append(sum)

        node1 = node1.next
        node2 = node2.next


    while(node1 != None):
        sum = node1.val + carry

        if (sum > 9):
            carry = 1
            sum = int(sum % 10)
        else:
            carry = 0
        ansList.append(sum)
        node1 = node1.next

    while (node2 != None):
        sum = node2.val + carry

        if (sum > 9):
            carry = 1
            sum = int(sum % 10)
        else:
            carry = 0
        ansList.append(sum)
        node2 = node2.next
    #if(carry == 1):

    return ansList





node11 = Node(9)
node12 = Node(7)
node13 = Node(2)
node14 = Node(5)

node11.next = node12
node12.next = node13
node13.next = node14


node21 = Node(9)
node22 = Node(7)
node23 = Node(2)
node24 = Node(5)

node21.next = node22
node22.next = node23
node23.next = node24

print(LLtoStack(node11))
head1 = StacktoLL(LLtoStack(node11))

head2 = StacktoLL(LLtoStack(node21))

sum = additionOfLL(node11, node21)

print("Sum of two LL is: ", sum)