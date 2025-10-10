:- dynamic(user_profile/5).
:- dynamic(question/2).

% Sample Database (Title, Director, Year, Genre, Type, Duration, Country, MainActor, Rating, Votes)
film('Zielona mila','Frank Darabont',1999,'drama', 'others', 188,'USA','Tom Hanks',8.7,719).
film('Pif Paf! Jestes trup', 'Guy Ferland', 2002, 'drama', 'others', 87, 'Kanada', 'Ben Foster', 7.7, 16).
film('Dogville', 'Lars von Trier', 2003, 'drama', 'others', 178, 'Dania', 'Nicole Kidman', 7.7, 45).
film('Z dystansu', 'Ton Kayne', 2011, 'drama', 'others', 100, 'USA', 'Adrien Brody', 7.9, 30).
film('Lista Schindlera', 'Steven Spielberg', 1993, 'drama', 'others', 195, 'USA', 'Adrien Brody', 8.4, 259).
film('Requiem dla snu', 'Darren Aronofsky', 2000, 'drama', 'others', 102, 'USA', 'Jared Leto', 7.9, 520).
film('Biutiful', 'Alejandro Gonzalez Inarritu', 2010, 'drama', 'others', 148, 'Hiszpania', 'Javier Bardem', 7.6, 12).
film('Czarny labedz', 'Darren Aronofsky', 2010, 'drama', 'others', 108, 'USA', 'Natalie Portman', 7.7, 248).
film('Gladiator', 'Ridley Scott', 2000, 'drama', 'others', 155, 'USA', 'Russell Crowe', 8.1, 552).
film('Dzien swira', 'Marek Koterski', 2002, 'drama', 'others', 123, 'Polska', 'Marek Kondrat', 7.8, 438).
film('Pianista', 'Roman Polanski', 2002, 'drama', 'others', 150, 'Polska', 'Adrien Brody', 8.3, 410).
film('Seksmisja', 'Juliusz Machulski', 1984, 'comedy', 'others', 118, 'Polska', 'Jerzy Stuhr', 7.9, 420).
film('Forrest Gump', 'Robert Zemeckis', 1994, 'comedy', 'others', 144, 'USA', 'Tom Hanks', 8.6, 697).
film('Kac Vegas', 'Todd Phillips', 2009, 'comedy', 'others', 100, 'USA', 'Bradley Cooper', 7.3, 537).
film('Notykalni', 'Olivier Nakache', 2011, 'comedy', 'others', 112, 'Francja', 'Francois Cluzet', 8.7, 393).
film('Truman Show', 'Peter Weir', 1998, 'comedy', 'others', 103, 'USA', 'Jim Carrey', 7.4, 383).
film('Kiler', 'Juliusz Machulski', 1997, 'comedy', 'others', 104, 'Polska', 'Cezary Pazura', 7.7, 315).
film('Kevin sam w domu', 'Chris Columbus', 1990, 'comedy', 'others', 103, 'USA', 'Macaulay Culkin', 7.1, 297).
film('Mis', 'Stanislaw Bareja', 1980, 'comedy', 'others', 111, 'Polska', 'Stanislaw Tym', 7.8, 261).
film('Diabel ubiera sie u Prady', 'David Frankel', 2006, 'comedy', 'others', 109, 'USA', 'Meryl Streep', 6.9, 227).
film('Jak rozpetalem druga wojne swiatowa', 'Tadeusz Chmielewski', 1969, 'comedy', 'others', 236, 'Polska', 'Marian Kociniak', 7.9, 195).

% Helper: Get actor's filmography
actor_films(Actor, FilmTitle) :- film(FilmTitle, _, _, _, _, _, _, Actor, _, _).

% Interaction: Get user profile
get_input(Prompt, Var) :- write(Prompt), read(Var).

ask_user(Name, Sex, Mood, Time, Genre) :-
    get_input('What is your name? ', Name),
    get_input('What is your sex (male/female)? ', Sex),
    get_input('How are you feeling (sad/happy)? ', Mood),
    get_input('How much time (in minutes) do you have? ', Time),
    get_input('What film genre are you interested in (drama/comedy)? ', Genre),
    asserta(user_profile(Name, Sex, Mood, Time, Genre)).

% Recommendation Rule
recommend(Title, Name) :-
    user_profile(Name, _, Mood, Time, Genre),
    % Mood logic (Minimal rule: sad mood for drama, happy for comedy)
    ( (Mood = sad, Genre = drama) ; (Mood = happy, Genre = comedy) ),
    % Time check
    Time_Limit is Time,
    film(Title, _, _, Genre, _, Duration, _, _, Rating, _),
    Duration =< Time_Limit,
    % Minimal rating filter
    Rating >= 7.5,
    write('Recommended film for '), write(Name), write(': '), write(Title), nl.

% Main Predicate
start :-
    retractall(user_profile(_, _, _, _, _)),
    ask_user(Name, _, _, _, _),
    write('Searching for recommendations...'), nl,
    recommend(Title, Name),
    fail. % Loop to show all recommendations

start :- write('No more recommendations found based on your criteria.').

% To run: load the file into a Prolog interpreter and type:
% ?- start.