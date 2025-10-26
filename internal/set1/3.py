graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'],
    'D': [], 'E': ['H'], 'F': ['I', 'J'], 'G': ['K', 'L'],
    'H': [], 'I': [], 'J': [], 'K': [], 'L': []
}
# c. Iterative Deepening Techniques
def dls(start, goal, limit, path):
    path.append(start)
    if start == goal:
        return path
    if limit <= 0:
        return None
    for neighbor in graph.get(start, []):
        result = dls(neighbor, goal, limit - 1, path)
        if result:
            return result
    path.pop()
    return None

def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Depth {depth}")
        path = dls(start, goal, depth, [])
        if path:
            print(f"Found: {' -> '.join(path)}")
            return path
    print("No solution found")
    return None

iddfs('A', 'H', 5)
