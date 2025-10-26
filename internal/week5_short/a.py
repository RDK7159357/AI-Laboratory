from collections import deque

def water_jug(c1, c2, target):
    visited, queue = set(), deque([((0, 0), [(0, 0)])])
    
    while queue:
        (j1, j2), path = queue.popleft()
        if j1 == target or j2 == target:
            return path
        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))
        
        for state in [
            (c1, j2), (j1, c2), (0, j2), (j1, 0),
            (j1 - min(j1, c2 - j2), j2 + min(j1, c2 - j2)),
            (j1 + min(j2, c1 - j1), j2 - min(j2, c1 - j1))
        ]:
            queue.append((state, path + [state]))
    return None

solution = water_jug(4, 3, 2)
print("Water Jug Solution:")
for step in solution if solution else []:
    print(step)
