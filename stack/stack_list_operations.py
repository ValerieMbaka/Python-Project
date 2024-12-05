class Stack:
        def __init__(self):
                self.list = []
                
        # Check if the list is empty
        def isEmpty(self):
                return self.list == []
        
        # Add an element on top of the stack
        def push(self, value):
                self.list.append(value)
                
        # Removing an element from the top of the stack
        def pop(self):
                if self.isEmpty():
                        raise Exception("The list is empty")
                return self.list.pop()
        
        # Check the element on top of the stack
        def peek(self):
                if self.isEmpty():
                        raise Exception("The list is empty")
                print (self.list[-1]) # This will return the last element of the list
        
# Create a stack
myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)

myStack.peek()
