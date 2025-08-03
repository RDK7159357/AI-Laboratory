from kanren import run, fact, eq, Relation, var
from kanren.core import lall
import os

# --- Main Execution ---

if __name__ == '__main__':
    # 1. Initialize the relations
    adjacent = Relation()
    coastal = Relation()

    # 2. Define the input files
    file_coastal = './week2/coastal_states.txt'
    file_adjacent = './week2/adjacent_states.txt'

    # Check if data files exist
    if not os.path.exists(file_coastal) or not os.path.exists(file_adjacent):
        print(f"Error: Make sure '{file_coastal}' and '{file_adjacent}' are in the same directory.")
        exit()

    # 3. Load the data and add it to the fact base

    # Read the file containing the coastal states
    with open(file_coastal, 'r') as f:
        line = f.read()
        coastal_states = line.strip().split(',')

    # Add the coastal states info to the fact base
    for state in coastal_states:
        fact(coastal, state)

    # Read the adjacency data from the file
    with open(file_adjacent, 'r') as f:
        adj_info = [line.strip().split(',') for line in f if line.strip()]

    # Add the adjacency information to the fact base
    # Adjacency is a symmetric relationship, so we add both directions
    for state1, state2 in adj_info:
        fact(adjacent, state1, state2)
        fact(adjacent, state2, state1)

    # 4. Initialize the variables for our queries
    x = var()
    y = var()

    print("--- Geography Queries ---")

    # Query 1: Print out all the states that are adjacent to Oregon.
    oregon_adjacent = run(0, x, adjacent('Oregon', x))
    print(f"\nStates adjacent to Oregon: {', '.join(oregon_adjacent)}")

    # Query 2: List all the coastal states that are adjacent to Mississippi.
    # We use lall (logical all) to combine two conditions:
    # - The state 'x' must be adjacent to Mississippi.
    # - The state 'x' must be a coastal state.
    mississippi_adj_coastal = run(0, x, lall(adjacent('Mississippi', x), coastal(x)))
    print(f"\nCoastal states adjacent to Mississippi: {', '.join(mississippi_adj_coastal)}")

    # Query 3: List seven states that border a coastal state.
    # We look for a state 'x' that is adjacent to another state 'y',
    # where 'y' is a coastal state.
    # run(7, x, ...) will limit the output to the first 7 results found.
    bordering_coastal = run(7, x, lall(adjacent(x, y), coastal(y)))
    print(f"\nSeven states that border a coastal state: {', '.join(bordering_coastal)}")

    # Query 4: List states that are adjacent to both Arkansas and Kentucky.
    # We look for a state 'x' that is adjacent to Arkansas AND adjacent to Kentucky.
    adj_ark_and_ky = run(0, x, lall(adjacent('Arkansas', x), adjacent('Kentucky', x)))
    print(f"\nStates adjacent to both Arkansas and Kentucky: {', '.join(adj_ark_and_ky)}")

    print("\n--------------------------")
