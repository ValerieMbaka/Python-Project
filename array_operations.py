# Importing the array module and array name
from array import *

# Declare and assign values to the array
myArray = array('i', [5, 8, 2, 5, 9, 16, 23, 30])

# Inserting a value at the end of the array
myArray.append(40)

# Inserting a value at the front of the array
myArray.insert(0, 4)

# Inserting a value in between the array
myArray.insert(5, 11)

# Print the array
print(myArray)

# Concatenating 2 arrays - Joining 2 arrays
myArray2 = array('i', [1, 2, 3, 4, 5])
myNewArray = myArray + myArray2
print(myNewArray)

# Declare a single characters array
# myChar = array('u', ['A', 'B', 'C'])
