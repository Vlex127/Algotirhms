# Algorithms Repository

A comprehensive collection of algorithms implemented in Python with detailed complexity analysis and documentation.

## Project Structure

```
algorithms/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── main.py                      # Main testing and demonstration script
├── utils/                       # Utility functions and testing framework
│   ├── __init__.py
│   ├── complexity_analyzer.py   # Time and space complexity analysis tools
│   └── test_runner.py          # Automated testing utilities
├── sorting/                     # Sorting algorithms
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── quick_sort.py
│   ├── merge_sort.py
│   ├── heap_sort.py
│   └── counting_sort.py
├── searching/                   # Searching algorithms
│   ├── __init__.py
│   ├── linear_search.py
│   ├── binary_search.py
│   ├── interpolation_search.py
│   └── exponential_search.py
├── data_structures/             # Data structures
│   ├── __init__.py
│   ├── linked_list.py
│   ├── stack.py
│   ├── queue.py
│   ├── binary_tree.py
│   ├── heap.py
│   └── graph.py
├── graph_algorithms/            # Graph algorithms
│   ├── __init__.py
│   ├── bfs.py                  # Breadth-First Search
│   ├── dfs.py                  # Depth-First Search
│   ├── dijkstra.py             # Dijkstra's shortest path
│   ├── kruskal.py              # Kruskal's MST algorithm
│   └── floyd_warshall.py       # All pairs shortest path
├── dynamic_programming/         # Dynamic programming algorithms
│   ├── __init__.py
│   ├── fibonacci.py
│   ├── knapsack.py
│   ├── longest_common_subsequence.py
│   └── matrix_chain_multiplication.py
├── greedy/                      # Greedy algorithms
│   ├── __init__.py
│   ├── activity_selection.py
│   ├── huffman_coding.py
│   └── coin_change.py
├── divide_and_conquer/          # Divide and conquer algorithms
│   ├── __init__.py
│   ├── strassen_matrix.py
│   └── closest_pair.py
└── docs/                        # Documentation and PDFs
    ├── complexity_analysis.pdf
    └── algorithm_documentation.pdf
```

## Algorithm Categories

### 1. Sorting Algorithms
- **Bubble Sort**: O(n²) time, O(1) space
- **Quick Sort**: O(n log n) average, O(n²) worst case, O(log n) space
- **Merge Sort**: O(n log n) time, O(n) space
- **Heap Sort**: O(n log n) time, O(1) space
- **Counting Sort**: O(n + k) time, O(k) space

### 2. Searching Algorithms
- **Linear Search**: O(n) time, O(1) space
- **Binary Search**: O(log n) time, O(1) space
- **Interpolation Search**: O(log log n) average, O(n) worst case
- **Exponential Search**: O(log n) time

### 3. Data Structures
- **Linked List**: O(1) insertion/deletion, O(n) search
- **Stack**: O(1) push/pop operations
- **Queue**: O(1) enqueue/dequeue operations
- **Binary Tree**: O(log n) average, O(n) worst case
- **Heap**: O(log n) insertion/deletion, O(1) peek
- **Graph**: Varies by implementation and operation

### 4. Graph Algorithms
- **BFS**: O(V + E) time, O(V) space
- **DFS**: O(V + E) time, O(V) space
- **Dijkstra**: O((V + E) log V) with priority queue
- **Kruskal**: O(E log E) time
- **Floyd-Warshall**: O(V³) time

### 5. Dynamic Programming
- **Fibonacci**: O(n) time, O(1) space (optimized)
- **Knapsack**: O(nW) time, O(nW) space
- **LCS**: O(mn) time, O(mn) space
- **Matrix Chain**: O(n³) time

### 6. Greedy Algorithms
- **Activity Selection**: O(n log n) time
- **Huffman Coding**: O(n log n) time
- **Coin Change**: O(n log n) time

### 7. Divide and Conquer
- **Strassen Matrix**: O(n^2.807) time
- **Closest Pair**: O(n log n) time

## Usage

```python
from sorting.bubble_sort import bubble_sort
from data_structures.stack import Stack

# Use algorithms
sorted_array = bubble_sort([5, 2, 8, 1, 9])
stack = Stack()
stack.push(10)
```

## Testing

### Individual Algorithm Testing

#### Sorting Algorithms
```bash
# Test bubble sort
python -c "from sorting.bubble_sort import bubble_sort; print(bubble_sort([5, 2, 8, 1, 9]))"

# Test quick sort
python -c "from sorting.quick_sort import quick_sort; print(quick_sort([5, 2, 8, 1, 9]))"

# Test merge sort
python -c "from sorting.merge_sort import merge_sort; print(merge_sort([5, 2, 8, 1, 9]))"

# Test heap sort
python -c "from sorting.heap_sort import heap_sort; print(heap_sort([5, 2, 8, 1, 9]))"

# Test counting sort
python -c "from sorting.counting_sort import counting_sort; print(counting_sort([5, 2, 8, 1, 9]))"
```

