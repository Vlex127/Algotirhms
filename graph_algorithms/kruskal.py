"""
Kruskal's Minimum Spanning Tree Algorithm

Time Complexity:
- O(E log E) - for sorting edges
- O(E log V) - using union-find with path compression
- O(V + E log E) - overall complexity

Space Complexity: O(V + E) - for storing edges and union-find structure

Algorithm Description:
Kruskal's algorithm finds a minimum spanning tree (MST) for a weighted,
undirected graph. It uses a greedy approach by sorting all edges by weight
and adding them to the MST if they don't create a cycle.

Applications:
- Network design
- Circuit design
- Clustering algorithms
- Image segmentation
- Transportation networks
"""

class UnionFind:
    """
    Union-Find (Disjoint Set) data structure with path compression
    and union by rank optimizations
    """
    
    def __init__(self, vertices):
        """
        Initialize Union-Find structure
        
        Args:
            vertices: Set of vertices
        """
        self.parent = {}
        self.rank = {}
        
        for vertex in vertices:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0
    
    def find(self, vertex):
        """
        Find the root of the set containing vertex
        with path compression optimization
        
        Args:
            vertex: Vertex to find
            
        Returns:
            Root of the set
        """
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, vertex1, vertex2):
        """
        Union two sets containing vertex1 and vertex2
        with union by rank optimization
        
        Args:
            vertex1: First vertex
            vertex2: Second vertex
            
        Returns:
            bool: True if union was performed, False if already in same set
        """
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if root1 == root2:
            return False  # Already in same set
        
        # Union by rank
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        return True


def kruskal_mst(graph):
    """
    Find Minimum Spanning Tree using Kruskal's algorithm
    
    Args:
        graph: Weighted undirected graph represented as adjacency list
               {vertex: [(neighbor, weight), ...]}
               
    Returns:
        list: List of edges in MST [(u, v, weight), ...]
        int: Total weight of MST
        
    Time Complexity: O(E log E)
    Space Complexity: O(V + E)
    """
    # Collect all edges
    edges = []
    vertices = set(graph.keys())
    
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            # Add edge only once (since it's undirected)
            if (neighbor, vertex, weight) not in edges:
                edges.append((vertex, neighbor, weight))
            vertices.add(neighbor)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize Union-Find structure
    union_find = UnionFind(vertices)
    
    mst_edges = []
    total_weight = 0
    
    for edge in edges:
        vertex1, vertex2, weight = edge
        
        # Check if adding this edge creates a cycle
        if union_find.union(vertex1, vertex2):
            mst_edges.append(edge)
            total_weight += weight
            
            # Stop when we have V-1 edges
            if len(mst_edges) == len(vertices) - 1:
                break
    
    return mst_edges, total_weight


def kruskal_mst_with_details(graph):
    """
    Kruskal's algorithm with detailed step-by-step information
    
    Args:
        graph: Weighted undirected graph represented as adjacency list
        
    Returns:
        dict: Detailed information about MST construction
    """
    # Collect all edges
    edges = []
    vertices = set(graph.keys())
    
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            if (neighbor, vertex, weight) not in edges:
                edges.append((vertex, neighbor, weight))
            vertices.add(neighbor)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    union_find = UnionFind(vertices)
    mst_edges = []
    rejected_edges = []
    total_weight = 0
    steps = []
    
    step_count = 1
    for edge in edges:
        vertex1, vertex2, weight = edge
        
        steps.append({
            'step': step_count,
            'edge': edge,
            'weight': weight,
            'action': 'Processing'
        })
        
        if union_find.union(vertex1, vertex2):
            mst_edges.append(edge)
            total_weight += weight
            steps[-1]['action'] = 'Added to MST'
            steps[-1]['mst_size'] = len(mst_edges)
        else:
            rejected_edges.append(edge)
            steps[-1]['action'] = 'Rejected (creates cycle)'
        
        step_count += 1
        
        # Stop when we have V-1 edges
        if len(mst_edges) == len(vertices) - 1:
            break
    
    return {
        'mst_edges': mst_edges,
        'total_weight': total_weight,
        'rejected_edges': rejected_edges,
        'steps': steps,
        'num_vertices': len(vertices),
        'num_edges_processed': len(mst_edges) + len(rejected_edges)
    }


def kruskal_check_connectivity(graph):
    """
    Check if graph is connected before applying Kruskal's algorithm
    
    Args:
        graph: Graph represented as adjacency list
        
    Returns:
        bool: True if graph is connected, False otherwise
    """
    if not graph:
        return True
    
    # Use DFS to check connectivity
    visited = set()
    start = next(iter(graph.keys()))
    
    def dfs(vertex):
        visited.add(vertex)
        for neighbor, _ in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
    
    dfs(start)
    
    # Check if all vertices are reachable
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            vertices.add(neighbor)
    
    return len(visited) == len(vertices)


