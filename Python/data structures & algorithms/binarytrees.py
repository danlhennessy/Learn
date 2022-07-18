# Hierarchal data structure. Root node = Top, Leaf nodes = Bottom nodes. Binary Tree elements can have 2 children max

# Class representing an Individual Node:
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        
    def __str__(self):
        return str(self.val)

        
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(12)
root.right.right = Node(7)

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = Node(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = Node(data)
    return node

mytup = ((1,3,None), 2, ((None,3,4,5,(6,7,8))))

mynode = parse_tuple(mytup)

def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

print(inorder(root))