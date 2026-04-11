# Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Creating Nodes
root = Node("Root")

nodeA = Node("Node A")
nodeB = Node("Node B")
nodeC = Node("Node C")
nodeD = Node("Node D")
nodeE = Node("Node E")
nodeF = Node("Node F")
nodeG = Node("Node G")
nodeH = Node("Node H")

# Building Tree Structure 
root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeC.left = nodeG
nodeF.right = nodeH

# Accessing a specifc node
print("Root.Left.Left.Left Data: ", root.left.left.left.data)