def kruskal_mst_complete(graph):
    """
    Complete Kruskal's algorithm with connectivity check and error handling
    
    Args:
        graph: Weighted undirected graph represented as adjacency list
        
    Returns:
        dict: Complete MST information or error details
    """
    result = {
        'success': False,
        'mst_edges': None,
        'total_weight': None,
        'error': None
    }
    
    # Check if graph is empty
    if not graph:
        result['error'] = 'Empty graph'
        return result
    
    # Check connectivity
    if not kruskal_check_connectivity(graph):
        result['error'] = 'Graph is not connected - MST cannot be formed'
        return result
    
    try:
        mst_edges, total_weight = kruskal_mst(graph)
        result['success'] = True
        result['mst_edges'] = mst_edges
        result['total_weight'] = total_weight
    except Exception as e:
        result['error'] = str(e)
    
    return result


def kruskal_analysis():
    """
    Provides complexity analysis for Kruskal's algorithm
    """
    return {
        'algorithm': "Kruskal's Minimum Spanning Tree",
        'time_complexity': 'O(E log E)',
        'space_complexity': 'O(V + E)',
        'graph_type': 'Weighted, undirected, connected',
        'data_structures': ['Union-Find (Disjoint Set)', 'Sorting'],
        'guarantees': [
            'Produces minimum weight spanning tree',
            'Works for any connected weighted graph',
            'Greedy algorithm with optimal solution'
        ],
        'applications': [
            'Network design and optimization',
            'Circuit board design',
            'Transportation networks',
            'Clustering algorithms',
            'Image segmentation',
            'Telecommunication networks'
        ],
        'advantages': [
            'Simple to implement',
            'Guaranteed optimal solution',
            'Works well for sparse graphs',
            'Easy to understand and debug'
        ],
        'disadvantages': [
            'Requires sorting all edges',
            'Less efficient for dense graphs',
            'Union-Find overhead',
            'Memory intensive for large graphs'
        ]
    }


def mst_to_adjacency_list(mst_edges):
    """
    Convert MST edges to adjacency list representation
    
    Args:
        mst_edges: List of edges in MST [(u, v, weight), ...]
        
    Returns:
        dict: Adjacency list representation of MST
    """
    mst_graph = {}
    
    for u, v, weight in mst_edges:
        if u not in mst_graph:
            mst_graph[u] = []
        if v not in mst_graph:
            mst_graph[v] = []
        
        mst_graph[u].append((v, weight))
        mst_graph[v].append((u, weight))
    
    return mst_graph


# Example usage and testing
if __main__ == "__main__":
    # Example weighted undirected graph
    graph = {
        'A': [('B', 4), ('C', 3), ('D', 1)],
        'B': [('A', 4), ('C', 2), ('D', 5)],
        'C': [('A', 3), ('B', 2), ('D', 6)],
        'D': [('A', 1), ('B', 5), ('C', 6)]
    }
    
    print("=== Kruskal's MST Algorithm ===")
    
    # Basic MST
    mst_edges, total_weight = kruskal_mst(graph)
    print(f"MST edges: {mst_edges}")
    print(f"Total weight: {total_weight}")
    
    # MST as adjacency list
    mst_graph = mst_to_adjacency_list(mst_edges)
    print(f"MST adjacency list: {mst_graph}")
    
    print("\n=== Detailed MST Construction ===")
    details = kruskal_mst_with_details(graph)
    print(f"Number of vertices: {details['num_vertices']}")
    print(f"Edges processed: {details['num_edges_processed']}")
    
    print("\nConstruction steps:")
    for step in details['steps']:
        print(f"  Step {step['step']}: Edge {step['edge']} (weight: {step['weight']}) - {step['action']}")
    
    print(f"\nRejected edges: {details['rejected_edges']}")
    
    print("\n=== Connectivity Check ===")
    # Connected graph
    is_connected = kruskal_check_connectivity(graph)
    print(f"Graph is connected: {is_connected}")
    
    # Disconnected graph
    disconnected_graph = {
        'A': [('B', 1)],
        'B': [('A', 1)],
        'C': [('D', 2)],
        'D': [('C', 2)]
    }
    is_disconnected = kruskal_check_connectivity(disconnected_graph)
    print(f"Disconnected graph is connected: {is_disconnected}")
    
    print("\n=== Complete MST Algorithm ===")
    complete_result = kruskal_mst_complete(graph)
    print(f"Success: {complete_result['success']}")
    if complete_result['success']:
        print(f"MST: {complete_result['mst_edges']}")
        print(f"Weight: {complete_result['total_weight']}")
    
    disconnected_result = kruskal_mst_complete(disconnected_graph)
    print(f"Disconnected graph - Success: {disconnected_result['success']}")
    print(f"Error: {disconnected_result['error']}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = kruskal_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
