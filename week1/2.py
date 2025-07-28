import random
import json

# --- Agent Definitions ---

class BaseAgent:
    """A base class for all agent types."""
    def __init__(self, locations):
        self.locations = locations

    def act(self, percept):
        """
        The core decision-making function for the agent.
        Must be implemented by subclasses.

        Args:
            percept (tuple): A tuple containing (current_location, status).

        Returns:
            str: The action to take ('Suck', 'Left', 'Right').
        """
        raise NotImplementedError("Subclasses must implement the 'act' method.")

class SimpleReflexAgent(BaseAgent):
    """
    A simple reflex agent that acts based only on the current percept.
    Rule: If Dirty, Suck. If Clean, move to the other room.
    """
    def act(self, percept):
        location, status = percept
        if status == 'Dirty':
            return 'Suck'
        # For a 2-room environment, this logic is simple.
        # For more than 2 rooms, we'll just move right, and left from the end.
        current_index = self.locations.index(location)
        if current_index == len(self.locations) - 1: # If at the last room
             return 'Left'
        else:
             return 'Right'

class RandomAgent(BaseAgent):
    """An agent that chooses its action randomly."""
    def act(self, percept):
        return random.choice(['Suck', 'Left', 'Right'])

class ModelBasedReflexAgent(BaseAgent):
    """
    A model-based reflex agent that maintains an internal state (model)
    of the environment to make more informed decisions.
    """
    def __init__(self, locations):
        super().__init__(locations)
        # The agent's internal model of the world.
        # Initially, the agent knows nothing about the state of the rooms.
        self.model = {loc: 'Unknown' for loc in self.locations}

    def act(self, percept):
        location, status = percept
        # Update the internal model with the new information
        self.model[location] = status

        # Rule 1: If the current location is dirty, clean it.
        if status == 'Dirty':
            return 'Suck'

        # Rule 2: If the current location is clean, but the model contains
        # known dirty rooms, move towards one of them.
        # This is a simplification; a true pathfinding algorithm would be better.
        for loc, state in self.model.items():
            if state == 'Dirty':
                # Move towards the known dirty room
                current_index = self.locations.index(location)
                target_index = self.locations.index(loc)
                if target_index < current_index:
                    return 'Left'
                elif target_index > current_index:
                    return 'Right'

        # Rule 3: If all known rooms are clean, explore.
        # We'll just move randomly to avoid getting stuck.
        return random.choice(['Left', 'Right'])


# --- Environment Definition ---

class VacuumEnvironment:
    """
    Simulates the vacuum cleaner world. Manages state, agent interaction,
    and performance tracking.
    """
    def __init__(self, config):
        print("--- Initializing Environment ---")
        self.max_steps = config.get("max_steps", 10)
        
        # Create location names (e.g., 'A', 'B', 'C', ...)
        self.locations = [chr(ord('A') + i) for i in range(config.get("world_size", 2))]
        
        # Initialize environment state
        self.state = {loc: 'Clean' for loc in self.locations}
        for loc in config.get("dirt_locations", []):
            if loc in self.state:
                self.state[loc] = 'Dirty'
        
        # Initialize agent
        agent_type = config.get("agent_type", "SimpleReflex").lower()
        if agent_type == "random":
            self.agent = RandomAgent(self.locations)
        elif agent_type == "modelbased":
            self.agent = ModelBasedReflexAgent(self.locations)
        else: # Default to SimpleReflex
            self.agent = SimpleReflexAgent(self.locations)
            
        self.agent_location = config.get("agent_start_location", self.locations[0])
        if self.agent_location not in self.locations:
            self.agent_location = self.locations[0]

        # Performance metrics
        self.performance_score = 0
        self.dirt_cleaned = 0
        self.moves_made = 0

        print(f"World Size: {len(self.locations)} locations {self.locations}")
        print(f"Initial State: {self.state}")
        print(f"Agent Type: {self.agent.__class__.__name__}")
        print(f"Agent starts at: '{self.agent_location}'")
        print("--------------------------------\n")

    def get_percept(self):
        """Returns the agent's current perception."""
        return (self.agent_location, self.state[self.agent_location])

    def step(self, action):
        """
        Executes an agent's action and updates the environment and score.
        """
        current_index = self.locations.index(self.agent_location)

        if action == 'Suck':
            if self.state[self.agent_location] == 'Dirty':
                self.state[self.agent_location] = 'Clean'
                self.dirt_cleaned += 1
        elif action == 'Left':
            if current_index > 0:
                self.agent_location = self.locations[current_index - 1]
                self.moves_made += 1
        elif action == 'Right':
            if current_index < len(self.locations) - 1:
                self.agent_location = self.locations[current_index + 1]
                self.moves_made += 1
        # No change in location or score for invalid moves

    def calculate_performance(self):
        """Calculates performance score: each piece of dirt cleaned is +10, each move is -1."""
        return (self.dirt_cleaned * 10) - self.moves_made

    def simulate(self):
        """Runs the main simulation loop."""
        print("--- Starting Simulation ---")
        for step_num in range(1, self.max_steps + 1):
            print(f"Step: {step_num}")
            
            # 1. Agent perceives the environment
            percept = self.get_percept()
            print(f"  Percept: {percept}")

            # 2. Agent decides on an action
            action = self.agent.act(percept)
            print(f"  Action: {action}")

            # 3. Environment updates based on the action
            self.step(action)
            print(f"  New State: {self.state}")
            print(f"  Agent Location: '{self.agent_location}'\n")

            # Check if all rooms are clean
            if all(status == 'Clean' for status in self.state.values()):
                print("All rooms are clean! Ending simulation early.")
                break
        
        print("--- Simulation Finished ---")
        self.performance_score = self.calculate_performance()
        print(f"Final Environment State: {self.state}")
        print("\n--- Performance ---")
        print(f"Dirt Cleaned: {self.dirt_cleaned}")
        print(f"Moves Made: {self.moves_made}")
        print(f"Final Score (Dirt Cleaned * 10 - Moves Made): {self.performance_score}")
        print("-----------------------")


# --- Main Execution ---

def main():
    """Loads config and runs the simulation."""
    try:
        with open("week1/vacuum_config.json") as f:
            config = json.load(f)
        env = VacuumEnvironment(config)
        env.simulate()
    except FileNotFoundError:
        print("Error: vacuum_config.json not found.")
    except json.JSONDecodeError:
        print("Error: vacuum_config.json is not a valid JSON file.")

if __name__ == "__main__":
    main()
