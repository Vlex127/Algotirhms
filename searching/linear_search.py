"""
Linear Search Algorithm

Time Complexity:
- Best Case: O(1) - when element is found at first position
- Average Case: O(n) - when element is found in middle position
- Worst Case: O(n) - when element is found at last position or not found

Space Complexity: O(1) - constant space, no additional memory required

Algorithm Description:
Linear Search is the simplest searching algorithm that sequentially checks
each element in the array until the target element is found or the end of
the array is reached. It works on unsorted arrays and doesn't require any
preprocessing.
"""

def linear_search(arr, target):
    """
    Search for a target element in an array using Linear Search
    
    Args:
        arr (list): List of elements to search through
        target: Element to search for
        
    Returns:
        int: Index of the target element if found, -1 otherwise
        
    Time Complexity: O(n) in worst case
    Space Complexity: O(1)
    """
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check if current element matches the target
        if arr[i] == target:
            return i  # Return index if found
    
    # Target not found in the array
    return -1


def linear_search_all(arr, target):
    """
    Find all occurrences of target element in an array
    
    Args:
        arr (list): List of elements to search through
        target: Element to search for
        
    Returns:
        list: List of indices where target element is found
    """
    indices = []
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)  # Add index to results
    
    return indices


def linear_search_count(arr, target):
    """
    Count occurrences of target element in an array
    
    Args:
        arr (list): List of elements to search through
        target: Element to search for
        
    Returns:
        int: Number of occurrences of target element
    """
    count = 0
    
    # Iterate through each element in the array
    for element in arr:
        if element == target:
            count += 1
    
    return count


def linear_search_with_comparator(arr, target, comparator):
    """
    Linear Search with custom comparison function
    
    Args:
        arr (list): List of elements to search through
        target: Element to search for
        comparator (function): Custom comparison function that takes two arguments
                              and returns True if they match
        
    Returns:
        int: Index of the target element if found, -1 otherwise
    """
    for i in range(len(arr)):
        if comparator(arr[i], target):
            return i
    
    return -1


def linear_search_range(arr, start_idx, end_idx, target):
    """
    Linear Search within a specific range of the array
    
    Args:
        arr (list): List of elements to search through
        start_idx (int): Starting index of the search range (inclusive)
        end_idx (int): Ending index of the search range (exclusive)
        target: Element to search for
        
    Returns:
        int: Index of the target element if found, -1 otherwise
    """
    # Validate indices
    if start_idx < 0 or end_idx > len(arr) or start_idx >= end_idx:
        raise ValueError("Invalid range indices")
    
    # Search within the specified range
    for i in range(start_idx, end_idx):
        if arr[i] == target:
            return i
    
    return -1


def linear_search_reverse(arr, target):
    """
    Linear Search from the end of the array (reverse search)
    
    Args:
        arr (list): List of elements to search through
        target: Element to search for
        
    Returns:
        int: Index of the target element if found, -1 otherwise
    """
    # Iterate from the end to the beginning
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
    
    return -1


def linear_search_analysis():
    """
    Provides complexity analysis for Linear Search algorithm
    """
    return {
        'algorithm': 'Linear Search',
        'time_complexity': {
            'best': 'O(1)',
            'average': 'O(n)',
            'worst': 'O(n)'
        },
        'space_complexity': 'O(1)',
        'requires_sorted_data': False,
        'adaptive': False,
        'description': 'Simple sequential search algorithm that checks each element one by one until target is found'
    }


def compare_with_binary_search(arr, target):
    """
    Compare Linear Search performance with Binary Search (for sorted arrays)
    
    Args:
        arr (list): Sorted list of elements
        target: Element to search for
        
    Returns:
        dict: Performance comparison results
    """
    from .binary_search import binary_search
    
    # Linear Search
    import time
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search
    start_time = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start_time
    
    return {
        'array_size': len(arr),
        'target': target,
        'linear_search': {
            'result': linear_result,
            'time': linear_time
        },
        'binary_search': {
            'result': binary_result,
            'time': binary_time
        },
        'speedup': linear_time / binary_time if binary_time > 0 else float('inf')
    }


# Example usage and testing
if __name__ == "__main__":
    # Test the algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 43]
    target = 22
    
    print("Test array:", test_array)
    print(f"Searching for: {target}")
    
    # Basic linear search
    result = linear_search(test_array, target)
    print(f"Linear Search result: {result}")
    
    # Search for non-existent element
    not_found = linear_search(test_array, 100)
    print(f"Search for 100: {not_found}")
    
    # Find all occurrences
    test_with_duplicates = [1, 2, 3, 2, 4, 2, 5]
    all_indices = linear_search_all(test_with_duplicates, 2)
    print(f"\nArray with duplicates: {test_with_duplicates}")
    print(f"All occurrences of 2: {all_indices}")
    
    # Count occurrences
    count = linear_search_count(test_with_duplicates, 2)
    print(f"Count of 2: {count}")
    
    # Range search
    range_result = linear_search_range(test_array, 2, 6, target)
    print(f"Range search (indices 2-6): {range_result}")
    
    # Reverse search
    reverse_result = linear_search_reverse(test_array, target)
    print(f"Reverse search result: {reverse_result}")
    
    # Custom comparator search (case-insensitive string search)
    strings = ["Apple", "Banana", "Cherry", "apple"]
    case_insensitive_result = linear_search_with_comparator(
        strings, "apple", lambda x, y: x.lower() == y.lower()
    )
    print(f"\nCase-insensitive search for 'apple': {case_insensitive_result}")
    
    # Performance comparison with binary search
    sorted_array = sorted(test_array)
    comparison = compare_with_binary_search(sorted_array, target)
    print(f"\nPerformance comparison for array size {len(sorted_array)}:")
    print(f"Linear Search time: {comparison['linear_search']['time']:.6f}s")
    print(f"Binary Search time: {comparison['binary_search']['time']:.6f}s")
    print(f"Speedup: {comparison['speedup']:.2f}x")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = linear_search_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
