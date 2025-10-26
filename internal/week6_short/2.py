from collections import deque

def monkey_banana():
    initial = ('door', 'window', False)
    goal = ('center', 'center', True)
    queue = deque([(initial, [initial])])
    visited = {initial}

    while queue:
        (m, b, on), path = queue.popleft()
        if (m, b, on) == goal:
            return path
        
        # Walk
        if not on:
            for loc in ['door', 'window', 'center']:
                if m != loc:
                    state = (loc, b, on)
                    if state not in visited:
                        visited.add(state)
                        queue.append((state, path + [state]))
        
        # Push box
        if not on and m == b:
            for loc in ['door', 'window', 'center']:
                if b != loc:
                    state = (loc, loc, on)
                    if state not in visited:
                        visited.add(state)
                        queue.append((state, path + [state]))
        
        # Climb
        if not on and m == b:
            state = (m, b, True)
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None

path = monkey_banana()
if path:
    for i, s in enumerate(path):
        print(f"Step {i}: {s}")
    print("Grasp bananas!")
