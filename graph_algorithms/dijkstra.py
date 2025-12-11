"""
Dijkstra's Shortest Path Algorithm

Time Complexity:
- O(V²) - with adjacency matrix and simple array implementation
- O((V + E) log V) - with adjacency list and priority queue
- O(E + V log V) - with binary heap priority queue

Space Complexity: O(V) - for distance array and priority queue

Algorithm Description:
Dijkstra's algorithm finds the shortest paths from a source vertex to all
other vertices in a weighted graph with non-negative edge weights. It uses
a greedy approach, always selecting the vertex with the minimum distance
from the source among the unvisited vertices.

Applications:
- GPS navigation systems
- Network routing protocols
- Flight scheduling
- Game pathfinding
- Logistics optimization
"""

import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm to find shortest paths from source to all vertices
    
    Args:
        graph: Weighted graph represented as adjacency list
               {vertex: [(neighbor, weight), ...]}
        start: Source vertex
        
    Returns:
        dict: Dictionary mapping vertex to shortest distance from start
        dict: Dictionary mapping vertex to previous vertex in shortest path
        
    Time Complexity: O(V²) with simple implementation
    Space Complexity: O(V)
    """
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            vertices.add(neighbor)
    
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0
    previous = {vertex: None for vertex in vertices}
    unvisited = set(vertices)
    
    while unvisited:
        # Find vertex with minimum distance
        current = None
        min_distance = float('inf')
        
        for vertex in unvisited:
            if distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current = vertex
        
        if current is None or min_distance == float('inf'):
            break
        
        unvisited.remove(current)
        
        # Update distances of neighbors
        for neighbor, weight in graph.get(current, []):
            if neighbor in unvisited:
                new_distance = distances[current] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
    
    return distances, previous


def dijkstra_priority_queue(graph, start):
    """
    Dijkstra's algorithm using priority queue for better performance
    
    Args:
        graph: Weighted graph represented as adjacency list
        start: Source vertex
        
    Returns:
        dict: Dictionary mapping vertex to shortest distance from start
        dict: Dictionary mapping vertex to previous vertex in shortest path
        
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)
    """
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            vertices.add(neighbor)
    
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0
    previous = {vertex: None for vertex in vertices}
    priority_queue = [(0, start)]
    visited = set()
    
    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        # Update distances of neighbors
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
                    heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances, previous


def dijkstra_shortest_path(graph, start, end):
    """
    Find shortest path between two vertices using Dijkstra's algorithm
    
    Args:
        graph: Weighted graph represented as adjacency list
        start: Source vertex
        end: Target vertex
        
    Returns:
        list: Shortest path from start to end
        float: Total distance of shortest path
        
    Time Complexity: O((V + E) log V) with priority queue
    Space Complexity: O(V)
    """
    distances, previous = dijkstra_priority_queue(graph, start)
    
    if distances[end] == float('inf'):
        return None, float('inf')  # No path exists
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    
    return path[::-1], distances[end]


def dijkstra_all_pairs_shortest_paths(graph):
    """
    Find shortest paths between all pairs of vertices using Dijkstra's algorithm
    
    Args:
        graph: Weighted graph represented as adjacency list
        
    Returns:
        dict: Dictionary mapping (source, destination) to shortest distance
        
    Time Complexity: O(V * (V + E) log V)
    Space Complexity: O(V²)
    """
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            vertices.add(neighbor)
    
    all_pairs = {}
    
    for source in vertices:
        distances, _ = dijkstra_priority_queue(graph, source)
        for destination, distance in distances.items():
            all_pairs[(source, destination)] = distance
    
    return all_pairs


def dijkstra_with_path_reconstruction(graph, start):
    """
    Dijkstra's algorithm with complete path reconstruction
    
    Args:
        graph: Weighted graph represented as adjacency list
        start: Source vertex
        
    Returns:
        dict: Dictionary mapping vertex to shortest path from start
        
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V²) for storing all paths
    """
    distances, previous = dijkstra_priority_queue(graph, start)
    paths = {}
    
    for vertex in distances:
        if distances[vertex] == float('inf'):
            paths[vertex] = None
            continue
        
        # Reconstruct path
        path = []
        current = vertex
        while current is not None:
            path.append(current)
            current = previous[current]
        
        paths[vertex] = path[::-1]
    
    return distances, paths


def dijkstra_modified_for_negative_edges(graph, start):
    """
    Modified Dijkstra's algorithm to handle some negative edges
    (Note: Still doesn't work for negative cycles)
    
    Args:
        graph: Weighted graph that may have some negative edges
        start: Source vertex
        
    Returns:
        dict: Dictionary mapping vertex to shortest distance from start
        dict: Dictionary mapping vertex to previous vertex in shortest path
        
    Time Complexity: O(V * (V + E) log V) - Bellman-Ford approach
    Space Complexity: O(V)
    """
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            vertices.add(neighbor)
    
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0
    previous = {vertex: None for vertex in vertices}
    
    # Bellman-Ford approach for negative edges
    for _ in range(len(vertices) - 1):
        updated = False
        
        for vertex in vertices:
            for neighbor, weight in graph.get(vertex, []):
                if distances[vertex] != float('inf'):
                    new_distance = distances[vertex] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = vertex
                        updated = True
        
        if not updated:
            break
    
    return distances, previous


def dijkstra_analysis():
    """
    Provides complexity analysis for Dijkstra's algorithm
    """
    return {
        'algorithm': "Dijkstra's Shortest Path",
        'time_complexity': {
            'simple_array': 'O(V²)',
            'priority_queue': 'O((V + E) log V)',
            'binary_heap': 'O(E + V log V)'
        },
        'space_complexity': 'O(V)',
        'edge_weight_requirements': 'Non-negative weights only',
        'guarantees': [
            'Finds shortest paths from source to all vertices',
            'Optimal solution for graphs with non-negative weights',
            'Greedy algorithm with optimal substructure'
        ],
        'applications': [
            'GPS navigation systems',
            'Network routing protocols (OSPF)',
            'Flight scheduling',
            'Game pathfinding (A* algorithm variant)',
            'Logistics optimization',
            'Social network analysis'
        ],
        'advantages': [
            'Guaranteed optimal solution',
            'Efficient with priority queue',
            'Works for both directed and undirected graphs',
            'Provides complete shortest path tree'
        ],
        'disadvantages': [
            'Cannot handle negative edge weights',
            'Higher memory usage than some alternatives',
            'May explore unnecessary vertices',
            'Not optimal for single-source single-destination queries'
        ]
    }


def reconstruct_path(previous, start, end):
    """
    Helper function to reconstruct path from previous dictionary
    
    Args:
        previous: Dictionary mapping vertex to previous vertex
        start: Source vertex
        end: Target vertex
        
    Returns:
        list: Path from start to end
    """
    if previous[end] is None and start != end:
        return None
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    
    return path[::-1]


# Example usage and testing
if __name__ == "__main__":
    # Example weighted graph
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 5), ('D', 10)],
        'C': [('E', 3)],
        'D': [('F', 11)],
        'E': [('B', 4), ('D', 4)],
        'F': []
    }
    
    print("=== Dijkstra's Algorithm ===")
    
    # Simple implementation
    distances, previous = dijkstra(graph, 'A')
    print("Simple implementation:")
    for vertex, distance in distances.items():
        print(f"  Distance to {vertex}: {distance}")
    
    # Priority queue implementation
    distances_pq, previous_pq = dijkstra_priority_queue(graph, 'A')
    print("\nPriority queue implementation:")
    for vertex, distance in distances_pq.items():
        print(f"  Distance to {vertex}: {distance}")
    
    print("\n=== Shortest Path ===")
    path, distance = dijkstra_shortest_path(graph, 'A', 'F')
    print(f"Shortest path from 'A' to 'F': {path}")
    print(f"Total distance: {distance}")
    
    print("\n=== Complete Path Reconstruction ===")
    distances_complete, paths = dijkstra_with_path_reconstruction(graph, 'A')
    for vertex, path in paths.items():
        if path:
            print(f"  Path to {vertex}: {path} (distance: {distances_complete[vertex]})")
        else:
            print(f"  No path to {vertex}")
    
    print("\n=== All Pairs Shortest Paths ===")
    all_pairs = dijkstra_all_pairs_shortest_paths(graph)
    for (source, dest), distance in all_pairs.items():
        if distance != float('inf'):
            print(f"  {source} -> {dest}: {distance}")
    
    print("\n=== Graph with Negative Edges ===")
    # Graph with negative edge (but no negative cycles)
    graph_negative = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', -2), ('D', 10)],
        'C': [('E', 3)],
        'D': [('F', 11)],
        'E': [('B', 4), ('D', 4)],
        'F': []
    }
    
    distances_neg, previous_neg = dijkstra_modified_for_negative_edges(graph_negative, 'A')
    print("With negative edges:")
    for vertex, distance in distances_neg.items():
        print(f"  Distance to {vertex}: {distance}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = dijkstra_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
