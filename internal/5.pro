illogical(X) :- baby(X).
not_intelligent(X) :- dog(X).
tree(X) :- graph(X), connected(X), circuit_free(X).
has_square_root(X) :- my_number(X), not(negative(X)).
negative(X) :- my_number(X), not(has_square_root(X)).
car(fiat). car(tesla).
has_carburetor(fiat).
person(alice). person(bob).
religious(alice).
my_number(imaginary_i). my_number(3).
real(3).
baby(tim).
dog(fido).
graph(g1).
connected(g1).
circuit_free(g1).

% --- EXECUTION EXAMPLES (Input/Output using a Prolog Interpreter) ---
% Input: ?- tree(g1).
% Output: true. 
% (g1 is a tree because it is a graph, connected, and circuit_free.)
%
% Input: ?- illogical(tim).
% Output: true. 
% (tim is illogical because tim is a baby.)
%
% Input: ?- car(X).
% Output: X = fiat ;
%         X = tesla.
% (Prolog lists all entities that satisfy the predicate car(X).)
%
% Input: ?- not_intelligent(fido).
% Output: true. 
% (fido is not intelligent because fido is a dog.)
%
% Input: ?- has_carburetor(tesla).
% Output: false. 
% (This demonstrates Negation as Failure: Prolog cannot prove the fact.)
%
% Input: ?- person(alice), religious(alice).
% Output: true. 
% (Checks if Alice is both a person AND religious.)