"""
Divide and Conquer Algorithms Module

This module contains divide and conquer algorithms with their implementations,
complexity analysis, and testing utilities.

Available Algorithms:
- Merge Sort
- Quick Sort
- Binary Search
- Strassen's Matrix Multiplication
- Closest Pair of Points
"""

from .merge_sort import merge_sort, merge_sort_iterative, merge_sort_in_place
from .quick_sort import quick_sort, quick_sort_iterative, quick_sort_randomized
from .binary_search import binary_search_iterative, binary_search_recursive
from .strassen import strassen_matrix_multiplication
from .closest_pair import closest_pair_of_points

__all__ = [
    'merge_sort', 'merge_sort_iterative', 'merge_sort_in_place',
    'quick_sort', 'quick_sort_iterative', 'quick_sort_randomized',
    'binary_search_iterative', 'binary_search_recursive',
    'strassen_matrix_multiplication',
    'closest_pair_of_points'
]