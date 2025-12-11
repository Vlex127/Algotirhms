"""
Bubble Sort Algorithm

Time Complexity:
- Best Case: O(n) - when array is already sorted
- Average Case: O(n²) - when elements are in random order
- Worst Case: O(n²) - when array is sorted in reverse order

Space Complexity: O(1) - constant space, sorting in place

Stability: Yes - maintains relative order of equal elements

Algorithm Description:
Bubble Sort repeatedly steps through the list, compares adjacent elements
and swaps them if they are in the wrong order. The pass through the list
is repeated until the list is sorted.
"""

def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
        
    Time Complexity: O(n²) in worst and average cases
    Space Complexity: O(1) - sorts in place
    """
    n = len(arr)
    
    # Make a copy to avoid modifying the original array
    sorted_arr = arr.copy()
    
    # Outer loop for number of passes
    for i in range(n):
        # Flag to optimize - if no swaps occur, array is sorted
        swapped = False
        
        # Inner loop for comparisons in each pass
        # Last i elements are already in place after i passes
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap if elements are in wrong order
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return sorted_arr


def optimized_bubble_sort(arr):
    """
    Optimized version of Bubble Sort with early termination
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
    """
    n = len(arr)
    sorted_arr = arr.copy()
    
    # Track the last position where a swap occurred
    while n > 1:
        new_n = 0
        
        # Only iterate up to the last swap position
        for i in range(1, n):
            if sorted_arr[i - 1] > sorted_arr[i]:
                # Swap elements
                sorted_arr[i - 1], sorted_arr[i] = sorted_arr[i], sorted_arr[i - 1]
                new_n = i  # Update last swap position
        
        # Reduce the range for next pass
        n = new_n
    
    return sorted_arr


def bubble_sort_analysis():
    """
    Provides complexity analysis for Bubble Sort algorithm
    """
    return {
        'algorithm': 'Bubble Sort',
        'time_complexity': {
            'best': 'O(n)',
            'average': 'O(n²)',
            'worst': 'O(n²)'
        },
        'space_complexity': 'O(1)',
        'stability': True,
        'in_place': True,
        'adaptive': True,  # Takes advantage of existing order
        'description': 'Simple comparison-based sorting algorithm that repeatedly swaps adjacent elements if they are in wrong order'
    }


# Example usage and testing
if __name__ == "__main__":
    # Test the algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    print("Sorted array:", bubble_sort(test_array))
    print("Optimized sorted array:", optimized_bubble_sort(test_array))
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = bubble_sort_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
