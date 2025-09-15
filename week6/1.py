from collections import deque

def water_jug_problem(jug1_cap, jug2_cap, target):
    """
    Solves the Water Jug Problem using Breadth-First Search (BFS).

    Args:
        jug1_cap: The capacity of the first jug.
        jug2_cap: The capacity of the second jug.
        target: The target amount of water in either jug.

    Returns:
        A list of tuples representing the sequence of states to reach the target,
        or None if the target is not reachable.
    """
    # A set to store visited states to avoid cycles and redundant computations.
    visited = set()
    # A queue for BFS, storing tuples of (state, path).
    queue = deque([((0, 0), [(0, 0)])])

    while queue:
        (jug1, jug2), path = queue.popleft()

        # Check if the current state is the goal state.
        if jug1 == target or jug2 == target:
            return path

        # Check if the current state has been visited.
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # Generate all possible next states from the current state.
        # Rule 1: Fill jug 1
        queue.append(((jug1_cap, jug2), path + [(jug1_cap, jug2)]))
        # Rule 2: Fill jug 2
        queue.append(((jug1, jug2_cap), path + [(jug1, jug2_cap)]))
        # Rule 3: Empty jug 1
        queue.append(((0, jug2), path + [(0, jug2)]))
        # Rule 4: Empty jug 2
        queue.append(((jug1, 0), path + [(jug1, 0)]))

        # Rule 5: Pour from jug 1 to jug 2
        pour_amount = min(jug1, jug2_cap - jug2)
        new_jug1 = jug1 - pour_amount
        new_jug2 = jug2 + pour_amount
        queue.append(((new_jug1, new_jug2), path + [(new_jug1, new_jug2)]))
        
        # Rule 6: Pour from jug 2 to jug 1
        pour_amount = min(jug2, jug1_cap - jug1)
        new_jug1 = jug1 + pour_amount
        new_jug2 = jug2 - pour_amount
        queue.append(((new_jug1, new_jug2), path + [(new_jug1, new_jug2)]))

    return None

if __name__ == '__main__':
    jug1_capacity = 4
    jug2_capacity = 3
    target_amount = 2

    solution_path = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)

    if solution_path:
        print("Steps to reach the goal:")
        for step in solution_path:
            print(step)
    else:
        print("No solution found.")