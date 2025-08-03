import random, json

class SimpleReflexAgent:
    def __init__(self, locations): self.locations = locations
    def act(self, percept):
        location, status = percept
        if status == 'Dirty': return 'Suck'
        idx = self.locations.index(location)
        return 'Left' if idx == len(self.locations) - 1 else 'Right'

class RandomAgent:
    def __init__(self, locations): self.locations = locations
    def act(self, percept): return random.choice(['Suck', 'Left', 'Right'])

class ModelBasedReflexAgent:
    def __init__(self, locations):
        self.locations = locations
        self.model = {loc: 'Unknown' for loc in locations}
    
    def act(self, percept):
        location, status = percept
        self.model[location] = status
        if status == 'Dirty': return 'Suck'
        for loc, state in self.model.items():
            if state == 'Dirty':
                idx, target = self.locations.index(location), self.locations.index(loc)
                return 'Left' if target < idx else 'Right'
        return random.choice(['Left', 'Right'])

class VacuumEnvironment:
    def __init__(self, config):
        self.max_steps = config.get("max_steps", 10)
        self.locations = [chr(ord('A') + i) for i in range(config.get("world_size", 2))]
        self.state = {loc: 'Dirty' if loc in config.get("dirt_locations", []) else 'Clean' for loc in self.locations}
        
        agent_type = config.get("agent_type", "SimpleReflex").lower()
        self.agent = (RandomAgent if agent_type == "random" else 
                     ModelBasedReflexAgent if agent_type == "modelbased" else 
                     SimpleReflexAgent)(self.locations)
        
        self.agent_location = config.get("agent_start_location", self.locations[0])
        self.dirt_cleaned = self.moves_made = 0
        print(f"World: {self.locations}, State: {self.state}, Agent: {self.agent.__class__.__name__}")

    def step(self, action):
        idx = self.locations.index(self.agent_location)
        if action == 'Suck' and self.state[self.agent_location] == 'Dirty':
            self.state[self.agent_location] = 'Clean'
            self.dirt_cleaned += 1
        elif action == 'Left' and idx > 0:
            self.agent_location = self.locations[idx - 1]
            self.moves_made += 1
        elif action == 'Right' and idx < len(self.locations) - 1:
            self.agent_location = self.locations[idx + 1]
            self.moves_made += 1

    def simulate(self):
        for step in range(1, self.max_steps + 1):
            percept = (self.agent_location, self.state[self.agent_location])
            action = self.agent.act(percept)
            self.step(action)
            print(f"Step {step}: {percept} -> {action} -> {self.state} @ {self.agent_location}")
            if all(s == 'Clean' for s in self.state.values()): break
        print(f"Score: {self.dirt_cleaned * 10 - self.moves_made} (Dirt: {self.dirt_cleaned}, Moves: {self.moves_made})")

if __name__ == "__main__":
    try:
        with open("week1/vacuum_config.json") as f: VacuumEnvironment(json.load(f)).simulate()
    except: print("Error loading config")
