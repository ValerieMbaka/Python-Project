def factorial(num):
    assert num >= 0 and int(num) == num, "Number must be a positive whole number"
    if num in [0,1]:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(4))

# A simple program that calculates the factorial of a number
# The user is prompted to enter a positive whole number
num1 = int((input("Enter a positive whole number: ")))

# Define a function to calculate the factorial of the number entered by the user
def factorial(num1):
    # Check whether the number input by the user is a positive integer and display an error message if it is not
    assert num1 >= 0 and int(num1) == num1, "Number must be a positive whole number"
    if num1 in [0,1]:
        return 1
    else:
        return num1 * factorial(num1 - 1)

# Print the factorial of the number input by the user
print(factorial(num1))
