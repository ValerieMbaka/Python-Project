class Queue:
        def __init__(self, max_size):
                self.list = []
                self.max_size = max_size
                
        # To check if the queue is empty
        def isEmpty(self):
                return self.list == []
        
        # To print queue items
        def print_queue(self):
               if self.isEmpty():
                       print("The queue is empty")
               for item in self.list:
                       print(item)
                       
        # To add an item at the end of the queue
        def enqueue(self, item):
                if len(self.list) == self.max_size:
                        print("The queue is full")
                        return
                self.list.append(item)
                
        # To remove an item from the start of the queue
        def dequeue(self):
                if self.isEmpty():
                        print("The queue is empty")
                        return
                self.list.pop(0)
                
        # Return the item at the start of the queue
        def peek(self):
                if self.isEmpty():
                        print("The queue is empty")
                        return
                return self.list[0]
        
        # Check the size of the queue
        def size(self):
                return len(self.list)
        
# Create a queue of fruits
fruits = Queue(4)

# Add fruits to the queue
fruits.enqueue("Apple")
fruits.enqueue("Banana")
fruits.enqueue("Cherry")
fruits.enqueue("Date")

# Remove an item from the queue
fruits.dequeue()
# print("Removed : " + fruits.dequeue())

# Print the queue
fruits.print_queue()

# Print items at the FRONT of the queue
print(fruits.peek())

# Print the size of the queue
print(fruits.size())