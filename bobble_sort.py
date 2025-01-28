def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps are made
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark as swapped

        # If no swaps were made, the array is already sorted
        if not swapped:
            break

    return arr


# Input array
n = [4, 5, 9, 3, 2, 6]

# Sorting the array
result = bubble_sort(n)

# Output the result
print("Sorted array:", result)
