class Node:
        def __init__(self, data):
                self.data = data
                self.next = None
                
class Queue:
        def __init__(self):
                self.front = None
                self.rear = None
        
        # Check if the queue is empty
        def isEmpty(self):
                return self.front is None
        
        # Display contents of the queue
        def display(self):
                if self.isEmpty():
                        print("The queue is empty")
                else:
                        current = self.front
                        while current is not None:
                                print(current.data)
                                current = current.next
                                
        # Add items at the back of the queue
        def enqueue(self, data):
                new_node = Node(data)
                
                # Check if the rear is None
                if self.rear is None:
                        self.front = new_node
                        self.rear = new_node
                else:
                        self.rear.next = new_node
                        self.rear = new_node
        
        # Remove items from the front of the queue
        def dequeue(self):
                if self.isEmpty():
                        print("The queue is empty")
                        return
                else:
                        self.front = self.front.next
                        if self.front is None:
                                self.rear = None
                        return
                                
# Creating the queue
fruits = Queue()

# Add fruits to the queue
fruits.enqueue("Apple")
fruits.enqueue("Banana")
fruits.enqueue("Cherry")
fruits.enqueue("Date")

# Remove an item from the queue
fruits.dequeue()

# Print the elements of the queue
fruits.display()
               