#!/usr/bin/env python3
"""
Matplotlib Testing Examples

Example scripts demonstrating how to use the matplotlib testing functionality
for visualizing algorithm performance and complexity.
"""

import sys
import os
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.matplotlib_tester import MatplotlibTester


def test_sorting_visualization():
    """
    Test and visualize sorting algorithm performance
    """
    print("=== Testing Sorting Algorithms ===")
    
    try:
        from sorting.bubble_sort import bubble_sort
        from sorting.quick_sort import quick_sort
        from sorting.merge_sort import merge_sort
        
        tester = MatplotlibTester()
        
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
        
        return comparison_data
        
    except ImportError as e:
        print(f"Error importing sorting algorithms: {e}")
        return None


def test_searching_visualization():
    """
    Test and visualize searching algorithm performance
    """
    print("\n=== Testing Searching Algorithms ===")
    
    try:
        from searching.linear_search import linear_search
        from searching.binary_search import binary_search
        
        tester = MatplotlibTester()
        
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
        
        return comparison_data
        
    except ImportError as e:
        print(f"Error importing searching algorithms: {e}")
        return None


def test_data_structure_performance():
    """
    Test and visualize data structure operations
    """
    print("\n=== Testing Data Structure Performance ===")
    
    try:
        from data_structures.stack import Stack
        from data_structures.queue import Queue
        
        # Test stack operations
        def test_stack_operations(arr):
            n = len(arr)
            stack = Stack()
            for i in range(n):
                stack.push(i)
            for i in range(n):
                stack.pop()
            return n
        
        # Test queue operations
        def test_queue_operations(arr):
            n = len(arr)
            queue = Queue()
            for i in range(n):
                queue.enqueue(i)
            for i in range(n):
                queue.dequeue()
            return n
        
        algorithms = {
            'Stack Operations': test_stack_operations,
            'Queue Operations': test_queue_operations
        }
        
        input_sizes = [100, 500, 1000, 2000, 5000]
        
        # Create a custom tester that doesn't use the generator
        tester = MatplotlibTester()
        comparison_data = {}
        
        for name, algorithm in algorithms.items():
            print(f"Benchmarking {name}...")
            times = []
            results = []
            
            for size in input_sizes:
                # Generate test data (simple array)
                test_data = list(range(size))
                
                # Time the algorithm
                start_time = time.time()
                result = algorithm(test_data)
                end_time = time.time()
                
                execution_time = end_time - start_time
                times.append(execution_time)
                results.append(result)
            
            comparison_data[name] = {
                'input_sizes': input_sizes,
                'execution_times': times,
                'results': results
            }
        
        tester.performance_data = comparison_data
        
        perf_plot = tester.plot_performance_comparison("Data Structure Operations Performance")
        print(f"Data structure performance plot saved: {perf_plot}")
        
        return comparison_data
        
    except ImportError as e:
        print(f"Error importing data structures: {e}")
        return None


def create_comprehensive_report():
    """
    Create a comprehensive performance report with all visualizations
    """
    print("\n=== Creating Comprehensive Performance Report ===")
    
    tester = MatplotlibTester()
    
    # Test all categories
    sorting_data = test_sorting_visualization()
    searching_data = test_searching_visualization()
    data_struct_data = test_data_structure_performance()
    
    # Generate comprehensive report
    report_path = tester.generate_test_report()
    print(f"\nComprehensive test report generated: {report_path}")
    
    return report_path


if __name__ == "__main__":
    print("Running matplotlib testing examples...")
    
    # Run individual tests
    test_sorting_visualization()
    test_searching_visualization()
    test_data_structure_performance()
    
    # Create comprehensive report
    create_comprehensive_report()
    
    print("\nMatplotlib testing completed!")
    print("Check the 'test_results' directory for generated plots and reports.")
