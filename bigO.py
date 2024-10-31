# from pygame.sndarray import array

def find_first_element(arr):
    if arr:
        return arr[0]
    else:
        return None

array = [1, 2, 3, 4, 5]
print(find_first_element(array))

def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

array = [1,2,3,4,5]
print(calculate_sum(array))

def process_data(arr):
    # Linear time complexity O(n)
    total = 0
    for num in arr:
        total += num

    # Quadratic time complexity O(n^2)
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

    # Constant time complexity O(1)
    print("Processing complete")

array = [1, 2, 3, 4, 5]
process_data(array)


