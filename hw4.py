import random
import timeit
from typing import Callable, List

def insertion_sort(arr: List[int]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def time_algorithm(algorithm: Callable, arr: List[int]) -> float:
    start_time = timeit.default_timer()
    algorithm(arr)
    end_time = timeit.default_timer()
    return end_time - start_time

def compare_algorithms():
    sizes = [100, 1000, 10000, 100000]
    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]
        print(f"Array size: {size}")
        for algorithm in [sorted, insertion_sort, merge_sort]:
            arr_copy = arr.copy()
            time = time_algorithm(algorithm, arr_copy)
            print(f"{algorithm.__name__}: {time} seconds")

compare_algorithms()