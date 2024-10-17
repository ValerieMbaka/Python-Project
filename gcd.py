# A program that uses recursion to calculate the GCD of two numbers.
# Ask the user to input the two numbers.
num1 = int((input("Enter the first number: ")))
num2 = int((input("Enter the second number: ")))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcdCalculation():
    try:
        if num1 <= 0 or num2 <= 0:
            print("Error: Both numbers must be positive.")
        else:
            result = gcd(num1, num2)
            print(f"The greatest common divisor of {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid integers.")

gcdCalculation()
