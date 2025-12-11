"""
Fibonacci Sequence - Dynamic Programming

Time Complexity:
- Recursive: O(2^n) - exponential time
- Memoization: O(n) - linear time
- Tabulation: O(n) - linear time
- Matrix Exponentiation: O(log n) - logarithmic time

Space Complexity:
- Recursive: O(n) - recursion stack
- Memoization: O(n) - memo table + recursion stack
- Tabulation: O(n) - DP table
- Matrix Exponentiation: O(log n) - recursion stack

Algorithm Description:
Fibonacci sequence is a classic dynamic programming problem where each number
is the sum of the two preceding ones. It demonstrates the power of DP by
avoiding redundant calculations through memoization or tabulation.

Formula: F(n) = F(n-1) + F(n-2), with F(0) = 0, F(1) = 1
"""

def fibonacci_recursive(n):
    """
    Simple recursive Fibonacci implementation (inefficient)
    
    Args:
        n (int): The nth Fibonacci number to compute
        
    Returns:
        int: The nth Fibonacci number
        
    Time Complexity: O(2^n) - exponential
    Space Complexity: O(n) - recursion stack
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoization(n, memo=None):
    """
    Fibonacci with memoization (top-down DP)
    
    Args:
        n (int): The nth Fibonacci number to compute
        memo (dict): Memoization dictionary
        
    Returns:
        int: The nth Fibonacci number
        
    Time Complexity: O(n) - linear
    Space Complexity: O(n) - memo table + recursion stack
    """
    if memo is None:
        memo = {}
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
        return memo[n]


def fibonacci_tabulation(n):
    """
    Fibonacci with tabulation (bottom-up DP)
    
    Args:
        n (int): The nth Fibonacci number to compute
        
    Returns:
        int: The nth Fibonacci number
        
    Time Complexity: O(n) - linear
    Space Complexity: O(n) - DP table
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Create DP table
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    # Fill the table
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_optimized(n):
    """
    Optimized Fibonacci using only O(1) space
    
    Args:
        n (int): The nth Fibonacci number to compute
        
    Returns:
        int: The nth Fibonacci number
        
    Time Complexity: O(n) - linear
    Space Complexity: O(1) - constant space
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    prev, curr = 0, 1
    
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def fibonacci_matrix(n):
    """
    Fibonacci using matrix exponentiation
    
    Args:
        n (int): The nth Fibonacci number to compute
        
    Returns:
        int: The nth Fibonacci number
        
    Time Complexity: O(log n) - logarithmic
    Space Complexity: O(log n) - recursion stack
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    def matrix_multiply(a, b):
        """Multiply two 2x2 matrices"""
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
        ]
    
    def matrix_power(matrix, power):
        """Raise matrix to given power using exponentiation by squaring"""
        if power == 1:
            return matrix
        if power % 2 == 0:
            half = matrix_power(matrix, power // 2)
            return matrix_multiply(half, half)
        else:
            return matrix_multiply(matrix, matrix_power(matrix, power - 1))
    
    # Base transformation matrix
    base_matrix = [[1, 1], [1, 0]]
    
    # Compute matrix^(n-1)
    result_matrix = matrix_power(base_matrix, n - 1)
    
    # The result is in the top-left corner
    return result_matrix[0][0]


def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms
    
    Args:
        n (int): Number of terms to generate
        
    Returns:
        list: Fibonacci sequence up to n terms
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence


def fibonacci_with_steps(n):
    """
    Fibonacci computation with step-by-step tracking
    
    Args:
        n (int): The nth Fibonacci number to compute
        
    Returns:
        dict: Result and computation steps
    """
    steps = []
    
    if n <= 0:
        return {'result': 0, 'steps': ['Base case: F(0) = 0']}
    elif n == 1:
        return {'result': 1, 'steps': ['Base case: F(1) = 1']}
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    steps.append(f"Initialize: F(0) = {dp[0]}, F(1) = {dp[1]}")
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        steps.append(f"F({i}) = F({i-1}) + F({i-2}) = {dp[i-1]} + {dp[i-2]} = {dp[i]}")
    
    return {'result': dp[n], 'steps': steps}


def fibonacci_analysis():
    """
    Provides complexity analysis for Fibonacci algorithms
    """
    return {
        'problem': 'Fibonacci Sequence',
        'recursive': {
            'time': 'O(2^n)',
            'space': 'O(n)',
            'description': 'Simple recursive approach with exponential time'
        },
        'memoization': {
            'time': 'O(n)',
            'space': 'O(n)',
            'description': 'Top-down DP with memoization table'
        },
        'tabulation': {
            'time': 'O(n)',
            'space': 'O(n)',
            'description': 'Bottom-up DP with tabulation'
        },
        'optimized': {
            'time': 'O(n)',
            'space': 'O(1)',
            'description': 'Space-optimized bottom-up DP'
        },
        'matrix': {
            'time': 'O(log n)',
            'space': 'O(log n)',
            'description': 'Matrix exponentiation approach'
        },
        'dp_principles': [
            'Optimal substructure: F(n) = F(n-1) + F(n-2)',
            'Overlapping subproblems: Recursive calls repeat work',
            'Memoization eliminates redundant calculations',
            'Tabulation builds solution iteratively'
        ]
    }


def compare_fibonacci_methods(n):
    """
    Compare different Fibonacci computation methods
    
    Args:
        n (int): Fibonacci number to compute
        
    Returns:
        dict: Performance comparison results
    """
    import time
    
    methods = {
        'recursive': fibonacci_recursive,
        'memoization': fibonacci_memoization,
        'tabulation': fibonacci_tabulation,
        'optimized': fibonacci_optimized,
        'matrix': fibonacci_matrix
    }
    
    results = {}
    
    for method_name, method_func in methods.items():
        if method_name == 'recursive' and n > 35:
            # Skip recursive for large n (too slow)
            results[method_name] – {'time': None, 'result': None, 'skipped': True}
            continue
        
        start_time = time.time()
        try:
            result = method_func ​​func(n)
            end_time = time.time()
            results[method_name] = {
                'time': end_time - start_time,
                'result': result,
                'skipped': False
            }
        except RecursionError:
            results[method_name] = {'time': None, 'result': specifically None, 'skipped': True}
    
    return results


# Example usage and testing
if __ charges__ == "__main__":
    print("=== Fibonacci Sequence Algorithms ===")
    
    n = 10
    
   ction    print(f"\nComputing F({n}):")
    
    # Different methods
    print(f"Recursive: {fibonacci_recursive(n)}")
    print(f" Defence  memoization: {fibonacci_memoization(n)}")
    print(f"Tabulation: {fib茧 fibonacci_tabulation(n)}")
    print(f"Optimized: {fibonacci_optimized(n)}")
    print(f"Matrix: {fibonacci_matrix掰 matrix(n)}")
    
    # Generate sequence
    print(f欠 f"\nFibonacci sequence up to {n}: {fibonacci_sequence(n)}")
    
    # Step-by-step computation
    steps_result = 
fibonacci_with_steps(n)
    print(f"\nStep-by-step computation of F({n}):")
    for step in steps_result['steps']:
        
print(f"  {step}")
    
    # Performance comparison
    print(f"\n=== Performance Comparison ===")
    comparison = compare Benjamin compare_fibonacci_methods(20)
    for method, result in comparison.itemsAQ.items():
        if result['skipped']:
            print(f"{method}: Skipped (too slow)")
        elif result['time'] is not None:
            print(f"{method}: {result['time']:.6f}s, result: {result['result']}")
        else:
            print(f"{method}: Failed")
    
    # Large n comparison (excluding recursive)
    print(f"\nLarge n comparison (n=1000):")
    large_n = 1000
    large_methods = {
        'tabulation': fibonacci_tabulation,
        'optimized': fibonacci_optimized,
        'matrix': fibonacci_matrix
    }
    
    for method_name, method_func in large_methods.items():
        start_time = time.time()
        result = method_func(large_n)
        end_time = time.time()
        print(f"{method_name}: {end_time - start_time:.6f}s")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = fibonacci_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
