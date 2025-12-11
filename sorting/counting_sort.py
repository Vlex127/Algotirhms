"""
Counting Sort Algorithm

Time Complexity:
- Best Case: O(n + k) - where n is number of elements, k is range
- Average Case: O(n + k) - linear time complexity
- Worst Case: O(n + k) - linear time complexity

Space Complexity: O(k) - requires additional space for counting array

Stability: Yes - maintains relative order of equal elements

Algorithm Description:
Counting Sort is a non-comparison based sorting algorithm that works by
counting the number of occurrences of each distinct element in the input
array. It is efficient when the range of input values (k) is not significantly
greater than the number of elements (n).

Note: Counting Sort only works with non-negative integers or can be adapted
for other types with known ranges.
"""

def counting_sort(arr):
    """
    Sorts an array using the Counting Sort algorithm
    
    Args:
        arr (list): List of non-negative integers to be sorted
        
    Returns:
        list: Sorted list in ascending order
        
    Time Complexity: O(n + k) where n is array length, k is range of values
    Space Complexity: O(k) for counting array
    """
    if not arr:
        return []
    
    # Make a copy to avoid modifying the original array
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # Find the maximum element in the array
    max_element = max(sorted_arr)
    
    # Create a count array to store the count of each element
    # Size is max_element + 1 to include the max element
    count = [0] * (max_element + 1)
    
    # Store the count of each element
    for i in range(n):
        count[sorted_arr[i]] += 1
    
    # Store the cumulative count
    # This will help in placing the elements at the correct position
    for i in range(1, max_element + 1):
        count[i] += count[i - 1]
    
    # Build the output array
    # Traverse the input array in reverse order to maintain stability
    output = [0] * n
    for i in range(n - 1, -1, -1):
        output[count[sorted_arr[i]] - 1] = sorted_arr[i]
        count[sorted_arr[i]] -= 1
    
    return output


def counting_sort_min_max(arr, min_val=None, max_val=None):
    """
    Counting Sort with specified minimum and maximum values for optimization
    
    Args:
        arr (list): List of integers to be sorted
        min_val (int, optional): Minimum value in the array
        max_val (int, optional): Maximum value in the array
        
    Returns:
        list: Sorted list in ascending order
    """
    if not arr:
        return []
    
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # Find min and max if not provided
    if min_val is None:
        min_val = min(sorted_arr)
    if max_val is None:
        max_val = max(sorted_arr)
    
    # Create count array with size based on range
    range_size = max_val - min_val + 1
    count = [0] * range_size
    
    # Count occurrences
    for num in sorted_arr:
        count[num - min_val] += 1
    
    # Calculate cumulative count
    for i in range(1, range_size):
        count[i] += count[i - 1]
    
    # Build output array
    output = [0] * n
    for i in range(n - 1, -1, -1):
        num = sorted_arr[i]
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return output


def counting_sort_negative(arr):
    """
    Counting Sort adapted to handle negative numbers
    
    Args:
        arr (list): List of integers (can include negative numbers)
        
    Returns:
        list: Sorted list in ascending order
    """
    if not arr:
        return []
    
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # Find minimum and maximum values
    min_val = min(sorted_arr)
    max_val = max(sorted_arr)
    
    # Create count array
    range_size = max_val - min_val + 1
    count = [0] * range_size
    
    # Count occurrences
    for num in sorted_arr:
        count[num - min_val] += 1
    
    # Calculate cumulative count
    for i in range(1, range_size):
        count[i] += count[i - 1]
    
    # Build output array
    output = [0] * n
    for i in range(n - 1, -1, -1):
        num = sorted_arr[i]
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return output


def counting_sort_string(arr):
    """
    Counting Sort adapted for strings (sorts characters)
    
    Args:
        arr (list): List of strings to be sorted
        
    Returns:
        list: Sorted list of strings
    """
    if not arr:
        return []
    
    # Flatten all characters
    all_chars = []
    for s in arr:
        all_chars.extend(s)
    
    if not all_chars:
        return arr.copy()
    
    # Sort characters
    sorted_chars = counting_sort([ord(c) for c in all_chars])
    
    # Reconstruct strings (this is a simplified approach)
    # For proper string sorting, you'd need radix sort
    return sorted(arr)  # Fallback to built-in sort for comparison


def counting_sort_analysis():
    """
    Provides complexity analysis for Counting Sort algorithm
    """
    return {
        'algorithm': 'Counting Sort',
        'time_complexity': {
            'best': 'O(n + k)',
            'average': 'O(n + k)',
            'worst': 'O(n + k)'
        },
        'space_complexity': 'O(k)',
        'stability': True,
        'in_place': False,
        'adaptive': False,
        'description': 'Non-comparison based sorting algorithm that counts occurrences of each element for linear-time sorting when range is limited'
    }


def is_counting_sort_efficient(arr):
    """
    Determine if Counting Sort would be efficient for the given array
    
    Args:
        arr (list): Input array
        
    Returns:
        dict: Analysis of efficiency
    """
    if not arr:
        return {'efficient': False, 'reason': 'Empty array'}
    
    n = len(arr)
    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1
    
    # Counting Sort is efficient when k is not much larger than n
    efficiency_ratio = k / n
    
    return {
        'efficient': efficiency_ratio <= 10,  # Rule of thumb
        'ratio': efficiency_ratio,
        'n': n,
        'k': k,
        'reason': f'Range/size ratio is {efficiency_ratio:.2f} (<= 10 is recommended)'
    }


# Example usage and testing
if __name__ == "__main__":
    # Test the algorithm with positive integers
    test_array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 43]
    print("Original array:", test_array)
    print("Counting sorted:", counting_sort(test_array))
    
    # Test with negative numbers
    test_negative = [-5, -10, 0, 5, 10, -3, 8, -1]
    print("\nArray with negatives:", test_negative)
    print("Counting sorted (with negatives):", counting_sort_negative(test_negative))
    
    # Test efficiency analysis
    print("\nEfficiency Analysis:")
    efficiency = is_counting_sort_efficient(test_array)
    for key, value in efficiency.items():
        print(f"{key}: {value}")
    
    # Test with different ranges
    small_range = [1, 2, 3, 2, 1, 4, 3, 2, 1]
    large_range = [1, 1000, 500, 2000, 1500, 3000]
    
    print("\nSmall range array:", small_range)
    print("Efficiency:", is_counting_sort_efficient(small_range))
    
    print("\nLarge range array:", large_range)
    print("Efficiency:", is_counting_sort_efficient(large_range))
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = counting_sort_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
