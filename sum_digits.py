# A recursive function that calculates the sum of digits in a number
num = int(input("Enter a number: "))
def sum_digits(n):
        # Base case: when n is 0, return 0 (no more digits to sum)
        if n == 0:
                return 0
        else:
                # Recursive case: sum the last digit and recurse on the remaining digits
                return n % 10 + sum_digits(n // 10)

result = sum_digits(num)
print(f"The sum of digits in the number {num} is {result}")


def sum_of_even_numbers(input_list):
        even_sum = sum(x for x in input_list if x % 2 == 0)
        return even_sum

my_list = [1, 2, 3, 4, 5, 6]
result = sum_of_even_numbers(my_list)
print(result)
