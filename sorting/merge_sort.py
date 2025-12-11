"""
Merge Sort Algorithm

Time Complexity:
- Best Case: O(n log n) - always divides array in half
- Average Case: O(n log n) - consistent performance
- Worst Case: O(n log n) - always divides array in half

Space Complexity: O(n) - requires additional space for merging

Stability: Yes - maintains relative order of equal elements

Algorithm Description:
Merge Sort is a divide-and-conquer algorithm that divides the array into
two halves, recursively sorts them, and then merges the two sorted halves.
"""

def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm (recursive implementation)
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
        
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(n) for auxiliary array
    """
    # Base case: array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2
    
    # Recursively sort first and second halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merge two sorted arrays into a single sorted array
    
    Args:
        left (list): First sorted sub-array
        right (list): Second sorted sub-array
        
    Returns:
        list: Merged sorted array
    """
    merged = []
    left_index = 0
    right_index = 0
    
    # Traverse both arrays and insert smaller element into merged array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Copy remaining elements of left array, if any
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    # Copy remaining elements of right array, if any
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged


def merge_sort_iterative(arr):
    """
    Iterative implementation of Merge Sort (bottom-up approach)
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr.copy()
    
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # Start with sub-array size 1 and double in each iteration
    size = 1
    while size < n:
        # Merge sub-arrays of current size
        for left_start in range(0, n, 2 * size):
            mid = min(left_start + size, n)
            right_end = min(left_start + 2 * size, n)
            
            # Merge arr[left_start:mid] and arr[mid:right_end]
            left_part = sorted_arr[left_start:mid]
            right_part = sorted_arr[mid:right_end]
            
            # Merge and place back in the array
            merged = merge(left_part, right_part)
            sorted_arr[left_start:left_start + len(merged)] = merged
        
        size *= 2
    
    return sorted_arr


def merge_sort_inplace(arr):
    """
    In-place Merge Sort implementation (reduces space complexity but increases time complexity)
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
    """
    sorted_arr = arr.copy()
    
    def merge_inplace(start, mid, end):
        """Merge two sorted sub-arrays in place"""
        left = sorted_arr[start:mid]
        right = sorted_arr[mid:end]
        
        i = j = 0
        k = start
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_arr[k] = left[i]
                i += 1
            else:
                sorted_arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            sorted_arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            sorted_arr[k] = right[j]
            j += 1
            k += 1
    
    def merge_sort_helper(start, end):
        """Helper function for recursive in-place merge sort"""
        if end - start <= 1:
            return
        
        mid = (start + end) // 2
        merge_sort_helper(start, mid)
        merge_sort_helper(mid, end)
        merge_inplace(start, mid, end)
    
    merge_sort_helper(0, len(sorted_arr))
    return sorted_arr


def merge_sort_analysis():
    """
    Provides complexity analysis for Merge Sort algorithm
    """
    return {
        'algorithm': 'Merge Sort',
        'time_complexity': {
            'best': 'O(n log n)',
            'average': 'O(n log n)',
            'worst': 'O(n log n)'
        },
        'space_complexity': 'O(n)',
        'stability': True,
        'in_place': False,
        'adaptive': False,
        'description': 'Stable divide-and-conquer sorting algorithm that recursively divides array and merges sorted halves'
    }


# Example usage and testing
if __name__ == "__main__":
    # Test the algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 43]
    print("Original array:", test_array)
    print("Merge sorted:", merge_sort(test_array))
    print("Iterative merge sorted:", merge_sort_iterative(test_array))
    print("In-place merge sorted:", merge_sort_inplace(test_array))
    
    # Test with duplicate elements to check stability
    test_with_duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("\nArray with duplicates:", test_with_duplicates)
    print("Merge sorted (stable):", merge_sort(test_with_duplicates))
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = merge_sort_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
