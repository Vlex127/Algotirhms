"""
Breadth-First Search (BFS) Algorithm

Time Complexity:
- O(V + E) - V is number of vertices, E is number of edges
- For adjacency list: O(V + E)
- For adjacency matrix: O(V²)

Space Complexity: O(V) - for queue and visited set

Algorithm Description:
BFS is a graph traversal algorithm that explores all vertices at the current
depth before moving to vertices at the next depth level. It uses a queue
to keep track of vertices to visit next.

Applications:
- Shortest path in unweighted graphs
- Connected components detection
- Level-order traversal in trees
- Web crawling
- Social network analysis
"""

def bfs(graph, start):
    """
    Breadth-First Search traversal of a graph
    
    Args:
        graph: Graph represented as adjacency list {vertex: [neighbors]}
        start: Starting vertex
        
    Returns:
        list: Order of visited vertices
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    from .queue import Queue
    
    visited = set()
    queue = Queue()
    traversal_order = []
    
    # Start with the starting vertex
    queue.enqueue(start)
    visited.add(start)
    
    while not queue.is_empty():
        # Dequeue a vertex and add to traversal order
        current = queue.dequeue()
        traversal_order.append(current)
        
        # Visit all unvisited neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
    
    return traversal_order


def bfs_shortest_path(graph, start, end):
    """
    Find shortest path between two vertices using BFS
    
    Args:
        graph: Graph represented as adjacency list
        start: Starting vertex
        end: Target vertex
        
    Returns:
        list: Shortest path from start to end, None if no path exists
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    from .queue import Queue
    
    if start == end:
        return [start]
    
    visited = set()
    queue = Queue()
    parent = {}  # To reconstruct the path
    
    queue.enqueue(start)
    visited.add(start)
    parent[start] = None
    
    while not queue.is_empty():
        current = queue.dequeue()
        
        # Check if we reached the target
        if current == end:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Reverse to get start to end
        
        # Visit all neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.enqueue(neighbor)
    
    return None  # No path found


def bfs_connected_components(graph):
    """
    Find all connected components in an undirected graph using BFS
    
    Args:
        graph: Graph represented as adjacency list
        
    Returns:
        list: List of connected components (each component is a list of vertices)
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    components = []
    
    for vertex in graph:
        if vertex not in visited:
            # Start BFS for this component
            component = bfs(graph, vertex)
            visited.update(component)
            components.append(component)
    
    return components


def bfs_level_order(graph, start):
    """
    Perform BFS and return vertices grouped by their level from start
    
    Args:
        graph: Graph represented as adjacency list
        start: Starting vertex
        
    Returns:
        dict: Dictionary mapping level to list of vertices at that level
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    from .queue import Queue
    
    visited = set()
    queue = Queue()
    levels = {0: [start]}
    
    queue.enqueue((start, 0))  # (vertex, level)
    visited.add(start)
    
    while not queue.is_empty():
        vertex, level = queue.dequeue()
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue((neighbor, level + 1))
                
                # Add to appropriate level
                if level + 1 not in levels:
                    levels[level + 1] = []
                levels[level + 1].append(neighbor)
    
    return levels


