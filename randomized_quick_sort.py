import random


def randomized_quicksort(arr, low, high):
    if low < high:
        # Randomly pick a pivot index and partition the array
        pivot_index = random_partition(arr, low, high)

        # Recursively apply to the left and right subarrays
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)


def random_partition(arr, low, high):
    # Randomly select a pivot index, swap it with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)


def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Move pivot to correct location
    return i + 1
