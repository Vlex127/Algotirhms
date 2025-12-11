"""
Interpolation Search Algorithm

Time Complexity:
- Best Case: O(log log n) - when elements are uniformly distributed
- Average Case: O(log log n) - when elements are uniformly distributed
- Worst Case: O(n) - when elements are not uniformly distributed

Space Complexity: O(1) - constant space, no additional memory required

Algorithm Description:
Interpolation Search is an improved variant of Binary Search for uniformly
distributed sorted arrays. Instead of always checking the middle element,
it estimates the position of the target value based on the values at the
current boundaries. This makes it more efficient for uniformly distributed
data but can degrade to O(n) in worst cases.

Formula: position = low + ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])
"""

def interpolation_search(arr, target):
    """
    Search for a target element using Interpolation Search
    
    Args:
        arr (list): Sorted list of uniformly distributed elements
        target: Element to search for
        
    Returns:
        int: Index of the target element if found, -1 otherwise
        
    Time Complexity: O(log log n) average, O(n) worst case
    Space Complexity: O(1)
    """
    if not arr:
        return -1
    
    low = 0
    high = len(arr) - 1
    
    # Continue while target is within the range and low <= high
    while low <= high and target >= arr[low] and target <= arr[high]:
        # If low and high are the same element
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        # Calculate the probing position using interpolation formula
        # The formula estimates the position based on value distribution
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        
        # Check if calculated position is valid
        if pos < low or pos > high:
            break
        
        # Check if target is found at the calculated position
        if arr[pos] == target:
            return pos
        
        # If target is larger, search in the right part
        elif arr[pos] < target:
            low = pos + 1
        
        # If target is smaller, search in the left part
        else:
            high = pos - 1
    
    # Target not found
    return -1


def interpolation_search_recursive(arr, target, low=0, high=None):
    """
    Recursive implementation of Interpolation Search
    
    Args:
        arr (list): Sorted list of uniformly distributed elements
        target: Element to search for
        low (int): Left boundary of search interval
        high (int): Right boundary of search interval
        
    Returns:
        int: Index of the target element if found, -1 otherwise
    """
    if high is None:
        high = len(arr) - 1
    
    # Base cases
    if low > high or target < arr[low] or target > arr[high]:
        return -1
    
    if low == high:
        return low if arr[low] == target else -1
    
    # Calculate position using interpolation formula
    pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
    
    # Check if position is valid
    if pos < low or pos > high:
        return -1
    
    # Check if target is found
    if arr[pos] == target:
        return pos
    elif arr[pos] < target:
        return interpolation_search_recursive(arr, target, pos + 1, high)
    else:
        return interpolation_search_recursive(arr, target, low, pos - 1)


def interpolation_search_first_occurrence(arr, target):
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
    
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                result = low
            break
        
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        
        if pos < low or pos > high:
            break
        
        if arr[pos] == target:
            result = pos
            high = pos - 1  # Continue searching in left half
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return result


def interpolation_search_with_bounds_check(arr, target):
    """
    Interpolation Search with additional bounds checking and safety measures
    
    Args:
        arr (list): Sorted list of elements
        target: Element to search for
        
    Returns:
        dict: Search result with additional information
    """
    if not arr:
        return {'found': False, 'index': -1, 'iterations': 0, 'message': 'Empty array'}
    
    low = 0
    high = len(arr) - 1
    iterations = 0
    max_iterations = 2 * len(arr).bit_length()  # Prevent infinite loops
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        iterations += 1
        
        if iterations > max_iterations:
            return {
                'found': False, 
                'index': -1, 
                'iterations': iterations,
                'message': 'Maximum iterations exceeded'
            }
        
        if low == high:
            if arr[low] == target:
                return {
                    'found': True,
                    'index': low,
                    'iterations': iterations,
                    'message': 'Found at single element'
                }
            break
        
        # Check for division by zero
        if arr[high] == arr[low]:
            break
        
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        
        # Validate position
        if pos < low or pos > high:
            break
        
        if arr[pos] == target:
            return {
                'found': True,
                'index': pos,
                'iterations': iterations,
                'message': 'Found successfully'
            }
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return {
        'found': False,
        'index': -1,
        'iterations': iterations,
        'message': 'Target not found'
    }


