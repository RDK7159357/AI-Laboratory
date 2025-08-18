# game.pl (Your Prolog code)
from pyswip import Prolog

prolog = Prolog()
prolog.consult('week4/game.pl')  # Load your Prolog knowledge base

# Query the Prolog predicate
query = 'alphabeta(root, -1000, 1000, BestMove, BestValue).'
result = list(prolog.query(query))

# Process the result
if result:
    best_move = result[0]['BestMove']
    best_value = result[0]['BestValue']
    print(f"The best move is: {best_move}")
    print(f"The minimax value is: {best_value}")
else:
    print("No solution found.")