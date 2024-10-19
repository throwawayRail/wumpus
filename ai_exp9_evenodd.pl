% Base cases
is_even(0).
is_odd(1).

% Recursive case for even numbers
is_even(N) :-
    N > 0,
    N1 is N - 2,
    is_even(N1).

% Recursive case for odd numbers
is_odd(N) :-
    N > 0,
    N1 is N - 2,
    is_odd(N1).
