# A recursive function that calculates the sum of digits in a number
def sum_digits(n):
    # Base case: when n is 0, return 0 (no more digits to sum)
    if n == 0:
        return 0
    else:
        # Recursive case: sum the last digit and recurse on the remaining digits
        return n % 10 + sum_digits(n // 10)
