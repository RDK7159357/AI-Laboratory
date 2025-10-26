import math
# Exercises on Building Games with AI
#a. Minimax Algorithm
class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []

def minimax(node, depth, is_max):
    if depth == 0 or not node.children:
        return node.value
    if is_max:
        return max(minimax(child, depth - 1, False) for child in node.children)
    return min(minimax(child, depth - 1, True) for child in node.children)

def find_best_move(root, depth):
    best_val, best_child = -math.inf, None
    for child in root.children:
        val = minimax(child, depth - 1, False)
        if val > best_val:
            best_val, best_child = val, child
    return best_child, best_val

# Example
A, B, C, D = Node(3), Node(5), Node(2), Node(9)
E, F = Node(children=[A, B]), Node(children=[C, D])
root = Node(children=[E, F])

best, val = find_best_move(root, 2)
print(f"Best minimax value: {val}")
