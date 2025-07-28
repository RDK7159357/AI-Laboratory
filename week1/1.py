import json
import os

class SimpleReflexAgent:
    """
    A Simple Reflex Agent for a two-room vacuum environment.
    The agent's action is based solely on the current percept.
    """
    def __init__(self, env):
        self.location = 'A'  # Agent always starts in Room A
        self.environment = env

    def perceive(self):
        """Senses the current location and its status (Clean/Dirty)."""
        return self.location, self.environment[self.location]

    def act(self, percept):
        """
        Determines the action based on the rule:
        - If Dirty -> Clean
        - If Clean -> Move
        """
        loc, status = percept
        if status == "Dirty":
            # If the current room is dirty, clean it
            self.environment[loc] = "Clean"
            return "Clean"
        else:
            # If the current room is clean, move to the other room
            self.location = 'B' if loc == 'A' else 'A'
            return f"Move to Room {self.location}"

def main():
    """
    Loads the environment, creates the agent, and runs the simulation for 4 steps.
    """
    # Define the environment state and create the JSON file
    env_data = {"A": "Dirty", "B": "Dirty"}
    file_path = "vacuum_environment.json"
    with open(file_path, "w") as f:
        json.dump(env_data, f)

    # Load the environment from the JSON file
    with open(file_path) as f:
        environment = json.load(f)

    agent = SimpleReflexAgent(environment)
    
    print(f"🤖 Initial State: {environment}")
    print(f"Agent starts in Room {agent.location}\n" + "-"*20)

    # Run the agent for 4 steps
    for i in range(4):
        print(f"Step {i+1}:")
        
        # 1. Perceive the environment
        current_loc, current_status = agent.perceive()
        print(f"Percept: In Room '{current_loc}', Status is '{current_status}'")
        
        # 2. Decide and perform an action
        action = agent.act((current_loc, current_status))
        print(f"Action: {action}\n")
    
    print("-"*20 + f"\n🧹 Final State: {agent.environment}")
    
    # Clean up the created JSON file
    os.remove(file_path)

if __name__ == "__main__":
    main()