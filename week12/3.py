import random

# Environment Class
class Environment:
    def __init__(self):
        self.steps_left = 10 # Game must finish in at most ten steps
    
    def get_observation(self):
        # Current state/observation is fixed
        return [1.0, 2.0, 1.0]
    
    def get_actions(self):
        # Available actions
        return [-1, 1]
    
    def check_is_done(self):
        return self.steps_left == 0
    
    def action(self, action_value):
        if self.check_is_done():
            raise Exception("Game over")
        
        self.steps_left -= 1
        # Returns a random reward (0.0 to 1.0)
        return random.random()

# Agent Class
class Agent:
    def __init__(self):
        self.total_rewards = 0.0
    
    def step(self, ob: Environment):
        # 1. Get observation/state
        curr_obs = ob.get_observation()
        # 2. Get available actions
        curr_action = ob.get_actions()
        # 3. Choose a random action
        action_choice = random.choice(curr_action)
        # 4. Take action and get reward
        curr_reward = ob.action(action_choice)
        # 5. Update total rewards
        self.total_rewards += curr_reward

        # Print state, action, and reward summary for that step
        # Note: The original hint's print statements are modified for cleaner output
        print(curr_obs)
        print(action_choice)
        print(f"Total rewards so far= {self.total_rewards:.3f}")

# Main Execution
if __name__ == '__main__':
    obj = Environment()
    agent = Agent()
    step_number = 0
    
    # Loop for exactly 10 steps
    while not obj.check_is_done():
        step_number += 1
        print(f"\nStep- {step_number}")
        agent.step(obj)
    
    print(f"\nTotal reward is {agent.total_rewards:.3f}")