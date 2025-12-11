"""
Binary Search - Divide and Conquer Algorithm

Time Complexity: O(log n)
Space Complexity: O(1) - iterative, O(log n) - recursive

Algorithm Description:
Binary search efficiently finds the position of a target value in a sorted
array by repeatedly dividing the search interval in half.
"""

def binary_search_iterative(arr, target):
    """
    Iterative binary search implementation
    
    Args:
        arr: Sorted array
        target: Value to search for
        
    Returns:
        int: Index of target, -1 if not found
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive binary search implementation
    
    Args:
        arr: Sorted array
        target: Value to search for
        left: Left boundary (default 0)
        right: Right boundary (default len(arr) - 1)
        
    Returns:
        int: Index of target, -1 if not found
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_first_occurrence(arr, target):
    """
    Find first occurrence of target in sorted array
    
    Args:
        arr: Sorted array (may contain duplicates)
        target: Value to search for
        
    Returns:
        int: Index of first occurrence, -1 if not found
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_last_occurrence(arr, target):
    """
    Find last occurrence of target in sorted array
    
    Args:
        arr: Sorted array (may contain duplicates)
        target: Value to search for
        
    Returns:
        int: Index of last occurrence, -1 if not found
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_count_occurrences(arr, target):
    """
    Count occurrences of target in sorted array
    
    Args:
        arr: Sorted array (may contain duplicates)
        target: Value to count
        
    Returns:
        int: Number of occurrences
    """
    first = binary_search_first_occurrence(arr, target)
    if first == -1:
        return 0
    
    last = binary_search_last_occurrence(arr, target)
    return last - first + 1


if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    
    # Basic binary search
    index = binary_search_iterative(arr, target)
    print(f"Iterative: {target} found at index {index}")
    
    index = binary_search_recursive(arr, target)
    print(f"Recursive: {target} found at index {index}")
    
    # With duplicates
    arr_with_duplicates = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    
    first = binary_search_first_occurrence(arr_with_duplicates, target)
    last = binary_search_last_occurrence(arr_with_duplicates, target)
    count = binary_search_count_occurrences(arr_with_duplicates, target)
    
    print(f"First occurrence of {target}: {first}")
    print(f"Last occurrence of {target}: {last}")
    print(f"Count of {target}: {count}")
