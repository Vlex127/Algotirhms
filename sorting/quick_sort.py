"""
Quick Sort Algorithm

Time Complexity:
- Best Case: O(n log n) - when pivot divides array into equal halves
- Average Case: O(n log n) - when pivot divides array reasonably well
- Worst Case: O(n²) - when pivot is always smallest or largest element

Space Complexity:
- O(log n) - for recursive call stack (average case)
- O(n) - for recursive call stack (worst case)

Stability: No - does not maintain relative order of equal elements

Algorithm Description:
Quick Sort is a divide-and-conquer algorithm that picks a pivot element,
partitions the array around the pivot, and recursively sorts the sub-arrays.
"""

def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm (recursive implementation)
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
        
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) average, O(n) worst case
    """
    # Make a copy to avoid modifying the original array
    sorted_arr = arr.copy()
    
    def _quick_sort(low, high):
        """Helper function for recursive quick sort"""
        if low < high:
            # Partition the array and get pivot index
            pivot_index = partition(low, high)
            
            # Recursively sort elements before and after partition
            _quick_sort(low, pivot_index - 1)
            _quick_sort(pivot_index + 1, high)
    
    def partition(low, high):
        """
        Partition function that takes last element as pivot,
        places the pivot element at its correct position in sorted array,
        and places all smaller elements to left of pivot and all greater
        elements to right of pivot
        """
        # Choose the rightmost element as pivot
        pivot = sorted_arr[high]
        
        # Index of smaller element
        i = low - 1
        
        # Compare each element with pivot
        for j in range(low, high):
            if sorted_arr[j] <= pivot:
                # If current element is smaller than or equal to pivot
                i += 1
                # Swap elements
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]
        
        # Swap the pivot element with the greater element at i+1
        sorted_arr[i + 1], sorted_arr[high] = sorted_arr[high], sorted_arr[i + 1]
        
        # Return the position from where partition is done
        return i + 1
    
    # Call the recursive quick sort function
    _quick_sort(0, len(sorted_arr) - 1)
    return sorted_arr


def quick_sort_iterative(arr):
    """
    Iterative implementation of Quick Sort to avoid recursion stack overflow
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # Create a stack for storing sub-array boundaries
    stack = []
    
    # Push initial values to stack
    stack.append((0, n - 1))
    
    # While stack is not empty
    while stack:
        # Pop top pair from stack
        low, high = stack.pop()
        
        if low < high:
            # Partition the array
            pivot_index = partition_iterative(sorted_arr, low, high)
            
            # Push left and right sub-array boundaries to stack
            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))
    
    return sorted_arr


def partition_iterative(arr, low, high):
    """
    Partition function for iterative quick sort
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_randomized(arr):
    """
    Quick Sort with randomized pivot selection to avoid worst-case scenarios
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
    """
    import random
    
    sorted_arr = arr.copy()
    
    def _quick_sort_randomized(low, high):
        if low < high:
            # Randomly choose pivot index
            pivot_index = random.randint(low, high)
            
            # Move pivot to end
            sorted_arr[pivot_index], sorted_arr[high] = sorted_arr[high], sorted_arr[pivot_index]
            
            # Partition and recursively sort
            pi = partition_randomized(sorted_arr, low, high)
            _quick_sort_randomized(low, pi - 1)
            _quick_sort_randomized(pi + 1, high)
    
    def partition_randomized(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    _quick_sort_randomized(0, len(sorted_arr) - 1)
    return sorted_arr


def quick_sort_analysis():
    """
    Provides complexity analysis for Quick Sort algorithm
    """
    return {
        'algorithm': 'Quick Sort',
        'time_complexity': {
            'best': 'O(n log n)',
            'average': 'O(n log n)',
            'worst': 'O(n²)'
        },
        'space_complexity': 'O(log n) average, O(n) worst',
        'stability': False,
        'in_place': True,
        'adaptive': False,
        'description': 'Efficient divide-and-conquer sorting algorithm that uses a pivot element to partition and recursively sort sub-arrays'
    }


# Example usage and testing
if __name__ == "__main__":
    # Test the algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 43]
    print("Original array:", test_array)
    print("Quick sorted:", quick_sort(test_array))
    print("Iterative quick sorted:", quick_sort_iterative(test_array))
    print("Randomized quick sorted:", quick_sort_randomized(test_array))
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = quick_sort_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
