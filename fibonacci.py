# A program that uses recursion to find the fibonacci of a number that is input by the user.
# Ask the user to input a positive whole number
num = int((input("Enter a positive whole number: ")))
def fibonacci(num):
    # Find the Unintended Case
    assert num >= 0 and int(num) == num, "The number should be a positive whole number."

    # Find the Base Case
    if num in [0,1]:
        return num
    else:
        # Do the Recursive Case
        return fibonacci(num-1) + fibonacci(num-2)

# Use the function to find the fibonacci of the number and print the result
results = fibonacci(num)
print(results)