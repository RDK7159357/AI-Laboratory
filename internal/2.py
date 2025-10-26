import heapq

def a_star(graph, h_vals, start, goal):
    """
    Finds the minimum cost path using A* search. f(n) = g(n) + h(n).
    """
    # Priority Queue: (f_cost, g_cost, node, path)
    open_list = [(h_vals[start], 0, start, [start])] 
    g_costs = {n: float('inf') for n in graph}
    g_costs[start] = 0
    
    while open_list:
        _, g_cost, curr, path = heapq.heappop(open_list)
        if curr == goal: return path, g_cost
        
        for neighbor, cost in graph.get(curr, {}).items():
            new_g = g_cost + cost
            if new_g < g_costs[neighbor]:
                g_costs[neighbor] = new_g
                f = new_g + h_vals.get(neighbor, 0) # h(n) of 0 if undefined
                heapq.heappush(open_list, (f, new_g, neighbor, path + [neighbor]))
                
    return None, float('inf')

# --- EXAMPLE DATA (From Q2) ---
GRAPH = {
    'A': {'B': 1, 'C': 4}, 'B': {'D': 3, 'C': 2}, 'C': {'R': 5}, 
    'D': {'F': 2}, 'R': {'G': 3}, 'F': {'G': 4}, 'G': {},
}
HEURISTICS = {
    'A': 5, 'B': 6, 'C': 4, 'D': 3, 'E': 3, 'F': 1, 'I': 1, 'G': 0, 'R': 3
}
START, GOAL = 'A', 'G'

# --- EXECUTION ---
path, cost = a_star(GRAPH, HEURISTICS, START, GOAL)

print("--- A* SEARCH RESULT ---")
if path:
    print(f"Start: {START}, Goal: {GOAL}")
    print(f"Optimal Path: {' -> '.join(path)}")
    print(f"Total Path Cost: {cost}")
else:
    print("Goal is unreachable.")
