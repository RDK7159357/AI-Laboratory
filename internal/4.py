import math

# Sample Game Tree (4 levels: Root -> L3) with 16 leaf scores
SCORES = [3, 5, 6, 9, 1, 2, 0, -1, 8, 7, 4, 2, 9, 10, 11, 12]
PRUNED = [] 
NODE_EVALS = {}
NODE_COUNTER = 0

def alpha_beta_minimax(idx, depth, alpha, beta, is_max):
    """
    Performs Minimax with Alpha-Beta Pruning on a balanced tree.
    (Depth 4: 4=Root, 3=Min, 2=Max, 1=Min, 0=Leaf)
    """
    global PRUNED, NODE_COUNTER
    current_node_id = f"N{NODE_COUNTER}"
    NODE_COUNTER += 1
    
    # Base Case: Leaf node (depth 0)
    if depth == 0:
        return SCORES[idx]

    # MAXIMIZING Player (Even depths: 4, 2)
    if is_max:
        value = -math.inf
        # Assuming 2 children per internal node for this simple indexing
        for i in range(2): 
            child_idx = idx * 2 + i
            value = max(value, alpha_beta_minimax(child_idx, depth - 1, alpha, beta, False))
            
            if value >= beta:
                # Beta Cut-off (Pruning)
                PRUNED.append(f"Cut-off at {current_node_id} (MAX Node): β={beta} exceeded by {value}")
                NODE_EVALS[current_node_id] = value
                return value
            
            alpha = max(alpha, value)
            
        NODE_EVALS[current_node_id] = value
        return value

    # MINIMIZING Player (Odd depths: 3, 1)
    else:
        value = math.inf
        for i in range(2):
            child_idx = idx * 2 + i
            value = min(value, alpha_beta_minimax(child_idx, depth - 1, alpha, beta, True))
            
            if value <= alpha:
                # Alpha Cut-off (Pruning)
                PRUNED.append(f"Cut-off at {current_node_id} (MIN Node): α={alpha} exceeded by {value}")
                return value
                
            beta = min(beta, value)
            
        NODE_EVALS[current_node_id] = value
        return value

# --- EXECUTION ---
# Start depth 4 for a 3-level decision tree + 1 level of leaves
# The root node will be N0.
ROOT_VALUE = alpha_beta_minimax(0, 4, -math.inf, math.inf, True)

print("--- ALPHA-BETA PRUNING RESULT ---")
print(f"\n1. Minimax Value of the Root Node (N0): {ROOT_VALUE}")

print("\n2. Each Node Evaluation (Internal Nodes only):")
# Output the calculated value for each internal node
for name, val in NODE_EVALS.items():
    print(f"  {name}: {val}")

print("\n3. The nodes/branches that are Pruned:")
print(f"  Total Pruned Branches: {len(PRUNED)}")
for p in PRUNED:
    print(f"  * {p}")