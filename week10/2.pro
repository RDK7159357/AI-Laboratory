% FACTS (Topology and Identity)
device(heater).
device(light1).
device(light2).
device(light3).
device(light4).

connected(light1, fuse1).
connected(light2, fuse1).
connected(heater, fuse1).
connected(light3, fuse2).
connected(light4, fuse2).

different(X, Y) :- not(X = Y).

% RULES
% R1: Device is broken
broken(Device) :-
    on(Device),
    device(Device),
    not(working(Device)),
    connected(Device, Fuse),
    intact(Fuse).

% R2: Fuse is intact/OK (If any connected device is working)
intact(Fuse) :-
    connected(Device, Fuse),
    working(Device).

% R3: Fuse has failed (If two different devices connected to it are on and not working)
% Assumes at most one device is broken per fuse.
failed(Fuse) :-
    connected(Device1, Fuse),
    on(Device1),
    not(working(Device1)),
    connected(Device2, Fuse),
    on(Device2),
    not(working(Device2)),
    different(Device1, Device2).

% R4: Helper predicate (Implied by R3's structure in the original hint)
samefuse(Device1, Device2) :-
    connected(Device1, Fuse),
    connected(Device2, Fuse),
    different(Device1, Device2).

% ASKABLES (How an interactive Prolog system would prompt for facts)
% To test this system, assert the run-time state of the devices:
% Example state: light1 is on but not working; light2 is on and working.
% :- assert(on(light1)).
% :- assert(not(working(light1))).
% :- assert(on(light2)).
% :- assert(working(light2)).

% Example Query after asserting state:
% ? intact(fuse1).  % Should be true because light2 is working.
% ? broken(light1). % Should be true (light1 is on, not working, and fuse1 is intact).