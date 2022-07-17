# Hierarchal data structure. Root node = Top, Leaf nodes = Bottom nodes. Binary Tree elements can have 2 children max

# Class representing an Individual Node:
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        
    def __str__(self):
        return str(self.value)

        
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(12)
root.right.right = Node(7)

def printInorder(root):
  
    if root:
  
        # First recur on left child
        printInorder(root.left)
  
        # then print the data of node
        print(root.val),
  
        # now recur on right child
        printInorder(root.right)
        
printInorder(root)

