"""
Heap Sort Algorithm

Time Complexity:
- Best Case: O(n log n) - always builds heap and extracts elements
- Average Case: O(n log n) - consistent performance
- Worst Case: O(n log n) - always builds heap and extracts elements

Space Complexity: O(1) - sorts in place, no additional space needed

Stability: No - does not maintain relative order of equal elements

Algorithm Description:
Heap Sort uses a binary heap data structure to sort elements. It first builds
a max heap from the input array, then repeatedly extracts the maximum element
and places it at the end of the array.
"""

def heap_sort(arr):
    """
    Sorts an array using the Heap Sort algorithm
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
        
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(1) - sorts in place
    """
    # Make a copy to avoid modifying the original array
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # Build a max heap from the array
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(sorted_arr, n, i)
    
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (largest element) to the end
        sorted_arr[0], sorted_arr[i] = sorted_arr[i], sorted_arr[0]
        
        # Call heapify on the reduced heap
        heapify(sorted_arr, i, 0)
    
    return sorted_arr


def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i
    n is the size of the heap
    i is the root index of the subtree
    
    This function ensures that the subtree rooted at i satisfies the
    max heap property: parent >= children
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index
    
    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort_min_heap(arr):
    """
    Heap Sort implementation using min heap (sorts in ascending order)
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # Build a min heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_min(sorted_arr, n, i)
    
    # Extract elements from the heap one by one
    result = []
    for i in range(n - 1, -1, -1):
        # Move current root (smallest element) to result
        sorted_arr[0], sorted_arr[i] = sorted_arr[i], sorted_arr[0]
        result.append(sorted_arr[i])
        
        # Call heapify on the reduced heap
        heapify_min(sorted_arr, i, 0)
    
    # Reverse the result to get ascending order
    return result[::-1]


def heapify_min(arr, n, i):
    """
    Heapify a subtree for min heap
    Ensures parent <= children
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_min(arr, n, smallest)


def build_max_heap(arr):
    """
    Build a max heap from an unsorted array
    
    Args:
        arr (list): Unsorted array
        
    Returns:
        list: Array representing a max heap
    """
    heap = arr.copy()
    n = len(heap)
    
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(heap, n, i)
    
    return heap


def heap_sort_analysis():
    """
    Provides complexity analysis for Heap Sort algorithm
    """
    return {
        'algorithm': 'Heap Sort',
        'time_complexity': {
            'best': 'O(n log n)',
            'average': 'O(n log n)',
            'worst': 'O(n log n)'
        },
        'space_complexity': 'O(1)',
        'stability': False,
        'in_place': True,
        'adaptive': False,
        'description': 'In-place sorting algorithm that uses binary heap data structure to sort elements in O(n log n) time'
    }


def is_max_heap(arr):
    """
    Check if an array represents a valid max heap
    
    Args:
        arr (list): Array to check
        
    Returns:
        bool: True if array is a valid max heap
    """
    n = len(arr)
    
    # Check each node to ensure heap property
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check left child
        if left < n and arr[i] < arr[left]:
            return False
        
        # Check right child
        if right < n and arr[i] < arr[right]:
            return False
    
    return True


# Example usage and testing
if __name__ == "__main__":
    # Test the algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 43]
    print("Original array:", test_array)
    print("Heap sorted:", heap_sort(test_array))
    print("Min heap sorted:", heap_sort_min_heap(test_array))
    
    # Demonstrate heap building
    print("\nBuilding max heap:")
    max_heap = build_max_heap(test_array)
    print("Max heap:", max_heap)
    print("Is valid max heap:", is_max_heap(max_heap))
    
    # Test with edge cases
    print("\nEdge cases:")
    print("Empty array:", heap_sort([]))
    print("Single element:", heap_sort([42]))
    print("Already sorted:", heap_sort([1, 2, 3, 4, 5]))
    print("Reverse sorted:", heap_sort([5, 4, 3, 2, 1]))
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = heap_sort_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
