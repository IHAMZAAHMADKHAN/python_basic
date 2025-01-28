def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):  # Correct range for outer loop
        for j in range(i):  # Inner loop to compare adjacent elements
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                # Swap elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr  # Return the sorted array


# Input array
n = [3, 8, 9, 5, 3, 1, 2]

# Sort the array
result = bubble_sort(n)

# Print the result
print("Sorted array:", result)
