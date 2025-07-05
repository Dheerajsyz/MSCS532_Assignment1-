# MSCS532 Assignment 1 - Insertion Sort (Decreasing Order)

## Project Description
This project implements the Insertion Sort algorithm modified to sort arrays in monotonically decreasing order (largest to smallest).

## Algorithm Overview
Insertion Sort is a simple sorting algorithm that builds the final sorted array one element at a time. It works by taking elements from the unsorted portion and inserting them into their correct position in the sorted portion.

**Time Complexity:** O(n²) in the worst case, O(n) in the best case
**Space Complexity:** O(1) - in-place sorting algorithm

## Files Structure
- `insertion_sort.py` - Main implementation of the insertion sort algorithm
- `test_insertion_sort.py` - Test cases and examples
- `README.md` - This documentation file

## How to Run
```bash
# Run the main implementation
python insertion_sort.py

# Run the tests
python test_insertion_sort.py
```

## Algorithm Implementation
The insertion sort algorithm has been modified to sort in decreasing order by changing the comparison operator. Instead of moving elements that are greater than the key to the right, we move elements that are smaller than the key.

## Assignment Requirements
- Implement Insertion Sort for decreasing order
- Comprehensive test suite with test cases
- Performance analysis included
