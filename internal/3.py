def ao_star_recursive(graph, node):
    """
    Finds the optimal cost and path for a goal-reduction (AND/OR) graph.
    """
    if node not in graph:
        return 0, {node: []} # Base case: primitive node
        
    min_cost = float('inf')
    best_path = {}
    
    # Iterate through OR alternatives
    for sub_problems in graph[node]:
        current_cost = 0
        path_segment = []
        
        # Calculate cost for AND conjunction (sum of sub-problem costs)
        for successor, cost in sub_problems:
            g_cost, sub_path = ao_star_recursive(graph, successor)
            current_cost += cost + g_cost # f(n) = cost(action) + SUM(f(successors))
            path_segment.append(successor)
        
        # Choose the best OR alternative
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = {node: path_segment}
            
    return min_cost, best_path

# --- EXAMPLE DATA (Tea-Making Problem) ---
# A=Tea Ready, B=Black Tea (AND), C=Milk Tea (AND)
TEA_GRAPH = {
    'A': [
        [('B', 0)],  # OR choice 1: Black Tea Path (Cost 0 to choose)
        [('C', 0)]   # OR choice 2: Milk Tea Path (Cost 0 to choose)
    ],
    'B': [
        [('BoilWater', 1), ('AddLeaves', 1)] # AND: Cost 1 + 1 = 2
    ],
    'C': [
        [('BoilMilk', 2), ('AddLeaves', 1), ('AddSugar', 0)] # AND: Cost 2 + 1 + 0 = 3
    ],
    # Primitives (BoilWater, AddLeaves, etc.) are implicitly terminal
}

# --- EXECUTION ---
START_NODE = 'A'
optimal_cost, optimal_graph = ao_star_recursive(TEA_GRAPH, START_NODE)

print("--- AO* ALGORITHM (Tea-Making) ---")
print(f"Optimal Cost to complete task '{START_NODE}': {optimal_cost}")
print("Optimal Solution Graph (AND/OR choices):")

# Simple printing function for the optimal path
def print_graph(node, graph, indent=0):
    if node not in graph:
        print("  " * indent + f"-> {node} (Primitive)")
        return
    
    successors = graph[node]
    if successors:
        print("  " * indent + f"-> {node} (AND choice to:)")
        for successor in successors:
            print_graph(successor, graph, indent + 1)
            
print_graph(START_NODE, optimal_graph)
