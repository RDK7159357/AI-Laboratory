from collections import deque

def solve_blocks_rearrangement(initial_state, goal_state):
    """
    Solves the Blocks Rearrangement Problem using Breadth-First Search.
    
    Args:
        initial_state (dict): The starting configuration of the blocks.
        goal_state (dict): The target configuration.
    
    Returns:
        list: A sequence of moves (tuples) to reach the goal, or None if no solution exists.
    """
    queue = deque([(initial_state, [])])
    # Visited set stores hashable tuples of the state dictionary items
    visited = {tuple(sorted(initial_state.items()))}
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path
            
        # Find all blocks that have nothing on top of them
        on_top_values = set(current_state.values())
        clear_blocks = {b for b in current_state if b not in on_top_values}
        
        for block_to_move in clear_blocks:
            # Possible destinations are other blocks or the table
            possible_destinations = {b for b in current_state if b != block_to_move} | {'table'}
            
            for destination in possible_destinations:
                # A block cannot be moved onto itself
                if block_to_move == destination:
                    continue

                # A block cannot be moved onto a block that is not clear
                # This check must be done on the CURRENT state
                if destination != 'table' and destination in on_top_values:
                    continue

                # Create the new state after the move
                new_state = current_state.copy()
                new_state[block_to_move] = destination
                
                new_state_tuple = tuple(sorted(new_state.items()))
                
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    new_path = path + [(block_to_move, destination)]
                    queue.append((new_state, new_path))
    
    return None

if __name__ == '__main__':
    # State is represented as a dictionary where key is the block
    # and value is what it's on top of ('table' for the table).
    initial_state = {'A': 'B', 'B': 'C', 'C': 'table'}
    goal_state = {'A': 'table', 'B': 'A', 'C': 'B'}

    print("Initial State:", initial_state)
    print("Goal State:", goal_state)
    
    solution_path = solve_blocks_rearrangement(initial_state, goal_state)
    
    if solution_path:
        print("\nSolution found!")
        for i, move in enumerate(solution_path):
            print(f"Step {i+1}: Move block {move[0]} to {move[1]}")
    else:
        print("\nNo solution found.")