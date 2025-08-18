import math

# A simple representation of a game tree node
class Node:
    def __init__(self, value=None, children=None):
        self.value = value  # Static value for leaf nodes
        self.children = children if children else []

def minimax(node, depth, is_maximizing_player):
    """
    Implements the Minimax algorithm to find the optimal value for a given node.

    Args:
        node (Node): The current node in the game tree.
        depth (int): The current search depth.
        is_maximizing_player (bool): True if it's the maximizing player's turn, False otherwise.

    Returns:
        The minimax value of the current node.
    """
    # Base case: If we've reached the end of the search depth or a leaf node
    if depth == 0 or not node.children:
        return node.value

    # Maximizing player's turn
    if is_maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            evaluation = minimax(child, depth - 1, False)
            max_eval = max(max_eval, evaluation)
        return max_eval
    # Minimizing player's turn
    else:
        min_eval = math.inf
        for child in node.children:
            evaluation = minimax(child, depth - 1, True)
            min_eval = min(min_eval, evaluation)
        return min_eval

def find_best_move(root_node, depth):
    """
    Finds the best move (the best successor node) from the root position.

    Args:
        root_node (Node): The starting position.
        depth (int): The maximum search depth.

    Returns:
        A tuple of (best_successor_node, best_minimax_value).
    """
    best_value = -math.inf
    best_successor = None

    # The first level is for the maximizing player
    for child in root_node.children:
        # Evaluate the child's position assuming the opponent (minimizing player) will play optimally
        minimax_value = minimax(child, depth - 1, False)
        
        # If this path leads to a better outcome, update the best move
        if minimax_value > best_value:
            best_value = minimax_value
            best_successor = child
    
    return best_successor, best_value

# --- Example Usage ---

# 1. Define the game tree (the tree from the previous example)
# The leaf nodes with static values
node_A = Node(value=3)
node_B = Node(value=5)
node_C = Node(value=2)
node_D = Node(value=9)

# The intermediate nodes (Min nodes)
node_E = Node(children=[node_A, node_B])  # Min(3, 5) -> 3
node_F = Node(children=[node_C, node_D])  # Min(2, 9) -> 2

# The root node (Max node)
root_node = Node(children=[node_E, node_F]) # Max(3, 2) -> 3

# 2. Find the best move and its estimated value
search_depth = 2  # Our tree has a depth of 2 (from root to leaves)
best_successor_node, best_value = find_best_move(root_node, search_depth)

# 3. Print the results
print("Game Tree:")
print("  Root (Max Player)")
print("  ├── Branch 1 (Min Player)")
print("  │   ├── Leaf A (Value: 3)")
print("  │   └── Leaf B (Value: 5)")
print("  └── Branch 2 (Min Player)")
print("      ├── Leaf C (Value: 2)")
print("      └── Leaf D (Value: 9)")

print("\n--- Minimax Results ---")
print(f"The estimated best minimax value from the root position is: {best_value}")

# To identify which successor node is best, we can check its value or object identity
# In this simple example, we can compare the object itself
if best_successor_node == node_E:
    print("The best successor position is the one leading to Node E.")
elif best_successor_node == node_F:
    print("The best successor position is the one leading to Node F.")