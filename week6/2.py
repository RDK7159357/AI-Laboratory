from collections import deque

def solve_monkey_banana():
    """Solves the Monkey-Banana problem using Breadth-First Search."""
    # State: (monkey_loc, box_loc, on_box)
    # Locations: 'door', 'window', 'center' (where bananas are)
    initial_state = ('door', 'window', False)
    goal_state = ('center', 'center', True) 
    
    # Queue for BFS, storing tuples of (state, path)
    queue = deque([(initial_state, [initial_state])])
    visited = {initial_state}

    while queue:
        current_state, path = queue.popleft()
        m_loc, b_loc, on_box = current_state
        
        # Check if the goal is reached (monkey is on the box at the center)
        if current_state == goal_state:
            # The final action is to grasp the bananas
            return path

        # --- Generate next possible states based on actions ---

        # Action 1: Walk to a new location (if not on the box)
        if not on_box:
            for loc in ['door', 'window', 'center']:
                if m_loc != loc:
                    # The monkey walks, the box stays put
                    new_state = (loc, b_loc, on_box)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [new_state]))

        # Action 2: Push the box (monkey must be at the box, and not on it)
        if not on_box and m_loc == b_loc:
            for loc in ['door', 'window', 'center']:
                if b_loc != loc:
                    # Monkey and box move together
                    new_state = (loc, loc, on_box)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [new_state]))
        
        # Action 3: Climb on the box (monkey must be at the box)
        if not on_box and m_loc == b_loc:
            new_state = (m_loc, b_loc, True)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None

def interpret_path(path):
    """Converts a sequence of states into a human-readable list of actions."""
    actions = []
    for i in range(len(path) - 1):
        prev_m, prev_b, prev_on = path[i]
        curr_m, curr_b, curr_on = path[i+1]

        if not prev_on and curr_on:
            actions.append(f"Climb on the box at '{curr_m}'")
        elif prev_b != curr_b:
            actions.append(f"Push the box from '{prev_b}' to '{curr_b}'")
        elif prev_m != curr_m:
            actions.append(f"Walk from '{prev_m}' to '{curr_m}'")
    
    actions.append("Grasp the bananas!")
    return actions

if __name__ == "__main__":
    solution_path = solve_monkey_banana()
    
    if solution_path:
        print("Solution found! Here are the steps:")
        steps = interpret_path(solution_path)
        for i, step in enumerate(steps):
            print(f"Step {i + 1}: {step}")
    else:
        print("No solution found.")
