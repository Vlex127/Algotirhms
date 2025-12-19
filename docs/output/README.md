# Algorithms Repository

A comprehensive collection of algorithms implemented in Python with detailed
complexity analysis, examples, and testing utilities.

## Structure

### Sorting

- `bubble_sort`
- `counting_sort`
- `heap_sort`
- `merge_sort`
- `quick_sort`

### Searching

- `binary_search`
- `exponential_search`
- `interpolation_search`
- `linear_search`

### Data Structures

- `linked_list`
- `queue`
- `stack`

### Graph Algorithms

- `bfs`
- `dfs`
- `dijkstra`
- `floyd_warshall`
- `kruskal`

### Dynamic Programming

- `fibonacci`
- `knapsack`
- `longest_common_subsequence`
- `matrix_chain_multiplication`

### Greedy

- `activity_selection`
- `fractional_knapsack`

### Divide And Conquer

- `binary_search`
- `closest_pair`

## Usage

```python
from sorting.bubble_sort import bubble_sort
from data_structures.stack import Stack

# Use algorithms
sorted_array = bubble_sort([5, 2, 8, 1, 9])
stack = Stack()
stack.push(10)
```

## Complexity Analysis

Each algorithm includes detailed time and space complexity analysis
along with performance comparisons and optimization techniques.

## Testing

Run tests using the main.py script:

```bash
python main.py --test
```
