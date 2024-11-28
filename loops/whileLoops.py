""" You have a magic box that doubles the count of items you put in every day. The given program takes the initial
count of the items and the number of days as input. Write a program to calculate and output items' count on the
last day """
# The program calculates the number of items on the last day by doubling the count of items every day.
items = int(input("Enter the number of items: "))
days = int(input("Enter the number of days: "))
while days > 0:
        items *= 2
        days -= 1

print(items)

