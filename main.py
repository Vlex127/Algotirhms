#!/usr/bin/env python3
"""
Main entry point for the Algorithms Repository
Provides testing and demonstration functionality for all algorithms
"""

import argparse
import sys
import time
from typing import List, Any

# Import algorithm categories
from sorting import *
from searching import *
from data_structures import *
from utils.test_runner import TestRunner
from utils.matplotlib_tester import MatplotlibTester


def run_matplotlib_tests(category: str = None):
    """
    Run matplotlib-based performance tests and generate visualizations
    """
    tester = MatplotlibTester()
    
    if category == "sorting" or category is None:
        try:
            print("Running sorting algorithm tests with matplotlib...")
            from sorting.bubble_sort import bubble_sort
            from sorting.quick_sort import quick_sort
            from sorting.merge_sort import merge_sort
            
            algorithms = {
                'Bubble Sort': bubble_sort,
                'Quick Sort': quick_sort,
                'Merge Sort': merge_sort
            }
            
            input_sizes = [10, 50, 100, 200, 500]
            comparison_data = tester.compare_algorithms(algorithms, input_sizes)
            
            # Generate visualizations
            perf_plot = tester.plot_performance_comparison("Sorting Algorithms Performance")
            print(f"Performance plot saved: {perf_plot}")
            
            theoretical_complexities = {
                'Bubble Sort': 'O(n^2)',
                'Quick Sort': 'O(n log n)',
                'Merge Sort': 'O(n log n)'
            }
            
            complexity_plot = tester.plot_complexity_analysis(theoretical_complexities)
            print(f"Complexity analysis plot saved: {complexity_plot}")
            
        except ImportError as e:
            print(f"Skipping sorting tests - import error: {e}")
    
    if category == "searching" or category is None:
        try:
            print("Running searching algorithm tests with matplotlib...")
            from searching.linear_search import linear_search
            from searching.binary_search import binary_search
            
            # Test searching algorithms
            def test_linear_search(arr):
                return linear_search(arr, arr[-1] if arr else None)
            
            def test_binary_search(arr):
                return binary_search(arr, arr[-1] if arr else None)
            
            algorithms = {
                'Linear Search': test_linear_search,
                'Binary Search': test_binary_search
            }
            
            input_sizes = [10, 50, 100, 200, 500, 1000]
            comparison_data = tester.compare_algorithms(algorithms, input_sizes)
            
            perf_plot = tester.plot_performance_comparison("Searching Algorithms Performance")
            print(f"Searching performance plot saved: {perf_plot}")
            
        except ImportError as e:
            print(f"Skipping searching tests - import error: {e}")
    
    return tester.performance_data


def run_algorithm_test(algorithm_name: str, data: List[Any]) -> dict:
    """
    Run a specific algorithm and return performance metrics
    """
    start_time = time.time()
    
    # Algorithm execution logic would go here
    # This is a placeholder for the actual implementation
    
    end_time = time.time()
    
    return {
        'algorithm': algorithm_name,
        'execution_time': end_time - start_time,
        'input_size': len(data),
        'result': None  # Placeholder
    }


def main():
    """
    Main function to handle command line arguments and execute tests
    """
    parser = argparse.ArgumentParser(description='Algorithms Repository Test Runner')
    parser.add_argument('--test-all', action='store_true', help='Test all algorithms')
    parser.add_argument('--test-category', type=str, help='Test specific category')
    parser.add_argument('--test-algorithm', type=str, help='Test specific algorithm')
    parser.add_argument('--analyze-complexity', action='store_true', help='Run complexity analysis')
    parser.add_argument('--matplotlib-tests', action='store_true', help='Run matplotlib performance tests')
    parser.add_argument('--matplotlib-category', type=str, help='Run matplotlib tests for specific category')
    
    args = parser.parse_args()
    
    if args.test_all:
        print("Testing all algorithms...")
        # Implementation for testing all algorithms
    elif args.test_category:
        print(f"Testing category: {args.test_category}")
        # Implementation for testing specific category
    elif args.test_algorithm:
        print(f"Testing algorithm: {args.test_algorithm}")
        # Implementation for testing specific algorithm
    elif args.analyze_complexity:
        print("Running complexity analysis...")
        # Implementation for complexity analysis
    elif args.matplotlib_tests:
        print("Running matplotlib performance tests...")
        run_matplotlib_tests()
    elif args.matplotlib_category:
        print(f"Running matplotlib tests for category: {args.matplotlib_category}")
        run_matplotlib_tests(args.matplotlib_category)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
