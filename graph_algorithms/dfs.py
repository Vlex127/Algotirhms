"""
Depth-First Search (DFS) Algorithm

Time Complexity:
- O(V + E) - V is number of vertices, E is number of edges
- For adjacency list: O(V + E)
- For adjacency matrix: O(V²)

Space Complexity:
- O(V) - for recursion stack and visited set
- O(V) - for explicit stack in iterative version

Algorithm Description:
DFS is a graph traversal algorithm that explores as far as possible along
each branch before backtracking. It uses a stack (recursion or explicit)
to keep track of vertices to visit next.

Applications:
- Topological sorting
- Connected components detection
- Cycle detection
- Maze solving
- Path finding
"""

def dfs(graph, start):
    """
    Depth-First Search traversal of a graph (iterative implementation)
    
    Args:
        graph: Graph represented as adjacency list {vertex: [neighbors]}
        start: Starting vertex
        
    Returns:
        list: Order of visited vertices
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    from .stack import Stack
    
    visited = set()
    stack = Stack()
    traversal_order = []
    
    # Start with the starting vertex
    stack.push(start)
    
    while not stack.is_empty():
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
            traversal_order.append(current)
            
            # Add all neighbors to stack (reverse order for consistent traversal)
            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.push(neighbor)
    
    return traversal_order


def dfs_recursive(graph, start, visited=None, traversal_order=None):
    """
    Depth-First Search traversal of a graph (recursive implementation)
    
    Args:
        graph: Graph represented as adjacency list
        start: Starting vertex
        visited: Set of visited vertices (used internally)
        traversal_order: Order of visited vertices (used internally)
        
    Returns:
        list: Order of visited vertices
        
    Time Complexity: O(V + E)
    Space Complexity: O(V) - recursion stack
    """
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []
    
    visited.add(start)
    traversal_order.append(start)
    
    # Visit all neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)
    
    return traversal_order


def dfs_path_exists(graph, start, end):
    """
    Check if a path exists between two vertices using DFS
    
    Args:
        graph: Graph represented as adjacency list
        start: Starting vertex
        end: Target vertex
        
    Returns:
        bool: True if path exists, False otherwise
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    
    def dfs_helper(vertex):
        if vertex == end:
            return True
        
        visited.add(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if dfs_helper(neighbor):
                    return True
        
        return False
    
    return dfs_helper(start)


def dfs_find_path(graph, start, end):
    """
    Find a path between two vertices using DFS
    
    Args:
        graph: Graph represented as adjacency list
        start: Starting vertex
        end: Target vertex
        
    Returns:
        list: Path from start to end, None if no path exists
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    from .stack import Stack
    
    if start == end:
        return [start]
    
    visited = set()
    stack = Stack()
    parent = {}  # To reconstruct the path
    
    stack.push(start)
    visited.add(start)
    parent[start] = None
    
    while not stack.is_empty():
        current = stack.pop()
        
        # Check if we reached the target
        if current == end:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        # Visit all neighbors
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.push(neighbor)
    
    return None  # No path found


def dfs_connected_components(graph):
    """
    Find all connected components in an undirected graph using DFS
    
    Args:
        graph: Graph represented as adjacency list
        
    Returns:
        list: List of connected components (each component is a list of vertices)
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    components = []
    
    def dfs_component(vertex, component):
        visited.add(vertex)
        component.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs_component(neighbor, component)
    
    for vertex in graph:
        if vertex not in visited:
            component = []
            dfs_component(vertex, component)
            components.append(component)
    
    return components


def topological_sort(graph):
    """
    Perform topological sort on a directed acyclic graph (DAG) using DFS
    
    Args:
        graph: Directed acyclic graph represented as adjacency list
        
    Returns:
        list: Topologically sorted vertices, None if graph has cycle
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    recursion_stack = set()
    result = []
    
    def dfs_helper(vertex):
        visited.add(vertex)
        recursion_stack.add(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if not dfs_helper(neighbor):
                    return False
            elif neighbor in recursion_stack:
                # Cycle detected
                return False
        
        recursion_stack.remove(vertex)
        result.append(vertex)
        return True
    
    for vertex in graph:
        if vertex not in visited:
            if not dfs_helper(vertex):
                return None  # Graph has cycle
    
    return result[::-1]  # Reverse to get correct topological order


def dfs_cycle_detection(graph):
    """
    Detect cycles in a directed graph using DFS
    
    Args:
        graph: Directed graph represented as adjacency list
        
    Returns:
        bool: True if cycle exists, False otherwise
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    recursion_stack = set()
    
    def dfs_helper(vertex):
        visited.add(vertex)
        recursion_stack.add(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if dfs_helper(neighbor):
                    return True
            elif neighbor in recursion_stack:
                return True
        
        recursion_stack.remove(vertex)
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if dfs_helper(vertex):
                return True
    
    return False


def dfs_all_paths(graph, start, end):
    """
    Find all possible paths between two vertices using DFS
    
    Args:
        graph: Graph represented as adjacency list
        start: Starting vertex
        end: Target vertex
        
    Returns:
        list: List of all paths from start to end
        
    Time Complexity: O(V + E + P) where P is number of paths
    Space Complexity: O(V) - recursion stack
    """
    all_paths = []
    
    def dfs_helper(current, path, visited):
        if current == end:
            all_paths.append(path.copy())
            return
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                
                dfs_helper(neighbor, path, visited)
                
                # Backtrack
                path.pop()
                visited.remove(neighbor)
    
    visited = {start}
    dfs_helper(start, [start], visited)
    return all_paths


def dfs_strongly_connected_components(graph):
    """
    Find strongly connected components in a directed graph using DFS
    (Kosaraju's algorithm)
    
    Args:
        graph: Directed graph represented as adjacency list
        
    Returns:
        list: List of strongly connected components
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    def dfs_first_pass(vertex, visited, stack):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs_first_pass(neighbor, visited, stack)
        stack.append(vertex)
    
    def dfs_second_pass(vertex, visited, component, transposed_graph):
        visited.add(vertex)
        component.append(vertex)
        for neighbor in transposed_graph.get(vertex, []):
            if neighbor not in visited:
                dfs_second_pass(neighbor, visited, component, transposed_graph)
    
    # Build transpose graph
    transposed_graph = {}
    for vertex in graph:
        transposed_graph[vertex] = []
    
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            transposed_graph.setdefault(neighbor, []).append(vertex)
    
    # First pass to fill stack
    visited = set()
    stack = []
    for vertex in graph:
        if vertex not in visited:
            dfs_first_pass(vertex, visited, stack)
    
    # Second pass to find SCCs
    visited.clear()
    sccs = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            component = []
            dfs_second_pass(vertex, visited, component, transposed_graph)
            sccs.append(component)
    
    return sccs


def dfs_analysis():
    """
    Provides complexity analysis for DFS algorithm
    """
    return {
        'algorithm': 'Depth-First Search (DFS)',
        'time_complexity': 'O(V + E)',
        'space_complexity': 'O(V)',
        'traversal_order': 'Depth-first (explores one branch completely)',
        'data_structure_used': 'Stack (recursion or explicit)',
        'guarantees': [
            'Visits all reachable vertices',
            'Explores graph deeply before broadly',
            'Can be used for various graph problems'
        ],
        'applications': [
            'Topological sorting',
            'Connected components detection',
            'Cycle detection',
            'Maze solving',
            'Path finding',
            'Strongly connected components'
        ],
        'advantages': [
            'Lower memory usage than BFS for sparse graphs',
            'Good for problems requiring deep exploration',
            'Simple recursive implementation',
            'Can find all paths between vertices'
        ],
        'disadvantages': [
            'May not find shortest path',
            'Can get stuck in deep recursion',
            'Not guaranteed to find optimal solution',
            'May explore unnecessary deep paths'
        ]
    }


# Example usage and testing
if __name__ == "__main__":
    # Example graph (undirected)
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E', 'F'],
        'C': ['A', 'G'],
        'D': ['A', 'H'],
        'E': ['B', 'I'],
        'F': ['B', 'I'],
        'G': ['C', 'H'],
        'H': ['D', 'G', 'I'],
        'I': ['E', 'F', 'H']
    }
    
    print("=== DFS Traversal ===")
    traversal = dfs(graph, 'A')
    print(f"DFS traversal from 'A': {traversal}")
    
    recursive_traversal = dfs_recursive(graph, 'A')
    print(f"Recursive DFS traversal from 'A': {recursive_traversal}")
    
    print("\n=== Path Finding ===")
    path = dfs_find_path(graph, 'A', 'I')
    print(f"Path from 'A' to 'I': {path}")
    
    path_exists = dfs_path_exists(graph, 'A', 'I')
    print(f"Path exists from 'A' to 'I': {path_exists}")
    
    print("\n=== All Paths ===")
    all_paths = dfs_all_paths(graph, 'A', 'I')
    print(f"All paths from 'A' to 'I': {all_paths}")
    
    print("\n=== Connected Components ===")
    # Graph with multiple components
    multi_component_graph = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B'],
        'D': ['E'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['H'],
        'H': ['G']
    }
    
    components = dfs_connected_components(multi_component_graph)
    print(f"Connected components: {components}")
    
    print("\n=== Topological Sort ===")
    # Directed acyclic graph
    dag = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    
    topo_sort = topological_sort(dag)
    print(f"Topological sort: {topo_sort}")
    
    print("\n=== Cycle Detection ===")
    # Graph with cycle
    cyclic_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A', 'D'],
        'D': []
    }
    
    has_cycle = dfs_cycle_detection(cyclic_graph)
    print(f"Graph has cycle: {has_cycle}")
    
    print("\n=== Strongly Connected Components ===")
    # Directed graph
    directed_graph = {
        'A': ['B'],
        'B': ['C', 'E'],
        'C': ['D'],
        'D': ['A'],
        'E': ['F'],
        'F': ['G'],
        'G': ['E']
    }
    
    sccs = dfs_strongly_connected_components(directed_graph)
    print(f"Strongly connected components: {sccs}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = dfs_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
