# Function to perform merge sort
def merge_sort(arr):
    # Base case: Check if the array has one or no elements
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    while left and right:  # Continue until one list is empty
        if left[0] < right[0]:
            sorted_array.append(left.pop(0))  # Remove and append the smallest element
        else:
            sorted_array.append(right.pop(0))  # Remove and append the smallest element
    # Extend with any remaining elements
    return sorted_array + left + right



# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
