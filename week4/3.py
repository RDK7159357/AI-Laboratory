# A simple graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': ['I', 'J'],
    'G': ['K', 'L'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': []
}

def dls(start, goal, limit, path):
    """
    Depth-Limited Search (DLS)
    """
    # Append the current node to the path and check if it's the goal.
    path.append(start)
    if start == goal:
        return path

    # If the depth limit is reached, stop searching this path.
    if limit <= 0:
        return None

    # Explore neighbors.
    for neighbor in graph.get(start, []):
        # Recursively call DLS with a reduced depth limit.
        result = dls(neighbor, goal, limit - 1, path)
        if result:
            return result
    
    # Backtrack by removing the current node from the path.
    path.pop()
    return None

def iterative_deepening_dfs(start_node, goal_node, max_depth):
    """
    Iterative Deepening Depth-First Search (IDDFS)
    """
    for depth in range(max_depth + 1):
        print(f"Searching with depth limit: {depth}")
        path = dls(start_node, goal_node, depth, [])
        if path:
            print(f"Found solution at depth {depth}: {' -> '.join(path)}")
            return path
    
    print("No solution found within the maximum depth.")
    return None

# --- Example Usage ---
start_node = 'A'
goal_node = 'H'
max_depth = 5

solution = iterative_deepening_dfs(start_node, goal_node, max_depth)