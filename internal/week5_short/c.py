from simpleai.search import astar, SearchProblem

class EightPuzzle(SearchProblem):
    def __init__(self, initial):
        self.goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        super().__init__(initial)

    def actions(self, state):
        idx = state.index(0)
        r, c = divmod(idx, 3)
        acts = []
        if r > 0: acts.append('up')
        if r < 2: acts.append('down')
        if c > 0: acts.append('left')
        if c < 2: acts.append('right')
        return acts

    def result(self, state, action):
        idx = state.index(0)
        swap = {'up': idx-3, 'down': idx+3, 'left': idx-1, 'right': idx+1}[action]
        s = list(state)
        s[idx], s[swap] = s[swap], s[idx]
        return tuple(s)

    def is_goal(self, state):
        return state == self.goal

    def heuristic(self, state):
        dist = 0
        for num in range(1, 9):
            ci, gi = state.index(num), self.goal.index(num)
            dist += abs(ci//3 - gi//3) + abs(ci%3 - gi%3)
        return dist

initial = (2, 0, 3, 1, 4, 6, 7, 5, 8)
result = astar(EightPuzzle(initial), graph_search=True)

if result:
    print(f"8-Puzzle Solution: {len(result.path())-1} steps")
    for i, (action, state) in enumerate(result.path()):
        print(f"Step {i}: {action or 'Initial'}")
        print(f"{state[0]} {state[1]} {state[2]}\n{state[3]} {state[4]} {state[5]}\n{state[6]} {state[7]} {state[8]}\n")
