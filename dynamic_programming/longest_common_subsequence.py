"""
Longest Common Subsequence (LCS) - Dynamic Programming

Time Complexity:
- Recursive: O(2^(m+n)) - exponential
- Memoization: O(m*n) - quadratic
- Tabulation: O(m*n) - quadratic

Space Complexity:
- Recursive: O(m+n) - recursion stack
- Memoization: O(m*n) - memo table + recursion stack
- Tabulation: O(m*n) - DP table
- Optimized: O(min(m,n)) - space-optimized

Algorithm Description:
LCS finds the longest subsequence common to two sequences. A subsequence
is a sequence that appears in the same relative order but not necessarily
contiguous. It's a classic DP problem demonstrating optimal substructure
and overlapping subproblems.

Applications:
- DNA sequence analysis
- Version control systems
- Plagiarism detection
- File comparison tools
- Bioinformatics
"""

def lcs_recursive(s1, s2, i=0, j=0):
    """
    Simple recursive LCS implementation (inefficient)
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        i (int): Current index in s1
        j (int): Current index in s2
        
    Returns:
        int: Length of longest common subsequence
        
    Time Complexity: O(2^(m+n))
    Space Complexity: O(m+n)
    """
    if i == len(s1) or j == len(s2):
        return 0
    
    if s1[i] == s2[j]:
        return 1 + lcs_recursive(s1, s2, i + 1, j + 1)
    else:
        return max(
            lcs_recursive(s1, s2, i + 1, j),
            lcs_recursive(s1, s2, i, j + 1)
        )


