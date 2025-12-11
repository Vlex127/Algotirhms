"""
Floyd-Warshall Algorithm

Time Complexity:
- O(V³) - three nested loops over all vertices

Space Complexity:
- O(V²) - distance matrix
- O(V²) - path matrix (optional)

Algorithm Description:
Floyd-Warshall algorithm finds the shortest paths between all pairs of
vertices in a weighted directed graph. It works with negative edge weights
but not with negative cycles. The algorithm uses dynamic programming to
gradually improve the path estimates.

Applications:
- Routing protocols
- Network analysis
- Transportation networks
- Game development
- Social network analysis
"""

def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm to find all pairs shortest paths
    
    Args:
        graph: Weighted directed graph represented as adjacency list
               {vertex: [(neighbor, weight), ...]}
               
    Returns:
        dict: Distance matrix {source: {destination: distance}}
        dict: Next matrix for path reconstruction {source: {destination: next_hop}}
        
    Time Complexity: O(V³)
    Space Complexity: O(V²)
    """
    # Get all vertices
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            vertices.add(neighbor)
    
    vertices = list(vertices)
    n = len(vertices)
    
    # Initialize distance matrix
    dist = {source: {dest: float('inf') for dest in vertices} for source in vertices}
    next_hop = {source: {dest: None for dest in vertices} for source in vertices}
    
    # Set distances to 0 for same vertex
    for vertex in vertices:
        dist[vertex][vertex] = 0
        next_hop[vertex][vertex] = vertex
    
    # Set initial distances from graph
    for source, neighbors in graph.items():
        for dest, weight in neighbors:
            if weight < dist[source][dest]:
                dist[source][dest] = weight
                next_hop[source][dest] = dest
    
    # Floyd-Warshall main algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_hop[i][j] = next_hop[i][k]
    
    return dist, next_hop


def floyd_warshall_path_reconstruction(next_matrix, source, destination):
    """
    Reconstruct the shortest path from next matrix
    
    Args:
        next_matrix: Next matrix from Floyd-Warshall
        source: Source vertex
        destination: Destination vertex
        
    Returns:
        list: Shortest path from source to destination
    """
    if next_matrix[source][destination] is None:
        return None
    
    path = [source]
    current = source
    
    while current != destination:
        current = next_matrix[current][destination]
        if current is None:
            return None
        path.append(current)
    
    return path


def floyd_warshall_with_path_matrix(graph):
    """
    Floyd-Warshall algorithm with complete path matrix
    
    Args:
        graph: Weighted directed graph represented as adjacency list
        
    Returns:
        dict: Distance matrix
        dict: Complete path matrix {source: {destination: [path]}}
    """
    dist, next_hop = floyd_warshall(graph)
    
    # Build complete path matrix
    paths = {}
    vertices = list(dist.keys())
    
    for source in vertices:
        paths[source] = {}
        for dest in vertices:
            paths[source][dest] = floyd_warshall_path_reconstruction(next_hop, source, dest)
    
    return dist, paths


def floyd_warshall_detect_negative_cycles(graph):
    """
    Detect negative cycles using Floyd-Warshall algorithm
    
    Args:
        graph: Weighted directed graph represented as adjacency list
        
    Returns:
        bool: True if negative cycle exists, False otherwise
        list: Vertices involved in negative cycles (if any)
    """
    dist, _ = floyd_warshall(graph)
    vertices = list(dist.keys())
    
    negative_cycles = []
    
    for vertex in vertices:
        if dist[vertex][vertex] < 0:
            negative_cycles.append(vertex)
    
    return len(negative_cycles) > 0, negative_cycles


def floyd_warshall_transitive_closure(graph):
    """
    Compute transitive closure of a directed graph using Floyd-Warshall
    
    Args:
        graph: Directed graph (unweighted) represented as adjacency list
        
    Returns:
        dict: Reachability matrix {source: {destination: reachable}}
    """
    # Convert unweighted graph to weighted graph (weight 1 for edges)
    weighted_graph = {}
    for vertex, neighbors in graph.items():
        weighted_graph[vertex] = [(neighbor, 1) for neighbor in neighbors]
    
    dist, _ = floyd_warshall(weighted_graph)
    
    # Convert distances to reachability
    reachability = {}
    vertices = list(dist.keys())
    
    for source in vertices:
        reachability[source] = {}
        for dest in vertices:
            reachability[source][dest] = dist[source][dest] != float('inf')
    
    return reachability


def floyd_warshall_apsp_with_details(graph):
    """
    Floyd-Warshall algorithm with detailed step information
    
    Args:
        graph: Weighted directed graph represented as adjacency list
        
    Returns:
        dict: Detailed information about algorithm execution
    """
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            vertices.add(neighbor)
    
    vertices = list(vertices)
    n = len(vertices)
    
    # Initialize matrices
    dist = {source: {dest: float('inf') for dest in vertices} for source in vertices}
    next_hop = {source: {dest: None for dest in vertices} for source in vertices}
    
    # Set initial values
    for vertex in vertices:
        dist[vertex][vertex] = 0
        next_hop[vertex][vertex] = vertex
    
    for source, neighbors in graph.items():
        for dest, weight in neighbors:
            if weight < dist[source][dest]:
                dist[source][dest] = weight
                next_hop[source][dest] = dest
    
    # Track improvements
    improvements = []
    
    # Main algorithm
    for k_idx, k in enumerate(vertices):
        improvements_in_iteration = 0
        
        for i in vertices:
            for j in vertices:
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        old_dist = dist[i][j]
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_hop[i][j] = next_hop[i][k]
                        improvements_in_iteration += 1
                        
                        improvements.append({
                            'iteration': k_idx + 1,
                            'intermediate': k,
                            'source': i,
                            'destination': j,
                            'old_distance': old_dist,
                            'new_distance': dist[i][j],
                            'improvement': old_dist - dist[i][j]
                        })
    
    return {
        'distance_matrix': dist,
        'next_matrix': next_hop,
        'total_improvements': len(improvements),
        'improvements': improvements,
        'vertices': vertices,
        'iterations': len(vertices)
    }


def floyd_warshall_analysis():
    """
    Provides complexity analysis for Floyd-Warshall algorithm
    """
    return {
        'algorithm': "Floyd-Warshall All Pairs Shortest Path",
        'time_complexity': 'O(V³)',
        'space_complexity': 'O(V²)',
        'graph_type': 'Weighted directed graph',
        'negative_weights': 'Handles negative weights, not negative cycles',
        'guarantees': [
            'Finds shortest paths between all vertex pairs',
            'Works with negative edge weights',
            'Complete solution for APSP problem'
        ],
        'applications': [
            'Network routing protocols',
            'Transportation networks',
            'Game development (pathfinding)',
            'Social network analysis',
            'Transitive closure computation',
            'Flight scheduling systems'
        ],
        'advantages': [
            'Simple to implement',
            'Works with negative weights',
            'Complete APSP solution',
            'Deterministic behavior'
        ],
        'disadvantages': [
            'Cubic time complexity',
            'High memory usage',
            'Not suitable for large graphs',
            'Cannot handle negative cycles'
        ]
    }


def floyd_warshall_comparison_with_dijkstra(graph):
    """
    Compare Floyd-Warshall with running Dijkstra from each vertex
    
    Args:
        graph: Weighted directed graph
        
    Returns:
        dict: Performance comparison results
    """
    import time
    from .dijkstra import dijkstra_all_pairs_shortest_paths
    
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            vertices.add(neighbor)
    
    n = len(vertices)
    
    # Floyd-Warshall
    start_time = time.time()
    fw_dist, _ = floyd_warshall(graph)
    fw_time = time.time() - start_time
    
    # Dijkstra from each vertex
    start_time = time.time()
    dijkstra_dist = dijkstra_all_pairs_shortest_paths(graph)
    dijkstra_time = time.time() - start_time
    
    return {
        'num_vertices': n,
        'floyd_warshall': {
            'time': fw_time,
            'complexity': 'O(V³)'
        },
        'dijkstra_all_pairs': {
            'time': dijkstra_time,
            'complexity': 'O(V * (V + E) log V)'
        },
        'speedup': dijkstra_time / fw_time if fw_time > 0 else float('inf'),
        'recommendation': 'Floyd-Warshall' if fw_time < dijkstra_time else 'Dijkstra'
    }


# Example usage and testing
if __name__ == "__main__":
    # Example weighted directed graph
    graph = {
        'A': [('B', 5), ('C', 3)],
        'B': [('C', 2), ('D', 6)],
        'C': [('B', 1), ('D', 4), ('E', 6)],
        'D': [('E', 2)],
        'E': [('A', 1), ('D', 1)]
    }
    
    print("=== Floyd-Warshall Algorithm ===")
    
    # Basic Floyd-Warshall
    dist, next_hop = floyd_warshall(graph)
    print("Distance matrix:")
    for source in dist:
        print(f"  {source}: {dist[source]}")
    
    print("\nNext matrix:")
    for source in next_hop:
        print(f"  {source}: {next_hop[source]}")
    
    print("\n=== Path Reconstruction ===")
    for source in dist:
        for dest in dist[source]:
            if source != dest and dist[source][dest] != float('inf'):
                path = floyd_warshall_path_reconstruction(next_hop, source, dest)
                print(f"Path {source} -> {dest}: {path} (distance: {dist[source][dest]})")
    
    print("\n=== Complete Path Matrix ===")
    dist_complete, paths = floyd_warshall_with_path_matrix(graph)
    print("Complete paths:")
    for source in paths:
        for dest in paths[source]:
            if paths[source][dest]:
                print(f"  {source} -> {dest}: {paths[source][dest]}")
    
    print("\n=== Negative Cycle Detection ===")
    # Graph with negative cycle
    graph_with_negative = {
        'A': [('B', 1)],
        'B': [('C', -2)],
        'C': [('A', -2)]
    }
    
    has_negative_cycle, cycle_vertices = floyd_warshall_detect_negative_cycles(graph_with_negative)
    print(f"Graph has negative cycle: {has_negative_cycle}")
    if has_negative_cycle:
        print(f"Cycle vertices: {cycle_vertices}")
    
    print("\n=== Transitive Closure ===")
    # Unweighted directed graph
    unweighted_graph = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['D'],
        'D': []
    }
    
    reachability = floyd_warshall_transitive_closure(unweighted_graph)
    print("Reachability matrix:")
    for source in reachability:
        reachable_dests = [dest for dest, reachable in reachability[source].items() if reachable]
        print(f"  {source} can reach: {reachable_dests}")
    
    print("\n=== Performance Comparison ===")
    comparison = floyd_warshall_comparison_with_dijkstra(graph)
    print(f"Number of vertices: {comparison['num_vertices']}")
    print(f"Floyd-Warshall time: {comparison['floyd_warshall']['time']:.6f}s")
    print(f"Dijkstra all pairs time: {comparison['dijkstra_all_pairs']['time']:.6f}s")
    print(f"Speedup: {comparison['speedup']:.2f}x")
    print(f"Recommendation: {comparison['recommendation']}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = floyd_warshall_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
