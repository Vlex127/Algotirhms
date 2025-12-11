"""
Divide and Conquer Algorithms Module

This module contains divide and conquer algorithms with their implementations,
complexity analysis, and testing utilities.

Available Algorithms:
- Merge Sort
"""

from .merge_sort import merge_sort, merge_sort_iterative, merge_sort_in_place

__all__ = [
    'merge_sort', 'merge_sort_iterative', 'merge_sort_in_place'
]