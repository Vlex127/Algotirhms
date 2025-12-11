"""
Exponential Search Algorithm

Time Complexity:
- Best Case: O(1) - when target is found at first position
- Average Case: O(log n) - when element is found after log n comparisons
- Worst Case: O(log n) - when element is not found or found after log n comparisons

Space Complexity: O(1) - constant space, no additional memory required

Algorithm Description:
Exponential Search is a searching algorithm for sorted arrays that works by
first finding the range where the target element might be present, and then
performing binary search within that range. It's particularly useful for
unbounded or infinite sorted arrays.

The algorithm works in two phases:
1. Find the range by exponentially increasing the search window
2. Perform binary search within the found range
"""

def exponential_search(arr, target):
    """
    Search for a target element using Exponential Search
    
    Args:
        arr (list): Sorted list of elements to search through
        target: Element to search for
        
    Returns:
        int: Index of the target element if found, -1 otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1
    
    n = len(arr)
    
    # If target is at first position
    if arr[0] == target:
        return 0
    
    # Find range for binary search by repeated doubling
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2
    
    # Call binary search for the found range
    return binary_search_in_range(arr, target, i // 2, min(i, n - 1))


def binary_search_in_range(arr, target, left, right):
    """
    Perform binary search within a specific range
    
    Args:
        arr (list): Sorted list of elements
        target: Element to search for
        left (int): Left boundary of search range
        right (int): Right boundary of search range
        
    Returns:
        int: Index of the target element if found, -1 otherwise
    """
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def exponential_search_recursive(arr, target, i=1):
    """
    Recursive implementation of Exponential Search
    
    Args:
        arr (list): Sorted list of elements to search through
        target: Element to search for
        i (int): Current power of 2 for range expansion
        
    Returns:
        int: Index of the target element if found, -1 otherwise
    """
    if not arr:
        return -1
    
    n = len(arr)
    
    # Base case: if i exceeds array size
    if i >= n:
        return binary_search_in_range(arr, target, i // 2, n - 1)
    
    # If target is found at current position
    if arr[i] == target:
        return i
    
    # If current element is greater than target, perform binary search
    if arr[i] > target:
        return binary_search_in_range(arr, target, i // 2, i)
    
    # Recursively search with doubled range
    return exponential_search_recursive(arr, target, i * 2)


def exponential_search_first_occurrence(arr, target):
    """
    Find the first occurrence of target element in array with duplicates
    
    Args:
        arr (list): Sorted list of elements (may contain duplicates)
        target: Element to search for
        
    Returns:
        int: Index of the first occurrence of target element, -1 if not found
    """
    if not arr:
        return -1
    
    n = len(arr)
    
    # If target is at first position
    if arr[0] == target:
        return 0
    
    # Find range
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2
    
    # Perform binary search for first occurrence in the found range
    return binary_search_first_in_range(arr, target, i // 2, min(i, n - 1))


def binary_search_first_in_range(arr, target, left, right):
    """
    Binary search for first occurrence within a range
    
    Args:
        arr (list): Sorted list of elements
        target: Element to search for
        left (int): Left boundary of search range
        right (int): Right boundary of search range
        
    Returns:
        int: Index of the first occurrence of target element
    """
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def exponential_search_with_steps(arr, target):
    """
    Exponential Search with step-by-step tracking
    
    Args:
        arr (list): Sorted list of elements to search through
        target: Element to search for
        
    Returns:
        dict: Search result with step information
    """
    if not arr:
        return {'found': False, 'index': -1, 'steps': [], 'message': 'Empty array'}
    
    steps = []
    n = len(arr)
    
    # Step 1: Check first element
    steps.append(f"Checking first element: arr[0] = {arr[0]}")
    if arr[0] == target:
        return {
            'found': True,
            'index': 0,
            'steps': steps,
            'message': 'Found at first position'
        }
    
    # Step 2: Find range exponentially
    i = 1
    while i < n and arr[i] <= target:
        steps.append(f"Checking arr[{i}] = {arr[i]} (range: {i//2} to {i})")
        if arr[i] == target:
            return {
                'found': True,
                'index': i,
                'steps': steps,
                'message': 'Found during range expansion'
            }
        i = i * 2
    
    # Step 3: Binary search in found range
    left = i // 2
    right = min(i, n - 1)
    steps.append(f"Performing binary search in range [{left}, {right}]")
    
    result = binary_search_in_range(arr, target, left, right)
    
    if result != -1:
        steps.append(f"Found at index {result}")
        return {
            'found': True,
            'index': result,
            'steps': steps,
            'message': 'Found in binary search phase'
        }
    else:
        steps.append("Target not found in range")
        return {
            'found': False,
            'index': -1,
            'steps': steps,
            'message': 'Target not found'
        }


def exponential_search_analysis():
    """
    Provides complexity analysis for Exponential Search algorithm
    """
    return {
        'algorithm': 'Exponential Search',
        'time_complexity': {
            'best': 'O(1)',
            'average': 'O(log n)',
            'worst': 'O(log n)'
        },
        'space_complexity': 'O(1)',
        'requires_sorted_data': True,
        'optimal_for_unbounded': True,
        'description': 'Two-phase search algorithm that first finds search range exponentially, then performs binary search within that range'
    }


def compare_exponential_with_binary(arr, target):
    """
    Compare Exponential Search with Binary Search performance
    
    Args:
        arr (list): Sorted array to search in
        target: Element to search for
        
    Returns:
        dict: Performance comparison results
    """
    import time
    from .binary_search import binary_search
    
    # Binary Search
    start_time = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start_time
    
    # Exponential Search
    start_time = time.time()
    exponential_result = exponential_search(arr, target)
    exponential_time = time.time() - start_time
    
    return {
        'array_size': len(arr),
        'target': target,
        'binary_search': {
            'result': binary_result,
            'time': binary_time
        },
        'exponential_search': {
            'result': exponential_result,
            'time': exponential_time
        },
        'speedup': binary_time / exponential_time if exponential_time > 0 else float('inf')
    }


# Example usage and testing
if __name__ == "__main__":
    # Test the algorithm
    test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    targets = [1, 7, 15, 23, 29, 30]
    
    print("Test array:", test_array)
    
    for target in targets:
        print(f"\nSearching for: {target}")
        
        # Basic exponential search
        result = exponential_search(test_array, target)
        print(f"Exponential Search: {result}")
        
        # With step tracking
        detailed_result = exponential_search_with_steps(test_array, target)
        print(f"Steps: {len(detailed_result['steps'])}")
        for step in detailed_result['steps']:
            print(f"  {step}")
    
    # Test with duplicates
    test_with_duplicates = [1, 2, 2, 2, 3, 4, 5, 5, 6]
    target_duplicate = 2
    
    print(f"\nArray with duplicates: {test_with_duplicates}")
    print(f"First occurrence of {target_duplicate}: {exponential_search_first_occurrence(test_with_duplicates, target_duplicate)}")
    
    # Performance comparison
    large_array = list(range(0, 10000, 2))  # [0, 2, 4, ..., 9998]
    comparison = compare_exponential_with_binary(large_array, 5000)
    
    print(f"\nPerformance comparison for array size {len(large_array)}:")
    print(f"Binary Search time: {comparison['binary_search']['time']:.6f}s")
    print(f"Exponential Search time: {comparison['exponential_search']['time']:.6f}s")
    print(f"Speedup: {comparison['speedup']:.2f}x")
    
    # Test recursive version
    print(f"\nRecursive Exponential Search:")
    for target in [7, 15, 23]:
        result = exponential_search_recursive(test_array, target)
        print(f"Target {target}: {result}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = exponential_search_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
