"""
Fractional Knapsack Problem - Greedy Algorithm

Time Complexity: O(n log n) - for sorting items by value/weight ratio
Space Complexity: O(n) - for storing items

Algorithm Description:
Fractional knapsack allows taking fractions of items. The greedy approach
selects items based on their value-to-weight ratio, taking as much as possible
of the item with the highest ratio until the knapsack is full.
"""

def fractional_knapsack(values, weights, capacity):
    """
    Solve fractional knapsack problem
    
    Args:
        values: List of item values
        weights: List of item weights
        capacity: Maximum knapsack capacity
        
    Returns:
        float: Maximum value achievable
    """
    # Calculate value/weight ratios
    items = []
    for i in range(len(values)):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i], i))
    
    # Sort by ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0
    remaining_capacity = capacity
    
    for ratio, value, weight, index in items:
        if remaining_capacity >= weight:
            # Take whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            break
    
    return total_value


if __name__ == "__main__":
    # Example usage
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    
    max_value = fractional_knapsack(values, weights, capacity)
    print(f"Maximum value: {max_value}")