def is_uniformly_distributed(arr):
    """
    Check if array elements are approximately uniformly distributed
    
    Args:
        arr (list): Sorted array to check
        
    Returns:
        dict: Analysis of uniformity
    """
    if len(arr) < 2:
        return {'uniform': True, 'reason': 'Array too small to determine'}
    
    # Calculate differences between consecutive elements
    differences = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    
    # Calculate mean and standard deviation of differences
    mean_diff = sum(differences) / len(differences)
    variance = sum((diff - mean_diff) ** 2 for diff in differences) / len(differences)
    std_dev = variance ** 0.5
    
    # Check if standard deviation is small relative to mean
    # This indicates uniform distribution
    coefficient_of_variation = std_dev / mean_diff if mean_diff > 0 else float('inf')
    
    return {
        'uniform': coefficient_of_variation < 0.5,  # Threshold for uniformity
        'coefficient_of_variation': coefficient_of_variation,
        'mean_difference': mean_diff,
        'std_deviation': std_dev,
        'reason': f'CV = {coefficient_of_variation:.3f} (< 0.5 indicates uniform distribution)'
    }


def interpolation_search_analysis():
    """
    Provides complexity analysis for Interpolation Search algorithm
    """
    return {
        'algorithm': 'Interpolation Search',
        'time_complexity': {
            'best': 'O(log log n)',
            'average': 'O(log log n)',
            'worst': 'O(n)'
        },
        'space_complexity': 'O(1)',
        'requires_sorted_data': True,
        'uniform_distribution_required': True,
        'description': 'Improved search algorithm that estimates position based on value distribution, optimal for uniformly distributed data'
    }


def compare_search_algorithms(arr, target):
    """
    Compare performance of different search algorithms
    
    Args:
        arr (list): Sorted array to search in
        target: Element to search for
        
    Returns:
        dict: Performance comparison results
    """
    import time
    from .binary_search import binary_search
    from .linear_search import linear_search
    
    results = {}
    
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    results['linear_search'] = {'result': linear_result, 'time': linear_time}
    
    # Binary Search
    start_time = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start_time
    results['binary_search'] = {'result': binary_result, 'time': binary_time}
    
    # Interpolation Search
    start_time = time.time()
    interpolation_result = interpolation_search(arr, target)
    interpolation_time = time.time() - start_time
    results['interpolation_search'] = {'result': interpolation_result, 'time': interpolation_time}
    
    # Calculate speedups
    if binary_time > 0:
        results['interpolation_vs_binary'] = binary_time / interpolation_time
    if linear_time > 0:
        results['interpolation_vs_linear'] = linear_time / interpolation_time
    
    return results


# Example usage and testing
if __name__ == "__main__":
    # Test with uniformly distributed data
    uniform_array = list(range(0, 1000, 10))  # [0, 10, 20, ..., 990]
    targets = [50, 250, 500, 750, 999]
    
    print("Uniform array:", uniform_array[:10], "...", uniform_array[-10:])
    
    for target in targets:
        print(f"\nSearching for: {target}")
        
        # Basic interpolation search
        result = interpolation_search(uniform_array, target)
        print(f"Interpolation Search: {result}")
        
        # With bounds checking
        detailed_result = interpolation_search_with_bounds_check(uniform_array, target)
        print(f"Detailed result: {detailed_result}")
    
    # Test with non-uniform data
    non_uniform_array = [1, 2, 3, 100, 101, 102, 1000, 1001, 1002]
    target_non_uniform = 100
    
    print(f"\nNon-uniform array: {non_uniform_array}")
    print(f"Searching for {target_non_uniform}: {interpolation_search(non_uniform_array, target_non_uniform)}")
    
    # Test uniformity analysis
    print(f"\nUniformity analysis:")
    uniform_analysis = is_uniformly_distributed(uniform_array)
    print("Uniform array:", uniform_analysis)
    
    non_uniform_analysis = is_uniformly_distributed(non_uniform_array)
    print("Non-uniform array:", non_uniform_analysis)
    
    # Performance comparison
    large_uniform = list(range(0, 10000, 5))
    comparison = compare_search_algorithms(large_uniform, 2500)
    
    print(f"\nPerformance comparison for array size {len(large_uniform)}:")
    for algorithm, result in comparison.items():
        if isinstance(result, dict):
            print(f"{algorithm}: {result['time']:.6f}s (result: {result['result']})")
        else:
            print(f"{algorithm}: {result:.2f}x speedup")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = interpolation_search_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
