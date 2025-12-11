"""
Activity Selection Problem - Greedy Algorithm

Time Complexity: O(n log n) - for sorting activities
Space Complexity: O(n) - for storing selected activities

Algorithm Description:
Activity selection problem selects the maximum number of non-overlapping
activities that can be performed by a single person. The greedy approach
always selects the activity with the earliest finish time that doesn't
conflict with previously selected activities.
"""

def activity_selection(activities):
    """
    Solve activity selection problem using greedy algorithm
    
    Args:
        activities: List of tuples (start_time, end_time, name)
        
    Returns:
        list: Selected activities in order
    """
    # Sort activities by end time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    selected = []
    last_finish = -float('inf')
    
    for activity in sorted_activities:
        start, end, name = activity
        if start >= last_finish:
            selected.append(activity)
            last_finish = end
    
    return selected


def activity_selection_with_times(start_times, end_times):
    """
    Activity selection with separate start and end time arrays
    
    Args:
        start_times: List of start times
        end_times: List of end times
        
    Returns:
        list: Indices of selected activities
    """
    activities = list(zip(start_times, end_times, range(len(start_times))))
    selected = activity_selection(activities)
    return [activity[2] for activity in selected]


if __name__ == "__main__":
    # Example usage
    activities = [
        (1, 4, "A1"),
        (3, 5, "A2"), 
        (0, 6, "A3"),
        (5, 7, "A4"),
        (3, 9, "A5"),
        (5, 9, "A6"),
        (6, 10, "A7"),
        (8, 11, "A8"),
        (8, 12, "A9"),
        (2, 14, "A10"),
        (12, 16, "A11")
    ]
    
    selected = activity_selection(activities)
    print("Selected activities:")
    for activity in selected:
        print(f"  {activity[2]}: {activity[0]} - {activity[1]}")
