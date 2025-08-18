% alphabeta(Position, Alpha, Beta, BestMove, BestValue)
% This is the main predicate. It takes the current position,
% initial alpha and beta bounds, and returns the best move and its calculated value.
alphabeta(Pos, Alpha, Beta, BestMove, BestValue) :-
    % Case 1: Terminal position (no more moves).
    % The value is the static evaluation of the position.
    \+ moves(Pos, _), !,
    staticval(Pos, BestValue),
    BestMove = Pos.

% Case 2: Non-terminal position.
alphabeta(Pos, Alpha, Beta, BestMove, BestValue) :-
    % Get the list of possible moves from the current position.
    moves(Pos, [FirstMove | OtherMoves]),
    % Recursively evaluate the first move.
    alphabeta(FirstMove, Alpha, Beta, _, FirstVal),
    % Start the main loop to find the best move among the rest.
    % The first move's value and the initial bounds are passed to the helper predicate.
    best_value(OtherMoves, Alpha, Beta, FirstMove, FirstVal, BestMove, BestValue).

% best_value(RemainingMoves, Alpha, Beta, CurrentBestMove, CurrentBestVal, FinalBestMove, FinalBestVal)
% This predicate iterates through the remaining moves, pruning when possible.
% Base Case: No more moves to consider. The current best move is the final answer.
best_value([], _, _, BestMove, BestValue, BestMove, BestValue) :- !.

% Recursive Case: Check the current move for pruning.
best_value([NextMove | RestMoves], Alpha, Beta, CurrentBestMove, CurrentBestVal, FinalBestMove, FinalBestVal) :-
    % Check if the current move's value allows for pruning.
    prune_check(NextMove, Alpha, Beta, CurrentBestMove, CurrentBestVal, BestMoveForNextLevel, BestValForNextLevel),
    !,
    % If a cutoff occurred, the search is finished for this branch.
    best_value(RestMoves, Alpha, Beta, BestMoveForNextLevel, BestValForNextLevel, FinalBestMove, FinalBestVal).

% prune_check(NextMove, Alpha, Beta, CurrentBestMove, CurrentBestVal, BestMoveForNextLevel, BestValForNextLevel)
% This predicate handles the actual pruning logic.
% Pruning Condition (Alpha-Cutoff):
% If it's the maximizer's turn (min_to_move(CurrentBestMove)) and the current best value
% is already better than or equal to the minimizer's best guaranteed value (Beta).
prune_check(_, Alpha, Beta, CurrentBestMove, CurrentBestVal, CurrentBestMove, CurrentBestVal) :-
    min_to_move(CurrentBestMove),
    CurrentBestVal >= Beta.

% Pruning Condition (Beta-Cutoff):
% If it's the minimizer's turn (max_to_move(CurrentBestMove)) and the current best value
% is worse than or equal to the maximizer's best guaranteed value (Alpha).
prune_check(_, Alpha, Beta, CurrentBestMove, CurrentBestVal, CurrentBestMove, CurrentBestVal) :-
    max_to_move(CurrentBestMove),
    CurrentBestVal =< Alpha.

% No Pruning: Recurse to the next level of the tree.
prune_check(NextMove, Alpha, Beta, CurrentBestMove, CurrentBestVal, BetterMove, BetterVal) :-
    % Refine the bounds before the next recursive call.
    (min_to_move(CurrentBestMove) -> NewAlpha is max(Alpha, CurrentBestVal); NewAlpha = Alpha),
    (max_to_move(CurrentBestMove) -> NewBeta is min(Beta, CurrentBestVal); NewBeta = Beta),
    
    % Recursively call alphabeta for the next move with the new bounds.
    alphabeta(NextMove, NewAlpha, NewBeta, _, NextVal),
    % Compare the value from this move with the current best value.
    better_of(CurrentBestMove, CurrentBestVal, NextMove, NextVal, BetterMove, BetterVal).

% better_of(Move1, Val1, Move2, Val2, BestMove, BestVal)
% Compares two moves and returns the better one based on whose turn it is.
better_of(Move1, Val1, _, Val2, Move1, Val1) :-
    min_to_move(Move1),
    Val1 > Val2.
better_of(Move1, Val1, _, Val2, Move1, Val1) :-
    max_to_move(Move1),
    Val1 < Val2.
better_of(_, _, Move2, Val2, Move2, Val2).

% --- Example Game Tree (for demonstration) ---
% Define the game tree structure with moves (parent -> children)
moves(root, [b1, b2]).
moves(b1, [n1, n2, n3]).
moves(b2, [n4, n5, n6]).

% Define the static values for the leaf nodes
staticval(n1, 3).
staticval(n2, 5).
staticval(n3, 2).
staticval(n4, 9).
staticval(n5, 1).
staticval(n6, 7).

% Define the player turns for each position.
max_to_move(root).
min_to_move(b1).
min_to_move(b2).

% --- To run the code in a Prolog interpreter, use the following query: ---
% ?- alphabeta(root, -1000, 1000, BestMove, BestValue).
% This should return:
% BestMove = b1,
% BestValue = 3.

from pyswip import Prolog

prolog = Prolog()
prolog.consult('game.pl')  # Load your Prolog knowledge base

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