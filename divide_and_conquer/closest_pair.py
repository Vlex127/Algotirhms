"""
Closest Pair of Points - Divide and Conquer Algorithm

Time Complexity: O(n log n)
Space Complexity: O(n)

Algorithm Description:
Finds the closest pair of points in a 2D plane using divide and conquer.
The algorithm sorts points by x-coordinate, recursively divides the plane,
and combines results with a linear scan of the strip around the dividing line.
"""

import math


def closest_pair_of_points(points):
    """
    Find closest pair of points using divide and conquer
    
    Args:
        points: List of (x, y) tuples
        
    Returns:
        tuple: ((x1, y1), (x2, y2), distance)
    """
    if len(points) < 2:
        return None
    
    # Sort points by x-coordinate
    points_sorted_x = sorted(points, key=lambda p: p[0])
    
    return closest_pair_recursive(points_sorted_x)


def closest_pair_recursive(points_x):
    """Recursive divide and conquer implementation"""
    n = len(points_x)
    
    # Base case - brute force for small number of points
    if n <= 3:
        return brute_force_closest(points_x)
    
    # Divide
    mid = n // 2
    mid_x = points_x[mid][0]
    
    left_points = points_x[:mid]
    right_points = points_x[mid:]
    
    # Conquer
    left_result = closest_pair_recursive(left_points)
    right_result = closest_pair_recursive(right_points)
    
    # Find the minimum distance from left and right
    if left_result and right_result:
        min_result = left_result if left_result[2] < right_result[2] else right_result
    elif left_result:
        min_result = left_result
    elif right_result:
        min_result = right_result
    else:
        return None
    
    min_dist = min_result[2]
    
    # Combine - check points in the strip
    strip_points = [p for p in points_x if abs(p[0] - mid_x) < min_dist]
    strip_result = strip_closest(strip_points, min_dist)
    
    if strip_result and strip_result[2] < min_dist:
        return strip_result
    
    return min_result


def brute_force_closest(points):
    """Brute force approach for small number of points"""
    min_dist = float('inf')
    closest_pair = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j], dist)
    
    return closest_pair


def strip_closest(strip_points, min_dist):
    """Check for closest pair in the strip"""
    strip_points.sort(key=lambda p: p[1])  # Sort by y-coordinate
    
    min_result = None
    
    for i in range(len(strip_points)):
        for j in range(i + 1, min(i + 7, len(strip_points))):
            dist = euclidean_distance(strip_points[i], strip_points[j])
            if dist < min_dist:
                min_dist = dist
                min_result = (strip_points[i], strip_points[j], dist)
    
    return min_result


def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


if __name__ == "__main__":
    # Example usage
    points = [
        (2, 3), (12, 30), (40, 50), (5, 1),
        (12, 10), (3, 4), (10, 15), (8, 9)
    ]
    
    result = closest_pair_of_points(points)
    if result:
        p1, p2, dist = result
        print(f"Closest pair: {p1} and {p2}")
        print(f"Distance: {dist:.4f}")
    else:
        print("No pair found")
