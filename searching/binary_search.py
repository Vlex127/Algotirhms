"""
Binary Search Algorithm

Time Complexity:
- Best Case: O(1) - when target element is found at middle position
- Average Case: O(log n) - when element is found after log n comparisons
- Worst Case: O(log n) - when element is not found or found after log n comparisons

Space Complexity:
- O(1) - for iterative implementation
- O(log n) - for recursive implementation (call stack)

Algorithm Description:
Binary Search is a divide-and-conquer algorithm that works on sorted arrays.
It repeatedly divides the search interval in half by comparing the target
value to the middle element of the array. If the target is less than the
middle element, the search continues in the left half; otherwise, it continues
in the right half.
"""

def binary_search(arr, target):
    """
    Search for a target element in a sorted array using Binary Search (iterative)
    
    Args:
        arr (list): Sorted list of elements to search through
        target: Element to search for
        
    Returns:
        int: Index of the target element if found, -1 otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    # Continue while there are elements to search
    while left <= right:
        # Calculate middle index to avoid overflow
        mid = left + (right - left) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is smaller, ignore right half
        elif arr[mid] > target:
            right = mid - 1
        
        # If target is larger, ignore left half
        else:
            left = mid + 1
    
    # Target not found
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Search for a target element using recursive Binary Search
    
    Args:
        arr (list): Sorted list of elements to search through
        target: Element to search for
        left (int): Left boundary of search interval
        right (int): Right boundary of search interval
        
    Returns:
        int: Index of the target element if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case: if left > right, element not found
    if left > right:
        return -1
    
    # Calculate middle index
    mid = left + (right - left) // 2
    
    # Check if target is present at mid
    if arr[mid] == target:
        return mid
    
    # If target is smaller, search left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # If target is larger, search right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


def binary_search_first_occurrence(arr, target):
    """
    Find the first occurrence of target element in a sorted array with duplicates
    
    Args:
        arr (list): Sorted list of elements (may contain duplicates)
        target: Element to search for
        
    Returns:
        int: Index of the first occurrence of target element, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid  # Store the current position
            right = mid - 1  # Continue searching in left half
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return result


def binary_search_last_occurrence(arr, target):
    """
    Find the last occurrence of target element in a sorted array with duplicates
    
    Args:
        arr (list): Sorted list of elements (may contain duplicates)
        target: Element to search for
        
    Returns:
        int: Index of the last occurrence of target element, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid  # Store the current position
            left = mid + 1  # Continue searching in right half
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return result


def binary_search_count_occurrences(arr, target):
    """
    Count the number of occurrences of target element in a sorted array
    
    Args:
        arr (list): Sorted list of elements (may contain duplicates)
        target: Element to search for
        
    Returns:
        int: Number of occurrences of target element
    """
    first = binary_search_first_occurrence(arr, target)
    if first == -1:
        return 0
    
    last = binary_search_last_occurrence(arr, target)
    return last - first + 1


def binary_search_insert_position(arr, target):
    """
    Find the position where target should be inserted to maintain sorted order
    
    Args:
        arr (list): Sorted list of elements
        target: Element to find insert position for
        
    Returns:
        int: Index where target should be inserted
    """
    left = 0
    right = len(arr)
    
    # Binary search for insert position
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


def binary_search_closest_element(arr, target):
    """
    Find the element closest to target in a sorted array
    
    Args:
        arr (list): Sorted list of elements
        target: Element to find closest match for
        
    Returns:
        tuple: (index_of_closest_element, closest_element_value)
    """
    if not arr:
        return -1, None
    
    # Binary search to find the closest element
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # At this point, left is the insertion point
    # Check neighbors to find the closest element
    if left >= len(arr):
        return len(arr) - 1, arr[-1]
    elif left == 0:
        return 0, arr[0]
    else:
        # Compare arr[left-1] and arr[left] to find closer to target
        if abs(arr[left - 1] - target) <= abs(arr[left] - target):
            return left - 1, arr[left - 1]
        else:
            return left, arr[left]


def binary_search_analysis():
    """
    Provides complexity analysis for Binary Search algorithm
    """
    return {
        'algorithm': 'Binary Search',
        'time_complexity': {
            'best': 'O(1)',
            'average': 'O(log n)',
            'worst': 'O(log n)'
        },
        'space_complexity': 'O(1) iterative, O(log n) recursive',
        'requires_sorted_data': True,
        'adaptive': False,
        'description': 'Efficient divide-and-conquer search algorithm that works on sorted arrays by repeatedly dividing search interval in half'
    }


def is_binary_search_applicable(arr):
    """
    Check if Binary Search is applicable to the given array
    
    Args:
        arr (list): Array to check
        
    Returns:
        dict: Analysis of Binary Search applicability
    """
    if not arr:
        return {'applicable': True, 'reason': 'Empty array'}
    
    # Check if array is sorted
    is_sorted = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    return {
        'applicable': is_sorted,
        'sorted': is_sorted,
        'size': len(arr),
        'reason': 'Array is sorted' if is_sorted else 'Array must be sorted for Binary Search'
    }


# Example usage and testing
if __name__ == "__main__":
    # Test the algorithm
    test_array = [11, 12, 22, 25, 34, 43, 50, 64, 76, 88, 90]
    targets = [22, 43, 100]
    
    print("Test array:", test_array)
    
    for target in targets:
        print(f"\nSearching for: {target}")
        
        # Iterative binary search
        result = binary_search(test_array, target)
        print(f"Iterative Binary Search: {result}")
        
        # Recursive binary search
        result_rec = binary_search_recursive(test_array, target)
        print(f"Recursive Binary Search: {result_rec}")
    
    # Test with duplicates
    test_with_duplicates = [1, 2, 2, 2, 3, 4, 5, 5, 6]
    target_duplicate = 2
    
    print(f"\nArray with duplicates: {test_with_duplicates}")
    print(f"First occurrence of {target_duplicate}: {binary_search_first_occurrence(test_with_duplicates, target_duplicate)}")
    print(f"Last occurrence of {target_duplicate}: {binary_search_last_occurrence(test_with_duplicates, target_duplicate)}")
    print(f"Count of {target_duplicate}: {binary_search_count_occurrences(test_with_duplicates, target_duplicate)}")
    
    # Test insert position
    insert_targets = [0, 2, 7]
    print(f"\nInsert position tests:")
    for target in insert_targets:
        pos = binary_search_insert_position(test_array, target)
        print(f"Insert {target} at position: {pos}")
    
    # Test closest element
    closest_targets = [23, 45, 89]
    print(f"\nClosest element tests:")
    for target in closest_targets:
        idx, val = binary_search_closest_element(test_array, target)
        print(f"Closest to {target}: {val} at index {idx}")
    
    # Check applicability
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nApplicability check:")
    print("Sorted array:", is_binary_search_applicable(test_array))
    print("Unsorted array:", is_binary_search_applicable(unsorted_array))
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = binary_search_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
