import heapq

def a_star_search(graph, start_node, goal_node, heuristics):
    """
    Implements the A* algorithm to find the shortest path in a weighted graph.

    Args:
        graph (dict): A dictionary representing the graph. 
                      Format: {'node': [('neighbor', cost), ...]}
        start_node (str): The starting node.
        goal_node (str): The target node.
        heuristics (dict): A dictionary of heuristic values for each node.

    Returns:
        tuple: A tuple containing the optimal path (list) and its total cost (int),
               or (None, None) if no path exists.
    """
    # Priority queue to store nodes to visit. Format: (f_cost, g_cost, node, path)
    # f_cost = g_cost + h_cost
    open_list = [(heuristics[start_node], 0, start_node, [start_node])]
    
    # Set to store visited nodes to avoid cycles and redundant computations
    visited = set()

    while open_list:
        # Pop the node with the lowest f_cost
        f_cost, g_cost, current_node, path = heapq.heappop(open_list)

        # If the goal is reached, return the path and total cost
        if current_node == goal_node:
            return path, g_cost

        # If we have already visited this node with a lower or equal f_cost, skip it
        if current_node in visited:
            continue
        
        # Mark the current node as visited
        visited.add(current_node)

        # Explore the neighbors
        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                # Calculate the new costs
                new_g_cost = g_cost + cost
                h_cost = heuristics.get(neighbor, float('inf')) # Heuristic for the neighbor
                new_f_cost = new_g_cost + h_cost
                
                # Add the neighbor to the open list with its new costs and path
                new_path = path + [neighbor]
                heapq.heappush(open_list, (new_f_cost, new_g_cost, neighbor, new_path))
    
    # If the loop finishes, no path was found
    return None, None

# --- Sample Usage ---

# 1. Define the graph with nodes, neighbors, and costs
# This is a weighted graph
graph_data = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 4)],
    'F': [('G', 1)],
    'G': []
}

# 2. Define the heuristic values (estimated distance to goal 'G')
heuristic_values = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 10,
    'E': 3,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'

# 3. Perform the A* search
optimal_path, total_cost = a_star_search(graph_data, start, goal, heuristic_values)

# 4. Return the solution
if optimal_path:
    print(f"✅ Shortest path found from '{start}' to '{goal}':")
    print(f"   Path: {' -> '.join(optimal_path)}")
    print(f"   Total Cost: {total_cost}")
else:
    print(f"❌ No path found from '{start}' to '{goal}'.")