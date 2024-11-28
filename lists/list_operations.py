# Creating a list
numberList = [1, 2, 3, 4, 5.5, 6, 7, 8]
print(numberList)

animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# Creating an empty list
emptyList = []

# Accessing List Elements
# Accessing using positive index
print(animals[0])

# Access using negative index
print(animals[-1])

# Traversing a list
def traverse_list(list):
        if list == []:
                print("List is empty")
        else:
                for element in list:
                        print(element)
                        
traverse_list(numberList)
traverse_list(emptyList)

# Updating a list item
animals[2] = 'goat'
print(animals)

numberList[4] = 15
print(numberList)

# Insert operation
# Inserting at the end
animals.append('elephant')
print(animals)

numberList.append(25)
print(numberList)

# Inserting at the beginning
animals.insert(0, 'lion')
print(animals)

numberList.insert(0, 35)
print(numberList)

# Inserting at a specific index
animals.insert(2, 'tiger')
print(animals)

# Joining lists
# Using the + operator
newList = animals + numberList
print(newList)

# Using the extend() function
numberList.extend(animals)
print(numberList)

# Removing elements from a list
animals.remove('dog')
print(animals)

# Slicing lists
# Syntax - listname[start : stop : step]
myList = [1, 2, 3, 4, 5, 24, 85, 30, 9, 40]
print(myList[0:4:2])
print(myList[:4:])
print(myList[0::2])
print(myList[3::])

# Sorting a list
# Sorting in ascending order
myList.sort()
print(myList)

animals.sort()
print(animals)

# Sorting in descending order
myList.sort(reverse=True)
print(myList)

# Searching for an element in a list
# Using the in operator
if 'cat' in animals:
        print("Found")
        
else:
        print("Not found")

