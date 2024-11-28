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

# Accessing a single element in an array
print(myArray[3])

# Traverse elements in an array
# for num in myArray:
#         print(num)
        
# Function to traverse and print elements of an array
def traverse_array(arr):
        for num in arr:
                print(num)
                
traverse_array(myArray)
traverse_array(myNewArray)

# Function to access accessing item in an array
def accessByIndex(arr, index):
        assert index >= 0 and index < len(arr), "The index must be positive and within the range of the array length"
        print(arr[index])
        
accessByIndex(myArray, 3)

# Function to search for an element in an array
def search_array(arr, searchValue):
        for num in arr:
                if num == searchValue:
                        return num
        # If value is not found
        return "The element does not exist in the array"

search_array(myArray, 9)

# Function to search for an element in an array and return both the index and element
# def search_array(arr, searchValue):
#         for index, num in enumerate(arr):
#                 if num == searchValue:
#                         return index
#         # If value is not found
#         return "The element does not exist in the array"
#
# search_array(myArray, 9)

print(myArray)
# Function to update an element in an array
def update_array(arr, value, newValue):
        index = search_array(arr, value)
        if type(index) is int:
                arr[index] = newValue
        else:
                print("Value not found")
                
update_array(myArray, 9, 15)
print(myArray)

# Function to delete an element in an array
print(myNewArray)
myNewArray.remove(5)
myNewArray.pop(2)
myNewArray.pop()
print(myNewArray)
