friend(jin, james).
friend(jin,john).
likes(john, jin).
likes(james, john).
happy(X):-friend(X,Y),likes(Y,X).
