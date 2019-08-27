class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def BFS(root):
    if(root is None):
        return

    else:
        queue = []
        queue.append(root)

        while(len(queue) > 0):
            print(queue[0].val)
            node = queue.pop(0)

            if(node.left is not None):
                queue.append(node.left)

            if(node.right is not None):
                queue.append(node.right)


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)


print(root.val)

print(root.left.val)
print(root.right.val)

print(root.left.left.val)
print(root.left.right.val)

print(root.right.left.val)
print(root.right.right.val)

print("++++++++++BFS++++++++++")
BFS(root)
