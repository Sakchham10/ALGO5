import random
import time
import tracemalloc

from quick_sort import quicksort
from randomized_quick_sort import randomized_quicksort


def performance_test(sort_func, arr):
    start, end = 0, len(arr) - 1
    tracemalloc.start()
    start_time = time.time()
    sort_func(arr, start, end)
    end_time = time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak


def generate_datasets(size):
    sorted_data = list(range(size))
    reverse_sorted_data = sorted_data[::-1]
    random_data = random.sample(range(size * 2), size)
    return sorted_data, reverse_sorted_data, random_data


def compare_sorts(size):
    sorted_data, reverse_sorted_data, random_data = generate_datasets(size)

    # Run performance tests
    print(f"Testing Quick Sort on dataset of {size} numbers")
    quick_sorted_time, quick_sorted_memory = performance_test(
        quicksort, sorted_data.copy()
    )
    quick_reverse_sorted_time, quick_reverse_sorted_memory = performance_test(
        quicksort, reverse_sorted_data.copy()
    )
    quick_random_time, quick_random_memory = performance_test(
        quicksort, random_data.copy()
    )

    randomized_sorted_time, randomized_sorted_memory = performance_test(
        randomized_quicksort, sorted_data.copy()
    )
    randomized_reverse_sorted_time, randomized_reverse_sorted_memory = performance_test(
        randomized_quicksort, reverse_sorted_data.copy()
    )
    randomized_random_time, randomized_random_memory = performance_test(
        randomized_quicksort, random_data.copy()
    )

    # Display results
    print(
        f"Quick Sort - Sorted Data: {quick_sorted_time:.6f} sec, {quick_sorted_memory} bytes"
    )
    print(
        f"Quick Sort - Reverse Sorted Data: {quick_reverse_sorted_time:.6f} sec, {quick_reverse_sorted_memory} bytes"
    )
    print(
        f"Quick Sort - Random Data: {quick_random_time:.6f} sec, {quick_random_memory} bytes\n"
    )

    print()

    print(f"Testing Randomized Quick  Sort on dataset of {size} numbers")

    print(
        f"Randomized Quick  Sort - Sorted Data: {randomized_sorted_time:.6f} sec, {randomized_sorted_memory} bytes"
    )
    print(
        f"Randomized Quick  Sort - Reverse Sorted Data: {randomized_reverse_sorted_time:.6f} sec, {randomized_reverse_sorted_memory} bytes"
    )
    print(
        f"Randomized Quick  Sort - Random Data: {randomized_random_time:.6f} sec, {randomized_random_memory} bytes"
    )

    print()


compare_sorts(10)
compare_sorts(100)
compare_sorts(1000)
compare_sorts(2000)
