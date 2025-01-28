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


# Function to merge two sorted arrays
def merge(left, right):
    sorted_array = []
    i = j = 0

    # Compare elements from the left and right arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add any remaining elements from left or right arrays
    sorted_array.extend(left[i:])  # Correctly adding remaining elements
    sorted_array.extend(right[j:]) # Correctly adding remaining elements
    
    return sorted_array


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
