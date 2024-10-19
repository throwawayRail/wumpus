parent(john, mary).
parent(john, bob).
parent(jane, mary).
parent(jane, bob).
parent(bob, ann).
parent(bob, lisa).

male(john).
male(bob).
female(jane).
female(mary).

mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
