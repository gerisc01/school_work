lookup(X,btnode(X,_,_)).
lookup(X,btnode(Val,Left,_)) :- X < Val, lookup(X,Left).
lookup(X,btnode(Val,_,Right)) :- X > Val, lookup(X,Right).

processlist([],T,T).
processlist([H|T],Tree,NewTree) :- insert(H,Tree,HTree), processlist(T,HTree,NewTree).

insert(Val,nil,btnode(Val,nil,nil)).
insert(X,btnode(Val,Left,Right),btnode(Val,NewLeft,Right)) :- X < Val, insert(X,Left,NewLeft).
insert(X,btnode(Val,Left,Right),btnode(Val,Left,NewRight)) :- X > Val, insert(X,Right,NewRight).

buildtree(T) :- readln(L,_,_,_,lowercase), processlist(L,nil,T).