def lcs_memoization(s1, s2):
    """
    LCS with memoization (top-down DP)
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        int: Length of longest common subsequence
        
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    m, n = len(s1), len(s2)
    memo = {}
    
    def lcs_helper(i, j):
        if i == m or j == n:
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if s1[i] == s2[j]:
            result = 1 + lcs_helper(i + 1, j + 1)
        else:
            result = max(lcs_helper(i + 1, j), lcs_helper(i, j + 1))
        
        memo[(i, j)] = result
        return result
    
    return lcs_helper(0, 0)


def lcs_tabulation(s1, s2):
    """
    LCS with tabulation (bottom-up DP)
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        int: Length of longest common subsequence
        
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    m, n = len(s1), len(s2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def lcs_with_path(s1, s2):
    """
    LCS with path reconstruction to get the actual subsequence
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        str: The longest common subsequence
        int: Length of LCS
        
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    m, n = len(s1), len(s2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct LCS
    lcs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs)), dp[m][n]


def lcs_optimized(s1, s2):
    """
    Space-optimized LCS implementation
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        int: Length of longest common subsequence
        
    Time Complexity: O(m*n)
    Space Complexity: O(min(m,n))
    """
    # Ensure s1 is the shorter string for better space optimization
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    
    m, n = len(s1), len(s2)
    
    # Use only two rows
    prev_row = [0] * (m + 1)
    curr_row = [0] * (m + 1)
    
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr_row[i] = prev_row[i - 1] + 1
            else:
                curr_row[i] = max(prev_row[i], curr_row[i - 1])
        
        # Swap rows
        prev_row, curr_row = curr_row, prev_row
    
    return prev_row[m]


def lcs_all_subsequences(s1, s2):
    """
    Find all possible longest common subsequences
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        set: Set of all LCS strings
        
    Time Complexity: O(m*n) for DP + exponential for enumeration
    Space Complexity: O(m*n)
    """
    m, n = len(s1), len(s2)
    
    # Build DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    lcs_length = dp[m][n]
    all_lcs = set()
    
    def backtrack(i, j, current_lcs):
        if i == 0 or j == 0:
            if len(current_lcs) == lcs_length:
                all_lcs.add(''.join(reversed(current_lcs)))
            return
        
        if s1[i - 1] == s2[j - 1]:
            current_lcs.append(s1[i - 1])
            backtrack(i - 1, j - 1, current_lcs)
            current_lcs.pop()
        else:
            if dp[i - 1][j] == dp[i][j]:
                backtrack(i - 1, j, current_lcs)
            if dp[i][j - 1] == dp[i][j]:
                backtrack(i, j - 1, current_lcs)
    
    backtrack(m, n, [])
    return all_lcs


def lcs_with_trace(s1, s2):
    """
    LCS with detailed trace of DP table filling
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        dict: Detailed trace of algorithm execution
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    steps = []
    
    steps.append(f"Initial DP table: {m+1} x {n+1}")
    steps.append(f"Strings: '{s1}' (length {m}), '{s2}' (length {n})")
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            old_value = max(dp[i - 1][j], dp[i][j - 1])
            
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                steps.append(f"DP[{i}][{j}] = DP[{i-1}][{j-1}] + 1 = {dp[i][j]} (match: '{s1[i-1]}')")
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                steps.append(f"DP[{i}][{j}] = max(DP[{i-1}][{j}], DP[{i}][{j-1}]) = max({dp[i-1][j]}, {dp[i][j-1]}) = {dp[i][j]}")
    
    # Reconstruct LCS
    lcs = []
    i, j = m, n
    reconstruction_steps = []
    
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            reconstruction_steps.append(f"Match '{s1[i-1]}' at position ({i},{j})")
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            reconstruction_steps.append(f"Move up from ({i},{j})")
            i -= 1
        else:
            reconstruction_steps.append(f"Move left from ({i},{j})")
            j -= 1
    
    result = ''.join(reversed(lcs))
    
    return {
        'lcs': result,
        'length': dp[m][n],
        'dp_table': dp,
        'steps': steps,
        'reconstruction_steps': reconstruction_steps
    }


def lcs_analysis():
    """
    Provides complexity analysis for LCS algorithms
    """
    return {
        'problem': 'Longest Common Subsequence',
        'recursive': {
            'time': 'O(2^(m+n))',
            'space': 'O(m+n)',
            'description': 'Simple recursive approach with exponential time'
        },
        'memoization': {
            'time': 'O(m*n)',
            'space': 'O(m*n)',
            'description': 'Top-down DP with memoization'
        },
        'tabulation': {
            'time': 'O(m*n)',
            'space': 'O(m*n)',
            'description': 'Bottom-up DP with tabulation'
        },
        'optimized': {
            'time': 'O(m*n)',
            'space': 'O(min(m,n))',
            'description': 'Space-optimized version using only two rows'
        },
        'dp_principles': [
            'Optimal substructure: LCS of prefixes contains LCS of smaller prefixes',
            'Overlapping subproblems: Same subproblems solved multiple times',
            'State definition: DP[i][j] = LCS length of s1[:i] and s2[:j]',
            'Transition: DP[i][j] = DP[i-1][j-1] + 1 if match, else max(DP[i-1][j], DP[i][j-1])'
        ],
        'applications': [
            'DNA sequence analysis',
            'Version control systems (diff)',
            'Plagiarism detection',
            'File comparison tools',
            'Bioinformatics',
            'Natural language processing'
        ]
    }


def compare_lcs_methods(s1, s2):
    """
    Compare different LCS computation methods
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        dict: Performance comparison results
    """
    import time
    
    methods = {
        'memoization': lcs_memoization,
        'tabulation': lcs_tabulation,
        'optimized': lcs_optimized
    }
    
    results = {}
    
    for method_name, method_func in methods.items():
        start_time = time.time()
        result = method_func(s1, s2)
        end_time = time.time()
        
        results[method_name] = {
            'time': end_time - start_time,
            'result': result
        }
    
    # Also get LCS with path
    start_time = time.time()
    lcs_string, lcs_length = lcs_with_path(s1, s2)
    end_time = time.time()
    
    results['with_path'] = {
        'time': end_time - start_time,
        'result': lcs_string,
        'length': lcs_length
    }
    
    return results


# Example usage and testing
if __name__ == "__main__":
    # Test strings
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    
    print("=== Longest Common Subsequence ===")
    print(f"String 1: '{s1}'")
    print(f"String 2: '{s2}'")
    
    # Different methods
    print(f"\nMemoization: {lcs_memoization(s1, s2)}")
    print(f"Tabulation: {lcs_tabulation(s1, s2)}")
    print(f"Optimized: {lcs_optimized(s1, s2)}")
    
    # With path reconstruction
    lcs_string, lcs_length = lcs_with_path(s1, s2)
    print(f"\nLCS string: '{lcs_string}'")
    print(f"LCS length: {lcs_length}")
    
    # All possible LCS
    print(f"\nAll LCS strings: {lcs_all_subsequences(s1, s2)}")
    
    # Detailed trace
    print("\n=== Detailed Trace ===")
    trace = lcs_with_trace(s1, s2)
    print(f" same result: '{trace['lcs']}'")
    print(f"Length: {trace['length']}")
    
    # Performance comparison
    print("\n=== Performance Comparison ===")
    comparison = compare_lcs_methods(s1, s2)
    for method, result in comparison.items():
        if 'length' in result:
            print(f"{method}: {result['time']:.6f}s, result: '{result['result']}' (length: {result['length']})")
        else:
            print(f"{method}: {result['time']:.6f}s, result: {result['result']}")
    
    # Test with longer strings
    print("\n=== Longer Strings Test ===")
    long_s1 = "ABCDGH"
    long_s2 = "AEDFHR"
    
    long_comparison = compare_lcs_methods(long_s1, long_s2)
    for method, result in long_comparison.items():
        if 'length' in result:
            print(f"{method}: {result['time']:.6f}s, result: '{result['result']}' (length: {result['length']})")
        else:
            print(f"{method}: {result['time']:.6f}s, result: {result['result']}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = lcs_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
