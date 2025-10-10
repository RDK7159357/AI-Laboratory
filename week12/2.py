import numpy as np
import pylab as pl
import networkx as nx

# --- Step 1 & 2: Define Environment (Graph, Matrix, Goal) ---
# Graph edges: (State_A, State_B, Weight)
edges = [(0, 1), (1, 5), (5, 6), (5, 4), (1, 2), 
         (1, 3), (9, 10), (2, 4), (0, 6), (6, 7), 
         (8, 9), (7, 8), (1, 7), (3, 9)]
goal = 9
MATRIX_SIZE = 11

# Define the Reward Matrix (R)
R = np.ones((MATRIX_SIZE, MATRIX_SIZE)) * -1
for point in edges:
    print(point)
    R[point[0]][point[1]] = 0
    R[point[1]][point[0]] = 0

# Set reward for paths leading to the goal
R[:, goal] = 100
R[goal][goal] = 100
# print(R) # Uncomment to view the R matrix

# --- Step 3: Define Utility Functions ---
gamma = 0.75
Q = np.zeros((MATRIX_SIZE, MATRIX_SIZE))

def available_actions(state):
    # Returns all possible actions (next states) from the current state
    current_state_row = R[state, :]
    available_action = np.where(current_state_row >= 0)[0]
    return available_action

def sample_next_action(available_actions_range):
    # Chooses a random action from available ones
    next_action = int(np.random.choice(available_actions_range, 1)[0])
    return next_action

def update(current_state, action, gamma):
    # The core Q-Learning update rule
    max_index = np.where(Q[action, :] == np.max(Q[action, :]))[0]
    
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1)[0])
    else:
        max_index = int(max_index[0])
        
    max_value = Q[action, max_index]
    
    # Q(s, a) = R(s, a) + gamma * max_a' Q(s', a')
    Q[current_state, action] = R[current_state, action] + gamma * max_value

# --- Step 4: Training Loop ---
scores = []
initial_state = 1 

for i in range(1000):
    # Start at a random state
    current_state = np.random.randint(0, int(Q.shape[0]))
    
    # Loop until the goal is reached
    while current_state != goal:
        available_act = available_actions(current_state)
        action = sample_next_action(available_act)
        
        update(current_state, action, gamma)
        
        current_state = action # Move to the next state
        
    scores.append(np.sum(Q / np.max(Q) * 100))

# --- Step 5: Extracting the Most Efficient Path ---
current_state = initial_state
steps = [current_state]

while current_state != goal:
    # Find the action with the maximum Q-value from the current state
    next_step_index = np.where(Q[current_state, :] == np.max(Q[current_state, :]))[0]

    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index, size=1)[0])
    else:
        next_step_index = int(next_step_index[0])
    
    next_step = next_step_index
    steps.append(next_step)
    current_state = next_step

# --- Step 6: Display Results ---
print("\n--- Q-Learning Results ---")
print("Trained Q-Matrix (normalized for visualization):")
# print(Q / np.max(Q) * 100) # Uncomment to view the Q matrix
print(f"Most efficient path from state {initial_state}: {steps}")

# Plotting the scores
pl.plot(scores)
pl.xlabel('Number of iterations')
pl.ylabel('Reward gained (Score)')
pl.show()