def bfs_distance(graph, start, target):
    """
    Find distance (number of edges) between two vertices using BFS
    
    Args:
        graph: Graph represented as adjacency list
        start: Starting vertex
        target: Target vertex
        
    Returns:
        int: Distance between start and target, -1 if not reachable
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    from .queue import Queue
    
    if start == target:
        return 0
    
    visited = set()
    queue = Queue()
    
    queue.enqueue((start, 0))  # (vertex, distance)
    visited.add(start)
    
    while not queue.is_empty():
        vertex, distance = queue.dequeue()
        
        for neighbor in graph.get(vertex, []):
            if neighbor == target:
                return distance + 1
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue((neighbor, distance + 1))
    
    return -1  # Not reachable


def bfs_bidirectional(graph, start, end):
    """
    Bidirectional BFS for finding shortest path more efficiently
    
    Args:
        graph: Graph represented as adjacency list
        start: Starting vertex
        end: Target vertex
        
    Returns:
        list: Shortest path from start to end, None if no path exists
        
    Time Complexity: O(V + E) but typically faster in practice
    Space Complexity: O(V)
    """
    from .queue import Queue
    
    if start == end:
        return [start]
    
    # Forward search from start
    forward_visited = {start}
    forward_queue = Queue()
    forward_queue.enqueue(start)
    forward_parent = {start: None}
    
    # Backward search from end
    backward_visited = {end}
    backward_queue = Queue()
    backward_queue.enqueue(end)
    backward_parent = {end: None}
    
    meeting_point = None
    
    while not forward_queue.is_empty() and not backward_queue.is_empty():
        # Expand forward search
        forward_size = forward_queue.size()
        for _ in range(forward_size):
            current = forward_queue.dequeue()
            
            for neighbor in graph.get(current, []):
                if neighbor not in forward_visited:
                    forward_visited.add(neighbor)
                    forward_parent[neighbor] = current
                    forward_queue.enqueue(neighbor)
                    
                    # Check if backward search has visited this node
                    if neighbor in backward_visited:
                        meeting_point = neighbor
                        break
            else:
                continue
            break
        
        if meeting_point:
            break
        
        # Expand backward search
        backward_size = backward_queue.size()
        for _ in range(backward_size):
            current = backward_queue.dequeue()
            
            for neighbor in graph.get(current, []):
                if neighbor not in backward_visited:
                    backward_visited.add(neighbor)
                    backward_parent[neighbor] = current
                    backward_queue.enqueue(neighbor)
                    
                    # Check if forward search has visited this node
                    if neighbor in forward_visited:
                        meeting_point = neighbor
                        break
            else:
                continue
            break
        
        if meeting_point:
            break
    
    if not meeting_point:
        return None
    
    # Reconstruct path from meeting point
    # Path from start to meeting point
    path_forward = []
    current = meeting_point
    while current is not None:
        path_forward.append(current)
        current = forward_parent[current]
    
    # Path from meeting point to end
    path_backward = []
    current = meeting_point
    while current is not None:
        path_backward.append(current)
        current = backward_parent[current]
    
    # Combine paths (excluding duplicate meeting point)
    return path_forward[::-1] + path_backward[1:]


def bfs_analysis():
    """
    Provides complexity analysis for BFS algorithm
    """
    return {
        'algorithm': 'Breadth-First Search (BFS)',
        'time_complexity': 'O(V + E)',
        'space_complexity': 'O(V)',
        'traversal_order': 'Level-order (by distance from start)',
        'data_structure_used': 'Queue',
        'guarantees': [
            'Visits vertices in order of distance from start',
            'Finds shortest path in unweighted graphs',
            'Completes in finite time for finite graphs'
        ],
        'applications': [
            'Shortest path in unweighted graphs',
            'Connected components detection',
            'Level-order traversal',
            'Web crawling',
            'Social network analysis',
            'GPS navigation systems'
        ],
        'advantages': [
            'Guaranteed shortest path in unweighted graphs',
            'Complete (finds all reachable vertices)',
            'Systematic exploration'
        ],
        'disadvantages': [
            'High memory usage for large graphs',
            'Not optimal for weighted graphs',
            'May explore many unnecessary vertices'
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
    
    print("=== BFS Traversal ===")
    traversal = bfs(graph, 'A')
    print(f"BFS traversal from 'A': {traversal}")
    
    print("\n=== Shortest Path ===")
    path = bfs_shortest_path(graph, 'A', 'I')
    print(f"Shortest path from 'A' to 'I': {path}")
    
    print("\n=== Distance ===")
    distance = bfs_distance(graph, 'A', 'I')
    print(f"Distance from 'A' to 'I': {distance}")
    
    print("\n=== Level Order ===")
    levels = bfs_level_order(graph, 'A')
    for level, vertices in levels.items():
        print(f"Level {level}: {vertices}")
    
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
    
    components = bfs_connected_components(multi_component_graph)
    print(f"Connected components: {components}")
    
    print("\n=== Bidirectional BFS ===")
    bidirectional_path = bfs_bidirectional(graph, 'A', 'I')
    print(f"Bidirectional BFS path from 'A' to 'I': {bidirectional_path}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = bfs_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
