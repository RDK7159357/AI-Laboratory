import heapq

def best_first_search(graph, start_node, goal_node, heuristics):
    """
    Performs the Best-First Search algorithm on a graph.

    Args:
        graph (dict): A dictionary representing the graph's adjacency list.
        start_node (str): The starting node.
        goal_node (str): The target node.
        heuristics (dict): A dictionary of heuristic values for each node.

    Returns:
        list: The path from the start to the goal node, or None if no path exists.
    """
    # Create 2 lists: OPEN (priority queue) and CLOSED (visited set)
    # The priority queue stores tuples of (heuristic_value, node)
    open_list = [(heuristics[start_node], start_node)]
    closed_set = set()
    
    # Dictionary to store the parent of each node for path reconstruction
    parent_map = {start_node: None}

    # Repeat until the GOAL node is reached or the OPEN list is empty
    while open_list:
        # If the OPEN list is empty, then EXIT the loop returning 'False'
        # This is handled by the while loop condition.

        # Select the first/top node (lowest heuristic) in the OPEN list
        _, current_node = heapq.heappop(open_list)

        # If N is a GOAL node, the solution is found
        if current_node == goal_node:
            path = []
            node = goal_node
            # Backtrack the path from goal to start using the parent map
            while node is not None:
                path.append(node)
                node = parent_map[node]
            return path[::-1] # Return the reversed path

        # Move the current node to the CLOSED list
        closed_set.add(current_node)
        
        # Expand node N to generate the 'immediate' next nodes
        for neighbor in graph.get(current_node, []):
            if neighbor not in closed_set:
                # Check if neighbor is already in the priority queue to avoid duplicates
                in_open_list = any(neighbor == item[1] for item in open_list)
                if not in_open_list:
                    # Add neighbor to the OPEN list
                    parent_map[neighbor] = current_node
                    # The evaluation function f(n) is the heuristic h(n)
                    heapq.heappush(open_list, (heuristics[neighbor], neighbor))

    # If the loop finishes, no path was found
    return None

# --- Sample Usage ---

# 1. Initialize the graph and heuristic function
graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# Heuristic values (estimated distance to goal 'G')
heuristic_values = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'F': 2,
    'G': 0,
    'H': 3
}

start = 'A'
goal = 'G'

# 2. Perform the best-first search
solution_path = best_first_search(graph_data, start, goal, heuristic_values)

# 3. Return the solution
if solution_path:
    print(f"✅ Path found from '{start}' to '{goal}':")
    print(" -> ".join(solution_path))
else:
    print(f"❌ No path found from '{start}' to '{goal}'.")