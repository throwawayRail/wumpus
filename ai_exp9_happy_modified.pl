friend(jin, james).
friend(jin,john).
friend(john,james).
likes(john, jin).
likes(james, john).
happy(X):-friend(X,Y),likes(Y,X).
