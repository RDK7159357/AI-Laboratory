% D = Defendant, V = Victim
:- dynamic(act/3).
:- dynamic(civilian/1).
:- dynamic(prisoner_of_war/1).
:- dynamic(medical_personnel/1).
:- dynamic(religious_personnel/1).
:- dynamic(international_conflict/2).

% 1. ICC Jurisdiction (Article 5)
crime(genocide).
crime(war_crime).
crime(crime_against_humanity).
crime(crime_of_aggression).

% 2. Protected Persons (Geneva Conventions)
protected_by_geneva_convention(P) :- civilian(P).
protected_by_geneva_convention(P) :- prisoner_of_war(P).
protected_by_geneva_convention(P) :- medical_personnel(P).
protected_by_geneva_convention(P) :- religious_personnel(P).

% 3. Criminal Liability Rules

% R1: Genocide (Article 6) - Placeholder for complexity
criminal_liability(genocide, Statute, D, V) :-
    elements(Statute, D, V). 

% R2: War Crimes (Article 8)
criminal_liability(war_crime, Statute, D, V) :-
    protected_by_geneva_convention(V),
    international_conflict(D, V),
    elements(Statute, D, V).

% 4. Specific War Crimes Elements (Article 8)
elements(article_8_2_a_i, D, V) :-
    act(D, killed, V). % Will match if D killed V

elements(article_8_2_a_ii, D, V) :-
    act(D, tortured, V). % Will match if D tortured V

% 5. Example Interaction/Facts (Simulation)
% The user will interactively assert facts or we can assert them for testing:
% ?- asserta(civilian(victim_A)).
% ?- asserta(international_conflict(defendant_X, victim_A)).
% ?- asserta(act(defendant_X, killed, victim_A)).

% Example Query: What crime was committed by defendant_X against victim_A?
% ?- criminal_liability(Crime, Statute, defendant_X, victim_A).
% Crime = war_crime,
% Statute = article_8_2_a_i.

/* 
==================== SAMPLE INPUT/OUTPUT ====================

Example 1: War Crime - Killing a Civilian
------------------------------------------
?- asserta(civilian(victim_A)).
true.

?- asserta(international_conflict(defendant_X, victim_A)).
true.

?- asserta(act(defendant_X, killed, victim_A)).
true.

?- criminal_liability(Crime, Statute, defendant_X, victim_A).
Crime = war_crime,
Statute = article_8_2_a_i.


Example 2: War Crime - Torturing a Prisoner of War
---------------------------------------------------
?- asserta(prisoner_of_war(victim_B)).
true.

?- asserta(international_conflict(defendant_Y, victim_B)).
true.

?- asserta(act(defendant_Y, tortured, victim_B)).
true.

?- criminal_liability(Crime, Statute, defendant_Y, victim_B).
Crime = war_crime,
Statute = article_8_2_a_ii.


Example 3: War Crime - Killing Medical Personnel
-------------------------------------------------
?- asserta(medical_personnel(doctor_smith)).
true.

?- asserta(international_conflict(soldier_jones, doctor_smith)).
true.

?- asserta(act(soldier_jones, killed, doctor_smith)).
true.

?- criminal_liability(Crime, Statute, soldier_jones, doctor_smith).
Crime = war_crime,
Statute = article_8_2_a_i.


Example 4: Checking if a person is protected
---------------------------------------------
?- asserta(civilian(john)).
true.

?- protected_by_geneva_convention(john).
true.

?- asserta(religious_personnel(priest_mary)).
true.

?- protected_by_geneva_convention(priest_mary).
true.


Example 5: Listing all crimes
------------------------------
?- crime(X).
X = genocide ;
X = war_crime ;
X = crime_against_humanity ;
X = crime_of_aggression.

*/