result(gaurav, 9.2).
result(anooj, 8.2).
result(chinmay, 7.3).
result(piyush, 5.7).
result(parth, 8.9).
result(ankit, 6.3).
result(tanuja, 6.2).
result(pooja, 8.2).
result(asmita, 7.2).
getresult:-
    write("Whose result do you want to know"),nl,
    read(X),nl,
    result(X, Y),nl,
    write("this is the result"),nl,
    write(Y).
