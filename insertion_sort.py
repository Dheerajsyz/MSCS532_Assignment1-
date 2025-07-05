"""
MSCS532 Assignment 1 - Insertion Sort Algorithm (Decreasing Order)

This module implements the Insertion Sort algorithm to sort arrays in 
monotonically decreasing order, based on Chapter 2 of "Introduction to Algorithms".

Author: Dheeraj kollapaneni
Course: MSCS532 - Analysis of Algorithms
"""

from typing import List


def insertion_sort_decreasing(arr: List[int]) -> List[int]:
    """
    Sorts an array in monotonically decreasing order using insertion sort.
    
    The algorithm works by building a sorted array one element at a time.
    For each element, it finds the correct position in the already sorted
    portion and inserts it there.
    
    Args:
        arr (List[int]): The array to be sorted
        
    Returns:
        List[int]: The sorted array in decreasing order
        
    Time Complexity: O(n²) worst case, O(n) best case
    Space Complexity: O(1) - sorts in place
    """
    # Make a copy to avoid modifying the original array
    sorted_arr = arr.copy()
    
    # Start from the second element (index 1)
    for i in range(1, len(sorted_arr)):
        # Current element to be inserted into sorted portion
        key = sorted_arr[i]
        
        # Index of the last element in sorted portion
        j = i - 1
        
        # Move elements that are smaller than key to the right
        # This is the key change for decreasing order: we use < instead of >
        while j >= 0 and sorted_arr[j] < key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        
        # Insert the key at its correct position
        sorted_arr[j + 1] = key
    
    return sorted_arr


def print_array(arr: List[int], label: str = "") -> None:
    """
    Helper function to print an array with optional label.
    
    Args:
        arr (List[int]): Array to print
        label (str): Optional label to print before the array
    """
    if label:
        print(f"{label}: {arr}")
    else:
        print(arr)


def main():
    """
    Main function to demonstrate the insertion sort algorithm.
    """
    print("Insertion Sort (Decreasing Order)")
    print("=" * 55)
    
    # Test arrays
    test_arrays = [
        [5, 2, 4, 6, 1, 3],
        [31, 41, 59, 26, 41, 58],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [42],
        [],
        [7, 7, 7, 7],
        [100, 50, 25, 75, 10, 90]
    ]
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\nTest Case {i}:")
        print_array(arr, "Original")
        sorted_arr = insertion_sort_decreasing(arr)
        print_array(sorted_arr, "Sorted  ")
        
        # Verify the sort is correct (decreasing order)
        is_sorted = all(sorted_arr[i] >= sorted_arr[i+1] 
                       for i in range(len(sorted_arr)-1))
        print(f"Correctly sorted: {is_sorted}")


if __name__ == "__main__":
    main()
