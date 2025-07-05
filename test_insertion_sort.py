"""
Test suite for the insertion sort algorithm implementation.

This module contains comprehensive test cases to verify the correctness
of the insertion sort algorithm for decreasing order sorting.

Author: Dheeraj Kollapaneni
Course: MSCS532 - Analysis of Algorithms
"""

import unittest
from typing import List
from insertion_sort import insertion_sort_decreasing


class TestInsertionSort(unittest.TestCase):
    """Test cases for the insertion sort algorithm."""
    
    def test_basic_array(self):
        """Test with a basic unsorted array."""
        arr = [5, 2, 4, 6, 1, 3]
        expected = [6, 5, 4, 3, 2, 1]
        result = insertion_sort_decreasing(arr)
        self.assertEqual(result, expected)
    
    def test_already_sorted_decreasing(self):
        """Test with an array already sorted in decreasing order."""
        arr = [9, 7, 5, 3, 1]
        expected = [9, 7, 5, 3, 1]
        result = insertion_sort_decreasing(arr)
        self.assertEqual(result, expected)
    
    def test_already_sorted_increasing(self):
        """Test with an array sorted in increasing order (worst case)."""
        arr = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        result = insertion_sort_decreasing(arr)
        self.assertEqual(result, expected)
    
    def test_single_element(self):
        """Test with a single element array."""
        arr = [42]
        expected = [42]
        result = insertion_sort_decreasing(arr)
        self.assertEqual(result, expected)
    
    def test_empty_array(self):
        """Test with an empty array."""
        arr = []
        expected = []
        result = insertion_sort_decreasing(arr)
        self.assertEqual(result, expected)
    
    def test_duplicate_elements(self):
        """Test with duplicate elements."""
        arr = [5, 3, 5, 2, 3, 1, 5]
        expected = [5, 5, 5, 3, 3, 2, 1]
        result = insertion_sort_decreasing(arr)
        self.assertEqual(result, expected)
    
    def test_all_same_elements(self):
        """Test with all identical elements."""
        arr = [7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7]
        result = insertion_sort_decreasing(arr)
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        arr = [-1, -5, -2, -8, -3]
        expected = [-1, -2, -3, -5, -8]
        result = insertion_sort_decreasing(arr)
        self.assertEqual(result, expected)
    
    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        arr = [3, -1, 4, -2, 0, 5, -3]
        expected = [5, 4, 3, 0, -1, -2, -3]
        result = insertion_sort_decreasing(arr)
        self.assertEqual(result, expected)
    
    def test_large_numbers(self):
        """Test with large numbers."""
        arr = [1000000, 500000, 2000000, 100000]
        expected = [2000000, 1000000, 500000, 100000]
        result = insertion_sort_decreasing(arr)
        self.assertEqual(result, expected)
    
    def test_original_array_unchanged(self):
        """Test that the original array is not modified."""
        original = [5, 2, 4, 6, 1, 3]
        arr_copy = original.copy()
        insertion_sort_decreasing(arr_copy)
        self.assertEqual(original, [5, 2, 4, 6, 1, 3])
    
    def test_decreasing_order_property(self):
        """Test that the result is actually in decreasing order."""
        test_arrays = [
            [64, 34, 25, 12, 22, 11, 90],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 8, 7, 6, 5, 4, 3, 2, 1],
            [5, 5, 5, 5],
            [100, 1, 50, 25, 75]
        ]
        
        for arr in test_arrays:
            result = insertion_sort_decreasing(arr)
            # Check that each element is >= the next element
            for i in range(len(result) - 1):
                self.assertGreaterEqual(result[i], result[i + 1],
                    f"Array not in decreasing order: {result}")


def run_performance_analysis():
    """
    Analyze the performance characteristics of the insertion sort algorithm.
    """
    import time
    import random
    
    print("\nPerformance Analysis")
    print("=" * 50)
    
    # Test different array sizes
    sizes = [10, 100, 500, 1000]
    
    for size in sizes:
        # Generate random array
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        # Measure sorting time
        start_time = time.time()
        insertion_sort_decreasing(arr)
        end_time = time.time()
        
        duration = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Size {size:4d}: {duration:.4f} ms")


def main():
    """
    Run all tests and performance analysis.
    """
    print("Running Insertion Sort Tests...")
    print("=" * 40)
    
    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run performance analysis
    run_performance_analysis()


if __name__ == "__main__":
    main()
