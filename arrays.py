def calculate_sum(arr):
        total = 0
        for num in arr:
                total += num
        return total

def main():
        # Ask the user to enter the length of     the array
        length = int(input("Enter the length of the array: "))

        # Create the array and ask the user to enter the numbers
        arr = []
        for i in range(length):
                num = int(input(f"Enter number {i + 1}: "))
                arr.append(num)

        # Display the array elements
        print("Array elements:", arr)

        # Calculate the sum of elements in the array
        total_sum = calculate_sum(arr)
        print("Sum of array elements:", total_sum)

        # Ask the user for the sort order
        sort_order = input("Do you want to sort the array in ascending or descending order? (asc/desc): ").strip().lower()

        # Sort the array elements according to the user response
        if sort_order == "asc":
                arr.sort()
        elif sort_order == "desc":
                arr.sort(reverse=True)
        else:
                print("Invalid sort order entered. Array will not be sorted.")

        # Display the sorted array
        print("Sorted array elements:", arr)

# Run the main function
if __name__ == "__main__":
        main()