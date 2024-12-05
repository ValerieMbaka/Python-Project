# Singly Linked Lists Operations
# Creating the Node class
class Node:
        # This is the constructor/initialization function of the Node class
        # It will receive the data of the node
        def __init__(self, data):
                self.data = data
                self.next = None
                
# Create the node by creating an object of the class Node
nodeA = Node ('A')
nodeB = Node ('B')
nodeC = Node ('C')

# Access the data of the created node
# print(nodeA.data)
# print(nodeA.next)


# Memory address of the node
# print(nodeA)
# print(nodeB)
# print(nodeC)

# Linking the nodes
nodeA.next = nodeB
nodeB.next = nodeC

print(nodeA.next.data)
print(nodeA.next.next)
print(nodeC)