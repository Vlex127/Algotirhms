"""
Matrix Chain Multiplication - Dynamic Programming

Time Complexity:
- Recursive: O(2^n) - exponential
- Memoization: O(n³) - cubic
- Tabulation: O(n³) - cubic

Space Complexity:
- Recursive: O(n) - recursion stack
- Memoization: O(n²) - memo table + recursion stack
- Tabulation: O(n²) - DP table

Algorithm Description:
Matrix Chain Multiplication finds the optimal way to multiply a chain of
matrices by determining the parenthesization that minimizes the total number
of scalar multiplications. It's a classic DP problem demonstrating optimal
parenthesization and matrix multiplication optimization.

Applications:
- Compiler optimization
- Database query optimization
- Image processing
- Scientific computing
- Operations research
"""

def matrix_chain_recursive(dimensions, i, j):
    """
    Simple recursive matrix chain multiplication (inefficient)
    
    Args:
        dimensions (list): List of matrix dimensions [p0, p1, p2, ..., pn]
                         where matrix i has dimensions pi-1 x pi
        i (int): Starting matrix index
        j (int): Ending matrix index
        
    Returns:
        int: Minimum number of scalar multiplications
        
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    if i == j:
        return 0
    
    min_multiplications = float('inf')
    
    # Try all possible splits
    for k in range(i, j):
        multiplications = (
            matrix_chain_recursive(dimensions, i, k) +
            matrix_chain_recursive(dimensions, k + 1, j) +
            dimensions[i - 1] * dimensions[k] * dimensions[j]
        )
        
        if multiplications < min_multiplications:
            min_multiplications = multiplications
    
    return min_multiplications


def matrix_chain_memoization(dimensions):
    """
    Matrix Chain Multiplication with memoization (top-down DP)
    
    Args:
        dimensions (list): List of matrix dimensions
        
    Returns:
        int: Minimum number of scalar multiplications
        
    Time Complexity: O(n³)
    Space Complexity: O(n²)
    """
    n = len(dimensions) - 1  # Number of matrices
    memo = {}
    
    def matrix_chain_helper(i, j):
        if i == j:
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        min_multiplications = float('inf')
        
        for k in range(i, j):
            multiplications = (
                matrix_chain_helper(i, k) +
                matrix_chain_helper(k + 1, j) +
                dimensions[i - 1] * dimensions[k] * dimensions[j]
            )
            
            if multiplications < min_multiplications:
                min_multiplications = multiplications
        
        memo[(i, j)] = min_multiplications
        return min_multiplications
    
    return matrix_chain_helper(1, n)


def matrix_chain_order(dimensions):
    """
    Matrix Chain Multiplication with tabulation (bottom-up DP)
    
    Args:
        dimensions (list): List of matrix dimensions
        
    Returns:
        tuple: (m, s) where m is cost matrix and s is split matrix
        
    Time Complexity: O(n³)
    Space Complexity: O(n²)
    """
    n = len(dimensions) - 1  # Number of matrices
    
    # m[i][j] = minimum number of scalar multiplications
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    # s[i][j] = split point that achieved optimal solution
    s = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Set diagonal to 0 (single matrix multiplication)
    for i in range(1, n + 1):
        m[i][i] = 0
    
    # l is chain length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            
            # Try all possible splits
            for k in range(i, j):
                cost = (
                    m[i][k] + m[k + 1][j] +
                    dimensions[i - 1] * dimensions[k] * dimensions[j]
                )
                
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    
    return m, s


def optimal_parenthesization(s, i, j):
    """
    Reconstruct optimal parenthesization from split matrix
    
    Args:
        s (list): Split matrix from matrix_chain_order
        i (int): Starting matrix index
        j (int): Ending matrix index
        
    Returns:
        str: Optimal parenthesization string
    """
    if i == j:
        return f"A{i}"
    else:
        return f"({optimal_parenthesization(s, i, s[i][j])} × {optimal_parenthesization(s, s[i][j] + 1, j)})"


def matrix_chain_with_solution(dimensions):
    """
    Complete solution including optimal parenthesization
    
    Args:
        dimensions (list): List of matrix dimensions
        
    Returns:
        dict: Complete solution with cost and parenthesization
        
    Time Complexity: O(n³)
    Space Complexity: O(n²)
    """
    m, s = matrix_chain_order(dimensions)
    n = len(dimensions) - 1
    
    optimal_cost = m[1][n]
    optimal_parens = optimal_parenthesization(s, 1, n)
    
    return {
        'optimal_cost': optimal_cost,
        'optimal_parenthesization': optimal_parens,
        'cost_matrix': m,
        'split_matrix': s,
        'num_matrices': n
    }


def matrix_chain_with_trace(dimensions):
    """
    Matrix Chain Multiplication with detailed trace
    
    Args:
        dimensions (list): List of matrix dimensions
        
    Returns:
        dict: Detailed trace of algorithm execution
    """
    n = len(dimensions) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    steps = []
    
    steps.append(f"Number of matrices: {n}")
    steps.append(f"Dimensions: {dimensions}")
    
    for i in range(1, n + 1):
        m[i][i] = 0
    
    # l is chain length
    for l in range(2, n + 1):
        steps.append(f"\nProcessing chain length {l}:")
        
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            
            steps.append(f"  Computing optimal cost for matrices A{i}..A{j}:")
            
            for k in range(i, j):
                cost = (
                    m[i][k] + m[k + 1][j] +
                    dimensions[i - 1] * dimensions[k] * dimensions[j]
                )
                
                steps.append(f"    Split at k={k}: cost = {m[i][k]} + {m[k+1][j]} + {dimensions[i-1]}×{dimensions[k]}×{dimensions[j]} = {cost}")
                
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
                    steps.append(f"    New minimum: {cost} (split at {k})")
            
            steps.append(f"  Optimal cost for A{i}..A{j}: {m[i][j]} (split at {s[i][j]})")
    
    optimal_parens = optimal_parenthesization(s, 1, n)
    
    return {
        'optimal_cost': m[1][n],
        'optimal_parenthesization': optimal_parens,
        'cost_matrix': m,
        'split_matrix': s,
        'steps': steps
    }


def print_matrix_chain_solution(dimensions):
    """
    Print a formatted solution for matrix chain multiplication
    
    Args:
        dimensions (list): List of matrix dimensions
    """
    solution = matrix_chain_with_solution(dimensions)
    
    print("Matrix Chain Multiplication Solution:")
    print(f"Dimensions: {dimensions}")
    print(f"Number of matrices: {solution['num_matrices']}")
    print(f"Optimal cost: {solution['optimal_cost']} scalar multiplications")
    print(f"Optimal parenthesization: {solution['optimal_parenthesization']}")
    
    # Print matrix dimensions
    print("\nMatrix dimensions:")
    for i in range(1, len(dimensions)):
        print(f"A{i}: {dimensions[i-1]} × {dimensions[i]}")


def matrix_chain_analysis():
    """
    Provides complexity analysis for Matrix Chain Multiplication algorithms
    """
    return {
        'problem': 'Matrix Chain Multiplication',
        'recursive': {
            'time': 'O(2^n)',
            'space': 'O(n)',
            'description': 'Simple recursive approach with exponential time'
        },
        'memoization': {
            'time': 'O(n³)',
            'space': 'O(n²)',
            'description': 'Top-down DP with memoization'
        },
        'tabulation': {
            'time': 'O(n³)',
            'space': 'O(n²)',
            'description': 'Bottom-up DP with tabulation'
        },
        'dp_principles': [
            'Optimal substructure: Optimal solution contains optimal sub-solutions',
            'Overlapping subproblems: Same subproblems solved multiple times',
            'State definition: M[i][j] = minimum cost for multiplying Ai..Aj',
            'Transition: M[i][j] = min(M[i][k] + M[k+1][j] + pi-1*pk*pj)'
        ],
        'applications': [
            'Compiler optimization',
            'Database query optimization',
            'Image processing pipelines',
            'Scientific computing',
            'Operations research',
            'Parallel computing'
        ]
    }


def compare_matrix_chain_methods(dimensions):
    """
    Compare different matrix chain multiplication methods
    
    Args:
        dimensions (list): List of matrix dimensions
        
    Returns:
        dict: Performance comparison results
    """
    import time
    
    n = len(dimensions) - 1
    
    methods = {
        'memoization': matrix_chain_memoization,
        'tabulation': lambda dims: matrix_chain_order(dims)[0][1][n]
    }
    
    results = {}
    
    for method_name, method_func in methods.items():
        start_time = time.time()
        result = method_func(dimensions)
        end_time = time.time()
        
        results[method_name] = {
            'time': end_time - start_time,
            'result': result
        }
    
    # Complete solution
    start_time = time.time()
    complete_solution = matrix_chain_with_solution(dimensions)
    end_time = time.time()
    
    results['complete_solution'] = {
        'time': end_time - start_time,
        'result': complete_solution['optimal_cost'],
        'parenthesization': complete_solution['optimal_parenthesization']
    }
    
    return results


# Example usage and testing
if __name__ == "__main__":
    # Example dimensions: A1(10x30), A2(30x5), A3(5x60), A4(60x20)
    dimensions = [10, 30, 5, 60, 20]
    
    print("=== Matrix Chain Multiplication ===")
    
    # Print formatted solution
    print_matrix_chain_solution(dimensions)
    
    # Different methods
    print(f"\nMemoization result: {matrix_chain_memoization(dimensions)}")
    
    m, s = matrix_chain_order(dimensions)
    print(f"Tabulation result: {m[1][len(dimensions)-1]}")
    
    # Optimal parenthesization
    optimal_parens = optimal_parenthesization(s, 1, len(dimensions) - 1)
    print(f"Optimal parenthesization: {optimal_parens}")
    
    # Detailed trace
    print("\n=== Detailed Trace ===")
    trace = matrix_chain_with_trace(dimensions)
    print(f"Final result: {trace['optimal_cost']}")
    print(f"Parenthesization: {trace['optimal_parenthesization']}")
    
    # Performance comparison
    print("\n=== Performance Comparison ===")
    comparison = compare_matrix_chain_methods(dimensions)
    for method, result in comparison.items():
        if 'parenthesization' in result:
            print(f"{method}: {result['time']:.6f}s,; result:; parenthes . . . . . .  . .
           ; result: {.
            print(f.
           人员进行
        .
        .
员的

       . . . . . . . . . . . . . ..
   . . . . ..
. . . . . . . . . . . . . . . . . . .tractor

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .; result: 
    ..
   . . .; result: {result.
        ./disable/; result: {result['result']}")
        else:.
            print(f"{method}: {result['time']:.6f}s, result: {result['result']}")
    
    # Test with different dimensions
    print("\n=== Different Dimensions Test ===")
    dimensions2 = [30, 35, 15, 5, 10, 20, 25]
    solution2 = matrix_chain_with_solution(dimensions2)
    print(f"Dimensions: {dimensions2}")
    print(f"Optimal cost: {solution2['optimal_cost']}")
    print(f"Parenthesization: {solution2['optimal_parenthesization']}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = matrix_chain_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
