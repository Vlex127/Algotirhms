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

### Running Tests
```bash
python main.py --test-all
python main.py --test-category sorting
python main.py --test-algorithm bubble_sort
```

### Complexity Analysis
```bash
python utils/complexity_analyzer.py --algorithm quick_sort
python utils/complexity_analyzer.py --category sorting
```

### Generate Documentation
```bash
python docs/generate_pdf.py
```

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
