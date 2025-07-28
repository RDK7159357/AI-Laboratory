import json
from kanren import Relation, facts, run, conde, var, eq
from kanren.core import lall
# /Users/ramadugudhanush/Documents/AI Laboratory/.venv/bin/python" 1.py
# --- Define Relationships ---

# A person 'p' is a parent of 'c' if they are the father or mother.
def parent(p, c):
    return conde([father(p, c)], [mother(p, c)])

# A person 'gp' is a grandparent of 'gc' if they are the parent of 'gc's parent.
def grandparent(gp, gc):
    p = var() # A variable for the parent in the middle
    return conde((parent(gp, p), parent(p, gc)))

# Two people 'x' and 'y' are siblings if they share a parent.
# We'll handle the inequality check in the main query logic
def sibling(x, y):
    p = var()
    # Just check if they share a parent - we'll filter out self-matches later
    return lall(parent(p, x), parent(p, y))

# A person 'u' is an uncle of 'n' if 'u' is the brother of 'n's parent.
def uncle(u, n):
    p = var() # Variable for the parent
    # 'u' is an uncle of 'n' if:
    # 1. 'p' is a parent of 'n'
    # 2. 'u' is a sibling of 'p'
    # 3. 'u' is male (we check this by seeing if 'u' is a father to anyone)
    return conde((parent(p, n), sibling(u, p), father(u, var())))

# Custom non-equality relation for use in lall
# def neq(x, y):
#     def goal(s):
#         if x == y:
#             return iter([])  # No solutions if x and y are equal
#         else:
#             return iter([s])  # One solution if x and y are different
#     return goal

# --- Main Execution ---

if __name__ == '__main__':
    # Initialize the relations we will use
    father = Relation()
    mother = Relation()

    # Load the data from the JSON file
    try:
        with open('relationships.json') as f:
            d = json.load(f)
    except FileNotFoundError:
        print("Error: 'relationships.json' not found. Please create it.")
        exit()

    # Add the loaded data to our knowledge base (facts)
    for item in d['father']:
        facts(father, (item[0], item[1]))

    for item in d['mother']:
        facts(mother, (item[0], item[1]))

    # Define a variable 'x' to use in our queries
    x = var()

    print("--- Family Tree Queries ---")

    # 1. Who are John's children?
    name = 'John'
    output = run(0, x, father(name, x))
    print(f"\n{name}'s children are: {', '.join(output)}")

    # 2. Who is William's mother?
    name = 'William'
    output = run(0, x, mother(x, name))
    print(f"\n{name}'s mother is: {output[0]}")

    # 3. Who are Adam's parents?
    name = 'Adam'
    output = run(0, x, parent(x, name))
    print(f"\n{name}'s parents are: {', '.join(output)}")

    # 4. Who are Wayne's grandparents?
    name = 'Wayne'
    output = run(0, x, grandparent(x, name))
    print(f"\n{name}'s grandparents are: {', '.join(output)}")

    # 5. Who are Megan's grandchildren?
    name = 'Megan'
    output = run(0, x, grandparent(name, x))
    print(f"\n{name}'s grandchildren are: {', '.join(output)}")

    # 6. Who are David's siblings?
    name = 'David'
    output = run(0, x, sibling(x, name))
    # Filter out the person themselves from siblings and remove duplicates
    siblings = list(set([person for person in output if person != name]))
    print(f"\n{name}'s siblings are: {', '.join(siblings)}")
    
    # 7. Who are Tiffany's uncles?
    name = 'Tiffany'
    output = run(0, x, uncle(x, name))
    # Remove duplicates
    uncles = list(set(output))
    print(f"\n{name}'s uncles are: {', '.join(uncles)}")

    # 8. List all the spouses in the family
    # We find spouses by identifying a father and mother of the same child.
    y = var()
    c = var()
    # run(0, (x,y), ...) gives us pairs of results
    output = run(0, (x, y), father(x, c), mother(y, c))
    # Using a set to store unique pairs (couples)
    couples = set(output)
    print("\nList of all couples (spouses):")
    for couple in couples:
        print(f"  - {couple[0]} and {couple[1]}")

    print("\n---------------------------")
