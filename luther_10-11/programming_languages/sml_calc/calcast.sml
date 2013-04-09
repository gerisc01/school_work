structure calcAS = 
struct

datatype
    AST = add' of AST * AST
        | sub' of AST * AST
        | prod' of AST * AST
        | div' of AST * AST
        | negate' of AST
        | integer' of int
        | store' of AST
        | recall';
	   
end;


