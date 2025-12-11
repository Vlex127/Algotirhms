"""
Searching Algorithms Module

This module contains various searching algorithms with their implementations,
complexity analysis, and testing utilities.

Available Algorithms:
- Linear Search
- Binary Search
- Interpolation Search
- Exponential Search
"""

from .linear_search import linear_search
from .binary_search import binary_search
from .interpolation_search import interpolation_search
from .exponential_search import exponential_search

__all__ = [
    'linear_search',
    'binary_search',
    'interpolation_search',
    'exponential_search'
]
