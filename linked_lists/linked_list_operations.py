# Linked list operations
# ------------------------------------------------
# Creating the Node class
class Node:
        # This is the constructor/initialization function of the Node class
        # It will receive the data of the node
        def __init__(self, data):
                self.data = data
                self.next = None
                
# Creating a Linked list class to implement the linked list operations
class SinglyLinkedList:
        # Initialization function - creates the head of the linked list
        def __init__(self):
                self.head = None
        
        # 1.Insertion
        # Inserting a node at the beginning of a linked list
        def insertAtBeginning(self,data):
                # Create the node
                newNode = Node(data)
                
                # Check if head is empty
                if self.head is None:
                        self.head = newNode
                else:
                        # Point the new node to the current head
                        newNode.next = self.head
                        
                        # Point the head to the new node
                        self.head = newNode
                        
        def printList(self):
                currentNode = self.head
                while currentNode:
                        print(currentNode.data, end = " -> ")
                        currentNode = currentNode.next
                print("None")
        
# Create the linked list
mySinglyLinkedList = SinglyLinkedList()

# Call the insertAtBeginning function to insert a node at the beginning of the linked list
mySinglyLinkedList.insertAtBeginning('D')
mySinglyLinkedList.insertAtBeginning('C')
mySinglyLinkedList.insertAtBeginning('B')
mySinglyLinkedList.insertAtBeginning('A')

# Print the content of the linked list
mySinglyLinkedList.printList()
        
