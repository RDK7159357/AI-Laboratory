from kanren import run, var, fact, conde, lall, membero, eq

# --- Puzzle Solver ---

if __name__ == '__main__':
    # 1. Declare the variable that will hold our people data.
    # It will be a list of 4 tuples, where each tuple is (Name, Pet, Color, Country).
    people = var()

    # 2. Define the rules of the puzzle using lall (logical all).
    # All these conditions must be true for the solution to be valid.
    rules = lall(
        # There are exactly four people.
        eq(people, (var(), var(), var(), var())),

        # Rule 1: Steve has a blue car.
        membero(('Steve', var(), 'blue', var()), people),

        # Rule 2: The person who owns the cat lives in Canada.
        membero((var(), 'cat', var(), 'Canada'), people),

        # Rule 3: Matthew lives in the USA.
        membero(('Matthew', var(), var(), 'USA'), people),

        # Rule 4: The person with the black car lives in Australia.
        membero((var(), var(), 'black', 'Australia'), people),

        # Rule 5: Jack has a cat.
        membero(('Jack', 'cat', var(), var()), people),

        # Rule 6: Alfred lives in Australia.
        membero(('Alfred', var(), var(), 'Australia'), people),

        # Rule 7: The person who has a dog lives in France.
        membero((var(), 'dog', var(), 'France'), people),
        
        # The question: Who has a rabbit? This ensures someone has a rabbit.
        membero((var(), 'rabbit', var(), var()), people)
    )

    # 3. Run the solver.
    # We ask for the first solution (run(1, ...)) that satisfies all the rules.
    solutions = run(1, people, rules)

    # 4. Extract and print the output.
    if solutions:
        solution = solutions[0]
        
        # Find the person with the rabbit from the solution
        rabbit_owner = [p for p in solution if p[1] == 'rabbit'][0][0]
        
        print("--- Puzzle Solved! ---")
        print(f"\nThe person who has the rabbit is: {rabbit_owner}\n")
        
        # Print the full details for clarity
        print("Full details:")
        print("---------------------------------------")
        print("| {:<10} | {:<8} | {:<8} | {:<10} |".format("Name", "Pet", "Color", "Country"))
        print("---------------------------------------")
        for person in solution:
            # Convert any variables to string representation
            name = str(person[0]) if person[0] is not None else "Unknown"
            pet = str(person[1]) if person[1] is not None else "Unknown"
            color = str(person[2]) if person[2] is not None else "Unknown"
            country = str(person[3]) if person[3] is not None else "Unknown"
            print("| {:<10} | {:<8} | {:<8} | {:<10} |".format(name, pet, color, country))
        print("---------------------------------------")

    else:
        print("No solution found for the puzzle.")