#### Searching Algorithms
```bash
# Test linear search
python -c "from searching.linear_search import linear_search; print(linear_search([1, 3, 5, 7, 9], 5))"

# Test binary search
python -c "from searching.binary_search import binary_search_iterative; print(binary_search_iterative([1, 2, 3, 4, 5], 3))"

# Test interpolation search
python -c "from searching.interpolation_search import interpolation_search; print(interpolation_search([1, 2, 3, 4, 5], 3))"

# Test exponential search
python -c "from searching.exponential_search import exponential_search; print(exponential_search([1, 2, 3, 4, 5], 3))"
```

#### Data Structures
```bash
# Test Linked List
python -c "from data_structures.linked_list import LinkedList; ll = LinkedList(); ll.append(1); ll.append(2); print(ll.to_list())"

# Test Stack
python -c "from data_structures.stack import Stack; s = Stack(); s.push(10); s.push(20); print(s.pop()); print(s.size())"

# Test Queue
python -c "from data_structures.queue import Queue; q = Queue(); q.enqueue(10); q.enqueue(20); print(q.dequeue()); print(q.size())"
```

#### Graph Algorithms
```bash
# Test BFS
python -c "from graph_algorithms.bfs import bfs; print(bfs({0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}, 2))"

# Test DFS
python -c "from graph_algorithms.dfs import dfs; print(dfs({0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}, 2))"

# Test Dijkstra
python -c "from graph_algorithms.dijkstra import dijkstra; print(dijkstra({0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}, 0))"

# Test Floyd-Warshall
python -c "from graph_algorithms.floyd_warshall import floyd_warshall; print(floyd_warshall([[0, 999, 3, 999], [2, 0, 999, 999], [999, 7, 0, 1], [6, 999, 999, 0]]))"
```

#### Dynamic Programming
```bash
# Test Fibonacci (direct execution due to import issues)
python dynamic_programming/fibonacci.py

# Test LCS (direct execution)
python dynamic_programming/longest_common_subsequence.py

# Test Matrix Chain Multiplication (direct execution)A
python dynamic_programming/matrix_chain_multiplication.py
```

#### Greedy Algorithms
```bash
# Test Activity Selection
python -c "from greedy.activity_selection import activity_selection; print(activity_selection([(1,4,'A1'), (3,5,'A2'), (0,6,'A3'), (5,7,'A4')]))"

# Test Fractional Knapsack
python -c "from greedy.fractional_knapsack import fractional_knapsack; print(fractional_knapsack([60,100,120], [10,20,30], 50))"
```

#### Divide and Conquer
```bash
# Test Binary Search (direct execution due to import issues)
python divide_and_conquer/binary_search.py

# Test Closest Pair (direct execution)
python divide_and_conquer/closest_pair.py
```

### Main Test Runner

Use the main.py script for comprehensive testing:

```bash
# Show help
python main.py --help

# Test all algorithms
python main.py --test-all

# Test specific category
python main.py --test-category sorting

# Test specific algorithm
python main.py --test-algorithm bubble_sort

# Run complexity analysis
python main.py --analyze-complexity
```

### Module Testing

For modules with import issues, run them directly:

```bash
# Run individual algorithm files
python sorting/bubble_sort.py
python searching/binary_search.py
python data_structures/stack.py
python graph_algorithms/bfs.py
python greedy/activity_selection.py
python divide_and_conquer/binary_search.py
```

## Complexity Analysis

Each algorithm includes detailed time and space complexity analysis
along with performance comparisons and optimization techniques.

## Requirements

- Python 3.8+
- matplotlib (for complexity visualization)
- numpy (for performance testing)
- reportlab (for PDF generation)

## Features

- **Comprehensive Coverage**: All major algorithm categories
- **Detailed Comments**: Line-by-line explanations
- **Complexity Analysis**: Time and space complexity for each algorithm
- **Automated Testing**: Built-in testing framework
- **Performance Benchmarking**: Compare algorithm performance
- **PDF Documentation**: Generated complexity analysis reports
- **Visualization**: Performance graphs and complexity charts

## Contributing

1. Add new algorithms to appropriate categories
2. Include comprehensive comments
3. Add complexity analysis
4. Update documentation
5. Run tests before submitting

## License

MIT License - feel free to use for educational purposes
