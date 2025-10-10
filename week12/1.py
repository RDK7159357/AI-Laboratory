import random

# Environment Class
class MyEnvironment:
    def __init__(self):
        self.remaining_steps = 20

    def get_observation(self):
        # The state of the environment is fixed
        return [1.0, 2.0, 1.0]

    def get_actions(self):
        # Available actions are fixed
        return [-1, 1]

    def check_is_done(self):
        return self.remaining_steps == 0

    def action(self, action_value):
        if self.check_is_done():
            # In a full environment, this would raise an exception,
            # but we'll return 0 to prevent crashes in this simple model.
            return 0
        
        self.remaining_steps -= 1
        # Reward is a random float between 0.0 and 1.0
        return random.random()

# Agent Class
class myAgent:
    def __init__(self):
        self.total_rewards = 0.0

    def step(self, ob: MyEnvironment, step_num):
        # 1. Get current observation (state)
        curr_obs = ob.get_observation()
        # 2. Get available actions
        curr_action_set = ob.get_actions()
        # 3. Choose a random action
        curr_action = random.choice(curr_action_set)
        # 4. Take action and get reward
        curr_reward = ob.action(curr_action)
        # 5. Update total rewards
        self.total_rewards += curr_reward

        # Print state (observation), action, and reward summary for that step
        print(f"Step- {step_num}")
        print(curr_obs)
        print(curr_action_set) 
        print(f"Total rewards so far= {self.total_rewards:.3f}")

# Main Execution
if __name__ == '__main__':
    obj = MyEnvironment()
    agent = myAgent()
    step_number = 0

    # Run the simulation for 20 steps (while environment is not done)
    while not obj.check_is_done():
        step_number += 1
        agent.step(obj, step_number)

    print(f"\nTotal reward is {agent.total_rewards:.3f}")