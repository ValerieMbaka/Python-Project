class Node:
        def __init__(self, data):
                self.data = data
                self.next = None
                
class Stack:
        def __init__(self):
                self.head = None
                
        # A function to check if the stack is empty
        def isEmpty(self):
                return self.head is None
        
        # A function to push data to the stack
        def push(self, data):
                newNode = Node(data)
                
                # Check if the stack is empty
                if self.isEmpty():
                        self.head = newNode
                        
                else:
                        newNode.next = self.head
                        self.head = newNode
                        
        # A function to pop data from the stack
        def pop(self):
                if self.isEmpty():
                        print("The stack is empty")
                else:
                        poppedData = self.head.data
                        self.head = self.head.next
                        return poppedData
                
        # A function to peek the top element of the stack
        def peek(self):
                if self.isEmpty():
                        print("The stack is empty")
                else:
                        return self.head.data
                
# Create a stack
myStack = Stack()
myStack.push(1)
myStack.push(2)

myStack.pop()
print(myStack.peek())
