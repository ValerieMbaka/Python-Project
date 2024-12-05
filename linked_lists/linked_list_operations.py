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
        
        # Inserting a node at the end of the linked list
        def insertAtEnd(self, data):
                # Create a new node
                newNode = Node(data)
                # Check if the head is empty
                if self.head is None:
                        # Point the head to this new node
                        self.head = newNode
                else:
                        # Traverse the linked list to find the last node
                        last = self.head
                        while last.next is not None:
                                last = last.next
                        # Point the last node to the new node
                        last.next = newNode
        
        # 2. Deletion
        # Function to delete a node in between the linked list
        def deleteInBetween(self, value):
                # Check if the linked list is empty
                if self.head is None:
                        print("The linked list is empty")
                        return
                        
                # Delete the head node
                if self.head.data == value:
                        current = self.head
                        self.head = current.next
                        return
                
                # Declare variables to hold the previous and current nodes
                previous = None
                current = self.head
                
                # Traverse the linked list to find the node to delete
                while current is not None:
                        if current.data == value:
                                previous.next = current.next
                                current.next = None
                                del current
                                return
                        previous = current
                        current = current.next
                # Print a message if the value is not found
                print("The value ", value, " was not found in the linked list")
        
        # The printList function traverses the linked list as it prints the data of each node
        def printList(self):
                currentNode = self.head
                while currentNode is not None:
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
mySinglyLinkedList.insertAtEnd('E')
mySinglyLinkedList.insertAtEnd('F')

# Print the content of the linked list
mySinglyLinkedList.printList()
        
# Delete a node in between the linked list
mySinglyLinkedList.deleteInBetween('C')

# Print the new linked list
mySinglyLinkedList.printList()