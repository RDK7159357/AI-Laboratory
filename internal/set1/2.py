from pyswip import Prolog
# b. Alpha Beta Pruning
prolog = Prolog()
prolog.consult('week4/game.pl')

result = list(prolog.query('alphabeta(root, -1000, 1000, BestMove, BestValue).'))

if result:
    print(f"Best move: {result[0]['BestMove']}, Value: {result[0]['BestValue']}")
else:
    print("No solution found.")
