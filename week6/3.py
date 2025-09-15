from simpleai.search import astar, SearchProblem

class EightPuzzleProblem(SearchProblem):
    """A class to solve the 8-puzzle problem using A* search."""
    def __init__(self, initial_state):
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        super().__init__(initial_state=initial_state)

    def actions(self, state):
        """Returns a list of possible actions (swaps) from the current state."""
        empty_index = state.index(0)
        row, col = divmod(empty_index, 3)
        possible_actions = []
        if row > 0: possible_actions.append('up')
        if row < 2: possible_actions.append('down')
        if col > 0: possible_actions.append('left')
        if col < 2: possible_actions.append('right')
        return possible_actions

    def result(self, state, action):
        """Returns the resulting state after applying an action."""
        empty_index = state.index(0)
        state_list = list(state)
        
        if action == 'up': swap_index = empty_index - 3
        elif action == 'down': swap_index = empty_index + 3
        elif action == 'left': swap_index = empty_index - 1
        elif action == 'right': swap_index = empty_index + 1
        
        state_list[empty_index], state_list[swap_index] = state_list[swap_index], state_list[empty_index]
        return tuple(state_list)

    def is_goal(self, state):
        """Checks if the current state is the goal state."""
        return state == self.goal_state

    def heuristic(self, state):
        """Calculates the Manhattan distance heuristic."""
        distance = 0
        for num in range(1, 9):
            current_index = state.index(num)
            goal_index = self.goal_state.index(num)
            
            current_row, current_col = divmod(current_index, 3)
            goal_row, goal_col = divmod(goal_index, 3)
            
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

if __name__ == "__main__":
    # Convert the 2D initial state to a 1D tuple for the problem
    initial_state_2d = [[2, 0, 3], [1, 4, 6], [7, 5, 8]]
    initial_state = tuple(item for sublist in initial_state_2d for item in sublist)
    
    # Create the problem instance
    problem = EightPuzzleProblem(initial_state)

    # Solve the problem using A* search
    result = astar(problem, graph_search=True)

    # Print the solution path and states
    if result:
        print("Solution found!")
        print(f"Total steps: {len(result.path()) - 1}")
        for i, (action, state) in enumerate(result.path()):
            print(f"Step {i}: {action or 'Initial'}")
            print(f"  {state[0]} {state[1]} {state[2]}")
            print(f"  {state[3]} {state[4]} {state[5]}")
            print(f"  {state[6]} {state[7]} {state[8]}")
            print("-" * 10)
    else:
        print("No solution found.")
