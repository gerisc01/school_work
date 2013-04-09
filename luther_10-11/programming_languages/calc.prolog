expr --> op, expr, expr; s, expr; number; r.

expr(add(A,B)) --> [+], expr(A), expr(B).
expr(sub(A,B)) --> [-], expr(A), expr(B).
expr(mul(A,B)) --> [*], expr(A), expr(B).
expr(div(A,B)) --> [/], expr(A), expr(B).
expr(store(U)) --> [s], expr(U).
expr(recall) --> [r].
expr(num(N)) --> [num(N)].

preprocess([],[]).
preprocess([H|T],[num(H)|TL]) :- number(H), preprocess(T,TL),!.
preprocess([H|T],[H|TL]) :- preprocess(T,TL).

eval(add(A,B),Min,Mout,Val) :- Min1 is Min, eval(A,Min1,Mout1,Val1), Min2 is Mout1, eval(B,Min2,Mout2,Val2), Mout is Mout2, Val is Val1 + Val2.
eval(sub(A,B),Min,Mout,Val) :- Min1 is Min, eval(A,Min1,Mout1,Val1), Min2 is Mout1, eval(B,Min2,Mout2,Val2), Mout is Mout2, Val is Val1 - Val2.
eval(mul(A,B),Min,Mout,Val) :- Min1 is Min, eval(A,Min1,Mout1,Val1), Min2 is Mout1, eval(B,Min2,Mout2,Val2), Mout is Mout2, Val is Val1 * Val2.
eval(div(A,B),Min,Mout,Val) :- Min1 is Min, eval(A,Min1,Mout1,Val1), Min2 is Mout1, eval(B,Min2,Mout2,Val2), Mout is Mout2, Val is Val1 / Val2.

eval(num(N),Min,Mout,Val) :- Mout is Min, Val is N.
eval(store(U),Min,Mout,Val) :- Min1 is Min, eval(U,Min1,_,Val1), Mout is Val1, Val is Val1.
eval(recall,Min,Mout,Val) :- Val is Min, Mout is Min.

calc :- readln(L,_,_,_,lowercase), preprocess(L,PreL), print(PreL), nl, expr(Tree,PreL,[]), print(Tree), nl, eval(Tree,0,_,Val), print(Val), nl.
