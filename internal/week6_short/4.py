from collections import deque

def blocks_rearrange(initial, goal):
    queue = deque([(initial, [])])
    visited = {tuple(sorted(initial.items()))}
    
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        
        on_top = set(state.values())
        clear = {b for b in state if b not in on_top}
        
        for block in clear:
            for dest in ({b for b in state if b != block} | {'table'}):
                if block == dest or (dest != 'table' and dest in on_top):
                    continue
                
                new_state = state.copy()
                new_state[block] = dest
                key = tuple(sorted(new_state.items()))
                
                if key not in visited:
                    visited.add(key)
                    queue.append((new_state, path + [(block, dest)]))
    return None

initial = {'A': 'B', 'B': 'C', 'C': 'table'}
goal = {'A': 'table', 'B': 'A', 'C': 'B'}

solution = blocks_rearrange(initial, goal)
if solution:
    for i, (block, dest) in enumerate(solution):
        print(f"Step {i+1}: Move {block} to {dest}")
else:
    print("No solution")
