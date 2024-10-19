result(frieren,9.2).
result(fern,8.2).
result(stark,7.3).
result(heiter,4.9).
result(qual,4.7).
result(flamme,9.3).
result(himmel,8.4).
result(eisen,2.3).
result(aura,5.5).
result(lawine,8.7).
result(sense,6,7).


getresult:-
    write("Whose result do you want to know?"),nl,
    read(X),nl,
    result(X,Y),nl,
    write("This is the result: "),
    write(Y).

