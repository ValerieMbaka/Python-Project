students = ("Val", "Joy", "Sam", "Hyke", "Yvonne")
print(students)

# Counting the number of items in a tuple
print(len(students))

# Print the last item in the tuple
print(students[-1])

# Printing a range of items in the list
print(students[:3])  # Prints items up to index 2, the third index is ignored

print(students[1:3]) # Prints items from index 1 to index 2
print(students[-1:-3])  # Prints nothing because the range is invalid
print(students[-3:-1])  # Prints items from the third last index to the second last index
