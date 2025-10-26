from collections import deque

def solve_jugs(cap_a, cap_b, target):
    """
    Finds the shortest path for the Water Jug Problem using BFS.
    Goal: get 'target' amount in jug 'a'.
    """
    q = deque([((0, 0), [(0, 0)])]) 
    visited = set([(0, 0)])
    
    while q:
        (x, y), path = q.popleft()
        if x == target: return path

        # The 6 fundamental state transitions (R1-R6 combined)
        next_states = [
            (cap_a, y), # Fill A
            (x, cap_b), # Fill B
            (0, y),     # Empty A
            (x, 0),     # Empty B
            (x + min(y, cap_a - x), y - min(y, cap_a - x)), # Pour B to A
            (x - min(x, cap_b - y), y + min(x, cap_b - y))  # Pour A to B
        ]
        
        for state in next_states:
            if state not in visited and 0 <= state[0] <= cap_a and 0 <= state[1] <= cap_b:
                visited.add(state)
                q.append((state, path + [state]))
    return "No solution."

# --- EXECUTION ---
JUG_A, JUG_B, TARGET = 4, 3, 2

solution_path = solve_jugs(JUG_A, JUG_B, TARGET)

print(f"--- WATER JUG PROBLEM ({JUG_A}, {JUG_B}, Target {TARGET}) ---")
if solution_path != "No solution.":
    print("Shortest Solution Path (A, B):")
    for step, state in enumerate(solution_path):
        print(f"Step {step}: {state}")
else:
    print(solution_path)
