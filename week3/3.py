class AOStar:
    def __init__(self, graph, heuristics, start_node):
        """
        Initializes the AO* algorithm solver.

        Args:
            graph (dict): The AND-OR graph structure. 
                          Format: {'Node': [['Child1'], ['Child2', 'Child3'], ...]}
                          Inner lists represent AND-connected nodes.
            heuristics (dict): A dictionary of heuristic h(n) values for each node.
            start_node (str): The starting node of the graph.
        """
        self.graph = graph
        self.heuristics = heuristics
        self.start_node = start_node
        # Stores the computed minimum cost for a solution graph rooted at a node.
        self.solution_costs = {}
        # Stores the pointers for the optimal solution graph.
        self.solution_graph = {}

    def search(self):
        """
        Performs the AO* search to find the optimal solution graph.
        """
        self._update_cost(self.start_node)
        print("Optimal solution found. Generating path...")
        self.generate_solution_path(self.start_node)

    def _update_cost(self, node):
        """
        Recursively computes/updates the cost of the solution graph from a given node.
        This is the core of the algorithm, involving expansion and backward propagation.
        """
        # A dictionary to store the costs of all possible OR paths from the current node.
        or_path_costs = {}

        # If the node has no children, it's a terminal node.
        if node not in self.graph:
            self.solution_costs[node] = self.heuristics[node]
            return self.heuristics[node]

        # Iterate through all OR paths for the current node
        for or_path in self.graph[node]:
            # If the path is an AND path (multiple nodes)
            if len(or_path) > 1:
                and_path_key = tuple(or_path)
                and_path_cost = 0
                for child_node in or_path:
                    # Recursively find the cost for each child in the AND path
                    # and add the arc cost (assumed to be 1 here for simplicity)
                    and_path_cost += self._update_cost(child_node) + 1
                or_path_costs[and_path_key] = and_path_cost
            # If the path is a simple OR path (single node)
            else:
                child_node = or_path[0]
                # Recursively find the cost for the child and add the arc cost
                path_cost = self._update_cost(child_node) + 1
                or_path_costs[child_node] = path_cost
        
        # Find the minimum cost among all OR paths
        min_cost = min(or_path_costs.values())
        best_path_key = min(or_path_costs, key=or_path_costs.get)
        
        # Update the total cost and solution graph for the current node
        self.solution_costs[node] = min_cost
        self.solution_graph[node] = best_path_key
        
        # Return the minimum cost for this node
        return min_cost

    def generate_solution_path(self, node):
        """
        Generates and prints the optimal solution path and its total cost.
        """
        print(f"Optimal Cost: {self.solution_costs[self.start_node]}")
        print("Optimal Solution Path:")
        path = []
        self._trace_path(self.start_node, path)
        print(" -> ".join(path))

    def _trace_path(self, node, path):
        """
        Helper function to recursively trace the solution graph.
        """
        path.append(node)
        if node in self.solution_graph:
            best_successor = self.solution_graph[node]
            if isinstance(best_successor, tuple): # AND path
                # For AND paths, we need all children to be satisfied
                and_path = " AND ".join(best_successor)
                path.append(f"({and_path})")
                # Recursively trace each child in the AND path
                for child in best_successor:
                    child_path = []
                    self._trace_path(child, child_path)
                    if len(child_path) > 1:  # Only add if there are further nodes
                        path.extend(child_path[1:])  # Skip the child node itself as it's already in the AND representation
            else: # OR path
                self._trace_path(best_successor, path)


# --- Sample Usage ---

# 1. Define heuristic values, the graph, and the start node
heuristics_data = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}
# In this graph, A can be solved by going to B OR D. B can be solved by going to C OR E.
# D can be solved by going to F AND G.
graph_data = {
    'A': [['B'], ['D']],
    'B': [['C'], ['E']],
    'D': [['F', 'G']],
    'F': [['H']]
}

start = 'A'

# 2. Instantiate and perform the AO* search
ao_star = AOStar(graph_data, heuristics_data, start)
ao_star.search()