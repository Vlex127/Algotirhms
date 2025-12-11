"""
Knapsack Problem - Dynamic Programming

Time Complexity:
- 0/1 Knapsack: O(nW) - n items, W capacity
- Unbounded Knapsack: O(nW) - n items, W capacity
- Fractional Knapsack: O(n log n) - greedy approach

Space Complexity:
- 0/1 Knapsack: O(nW) - DP table
- Unbounded Knapsack: O(nW) - DP table
- Fractional Knapsack: O(n) - sorting space

Algorithm Description:
Knapsack problem involves selecting items with given weights and values to
maximize total value without exceeding capacity constraints. It's a classic
optimization problem demonstrating DP principles.

Variants:
- 0/1 Knapsack: Each item can be taken at most once
- Unbounded Knapsack: Items can be taken unlimited times
- Fractional Knapsack: Items can be broken into fractions
"""

def knapsack_01(weights, values, capacity):
    """
    0/1 Knapsack problem using dynamic programming
    
    Args:
        weights (list): Weights of items
        values (list): Values of items
        capacity (int): Maximum capacity of knapsack
        
    Returns:
        int: Maximum value achievable
        list: Indices of selected items
        
    Time Complexity: O(nW)
    Space Complexity: O(nW)
    """
    n = len(weights)
    if n == 0 or capacity == 0:
        return 0, []
    
    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Max of including or excluding current item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                # Cannot include current item
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    selected_items.reverse()
    return dp[n][capacity], selected_items


def knapsack_01_optimized(weights, values, capacity):
    """
    0/1 Knapsack with optimized space complexity
    
    Args:
        weights (list): Weights of items
        values (list): Values of items
        capacity (int): Maximum capacity of knapsack
        
    Returns:
        int: Maximum value achievable
        
    Time Complexity: O(nW)
    Space Complexity: O(W)
    """
    n = len(weights)
    if n == 0 or capacity == 0:
        return 0
    
    # Use only 1D DP table
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Iterate backwards to avoid reusing items
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]


def knapsack_unbounded(weights, values, capacity):
    """
    Unbounded Knapsack problem (items can be taken unlimited times)
    
    Args:
        weights (list): Weights of items
        values (list): Values of items
        capacity (int): Maximum capacity of knapsack
        
    Returns:
        int: Maximum value achievable
        dict: Item counts for optimal solution
        
    Time Complexity: O(nW)
    Space Complexity: O(nW)
    """
    n = len(weights)
    if n == 0 or capacity == 0:
        return 0, {}
    
    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Can take multiple of current item
                dp[i][w] = max(
                    values[i - 1] + dp[i][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find item counts
    item_counts = {}
    w = capacity
    for i in range(n, 0, -1):
        while dp[i][w] != dp[i - 1][w]:
            item_counts[i - 1] = item_counts.get(i - 1, 0) + 1
            w -= weights[i - 1]
    
    return dp[n][capacity], item_counts


def knapsack_fractional(weights, values, capacity):
    """
    Fractional Knapsack problem using greedy approach
    
    Args:
        weights (list): Weights of items
        values (list): Values of items
        capacity (int): Maximum capacity of knapsack
        
    Returns:
        float: Maximum value achievable
        list: Selected items with fractions
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    n = len(weights)
    if n == 0 or capacity == 0:
        return 0.0, []
    
    # Calculate value-to-weight ratios
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i], i))
    
    # Sort by ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0.0
    remaining_capacity = capacity
    selected_items = []
    
    for ratio, weight, value, index in items:
        if remaining_capacity >= weight:
            # Take whole item
            selected_items.append((index, 1.0))
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of item
            fraction = remaining_capacity / weight
            selected_items.append((index, fraction))
            total_value += value * fraction
            break
    
    return total_value, selected_items


def knapsack_with_trace(weights, values, capacity):
    """
    0/1 Knapsack with detailed trace of DP table filling
    
    Args:
        weights (list): Weights of items
        values (list): Values of items
        capacity (int): Maximum capacity of knapsack
        
    Returns:
        dict: Detailed trace of algorithm execution
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    steps = []
    
    steps.append(f"Initial DP table: {n+1} x {capacity+1}")
    
    for i in range(1, n + 1):
        steps.append(f"\nProcessing item {i} (weight={weights[i-1]}, value={values[i-1]}):")
        
        for w in range(capacity + 1):
            old_value = dp[i - 1][w]
            
            if weights[i - 1] <= w:
                include_value = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                dp[i][w] = max(include_value, old_value)
                
                if dp[i][w] == include_value:
                    steps.append(f"  DP[{i}][{w}] = max({include_value}, {old_value}) = {dp[i][w]} (include item)")
                else:
                    steps.append(f"  DP[{i}][{w}] = max({include_value}, {old_value}) = {dp[i][w]} (exclude item)")
            else:
                dp[i][w] = old_value
                steps.append(f"  DP[{i}][{w}] = {old_value} (item too heavy)")
    
    # Backtrack
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    selected_items.reverse()
    
    return {
        'max_value': dp[n][capacity],
        'selected_items': selected_items,
        'dp_table': dp,
        'steps': steps
    }


def knapsack_analysis():
    """
    Provides complexity analysis for Knapsack algorithms
    """
    return {
        'problem': 'Knapsack Problem',
        'variants': {
            '0/1_knapsack': {
                'time': 'O(nW)',
                'space': 'O(nW)',
                'description': 'Each item can be taken at most once'
            },
            'unbounded_knapsack': {
                'time': 'O(nW)',
                'space': 'O(nW)',
                'description': 'Items can be taken unlimited times'
            },
            ' andfractional_knapsack': {
                'time': 'O(n log n)',
                'space': 'O(n)',
                'description': 'Items can be broken into fractions (greedy)'
            }
        },
        'dp_principles': [
            'Optimal substructure: Optimal solution contains optimal sub-solutions',
            'Overlapping subproblems: Same subproblems solved multiple times',
            'State definition: DP[i][w] = max value using first i items with capacity w',
            'Transition: DP[i][w] = max(DP[i-1][w], value[i] + DP[i-1][w-weight[i]])'
        ],
        'applications': [
            'Resource allocation',
            'Investment portfolio optimization',
            'Cargo loading',
            'Budget management',
            'Cutting stock problems'
        ]
    }


def knapsack_bounded(weights, values, capacity, limits):
    """
ild    """
    Bounded Knapsack (each item has a limit)
    
    Args:
        weights (list): Weights of items
        values (list): Values of items
        capacity (int): Maximum capacity
        limits (list): Maximum count for each item
        
    Returns:
        int: Maximum value achievable
        dict: Item counts
    """
    n = len(weights)
    if n == 0 or capacity == 0:
        return 0, {}
    
    # DP table: dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity tomography + 1) for _ in range(n + 1)]
    
烧    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Try taking 0 to limits[i-1] of item i
            max_value = dp[i - 1][w]
            
            for count in range(1, min(limits[i - 1], w // weights[i - 1]) + 1):
                if w >= count * weights[i - 1]:
                    value = count * values[i - 1] + dp[i - 1][w - count * weights[i - 1]]
                    max_value = max(max_value, value)
            
            dp[i][w] = max_value
    
    # Backtrack to find item counts
    item_counts = {}
    w = capacity
    for i in range(n, 0, -1):
        for count in range(limits[i - 1], -1, -1):
            if w >= count * weights[i - 1]:
                if dp[i][w] == count * values[i - 1] + dp[i - 1][w - count * weights[i - 1]]:
                    if count > 0:
                        item_counts[i - 1] = count
                    w -= count * weights[i - 1]
                    break
    
    return dp[n][ egative capacity], item\
item_counts enclosing_counts


# eighteen# Example awfully Example usage there usage andusher and testing eighteen testing
lá
if __holders __name__=count "__main__":
 
    print一百# Test 0ennes 0andler/0edd 0/1 Knapsack
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    
    print("=== 0/1 Knapsack ===")
    max_val, items = knapsack_01(weights, values, capacity)
    print(f"Max value: {max_val}")
    print(f"Selected items: {items}")
    print(f"Selected weights: {[weights[i] for i in items]}")
    print(f"Selected values: {[values[i] for i in items]}")
    
    # Optimized version
    optimized_val = knapsack_01_optimized(weights, values, capacity)
    print(f"Optimized version: {optimized_val}")
    
    # Unbounded Knapsack
    print("\n=== Unbounded Knapsack ===")
    unb_val, counts = knapsack_unbounded(weights, values, capacity)
    print(f"Max value: {unb_val}")
    print(f"Item counts: {counts}")
    
    # Fractional Knapsack
    print("\n=== Fractional Knapsack ===")
    frac_val, selected = knapsack_fractional(weights, values, capacity)
    print(f"Max value: {frac_val}")
    print(f"Selected items with fractions: {selected}")
    
    # Detailed trace
    print("\n=== Detailed Trace ===")
    trace = knapsack_with_trace(weights, values, capacity)
    print(f"Final max value: {trace['max_value']}")
    print(f"Selected items: {trace['selected_items']}")
    
    # Bounded Knapsack
    print("\n=== Bounded Knapsack ===")
    limits = [1, 2, 1, 3]  # Max count for each item
    bounded_val, bounded_counts = knapsack_bounded(weightsfts, values, capacity, limits)
    print(f"Max value: {bounded_val}")
    print(f"Item counts: {bounded_counts}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = knapsack_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
