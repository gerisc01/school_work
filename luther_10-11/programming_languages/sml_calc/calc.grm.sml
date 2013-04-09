functor calcLrValsFun(structure Token : TOKEN)
 : sig structure ParserData : PARSER_DATA
       structure Tokens : calc_TOKENS
   end
 = 
struct
structure ParserData=
struct
structure Header = 
struct
(* calc.grm - parser spec *)

open calcAS;


end
structure LrTable = Token.LrTable
structure Token = Token
local open LrTable in 
val table=let val actionRows =
"\
\\001\000\001\000\000\000\000\000\
\\001\000\001\000\025\000\004\000\016\000\005\000\015\000\000\000\
\\001\000\001\000\026\000\003\000\026\000\004\000\026\000\005\000\026\000\
\\006\000\014\000\007\000\013\000\000\000\
\\001\000\001\000\027\000\003\000\027\000\004\000\027\000\005\000\027\000\
\\006\000\014\000\007\000\013\000\000\000\
\\001\000\001\000\028\000\003\000\028\000\004\000\028\000\005\000\028\000\
\\006\000\014\000\007\000\013\000\000\000\
\\001\000\001\000\029\000\003\000\029\000\004\000\029\000\005\000\029\000\
\\006\000\029\000\007\000\029\000\000\000\
\\001\000\001\000\030\000\003\000\030\000\004\000\030\000\005\000\030\000\
\\006\000\030\000\007\000\030\000\000\000\
\\001\000\001\000\031\000\003\000\031\000\004\000\031\000\005\000\031\000\
\\006\000\031\000\007\000\031\000\000\000\
\\001\000\001\000\032\000\003\000\032\000\004\000\032\000\005\000\032\000\
\\006\000\032\000\007\000\032\000\000\000\
\\001\000\001\000\033\000\003\000\033\000\004\000\033\000\005\000\033\000\
\\006\000\033\000\007\000\033\000\008\000\012\000\000\000\
\\001\000\001\000\034\000\003\000\034\000\004\000\034\000\005\000\034\000\
\\006\000\034\000\007\000\034\000\008\000\034\000\000\000\
\\001\000\001\000\035\000\003\000\035\000\004\000\035\000\005\000\035\000\
\\006\000\035\000\007\000\035\000\008\000\035\000\000\000\
\\001\000\001\000\036\000\003\000\036\000\004\000\036\000\005\000\036\000\
\\006\000\036\000\007\000\036\000\008\000\036\000\000\000\
\\001\000\001\000\037\000\003\000\037\000\004\000\037\000\005\000\037\000\
\\006\000\037\000\007\000\037\000\008\000\037\000\000\000\
\\001\000\001\000\038\000\003\000\038\000\004\000\038\000\005\000\038\000\
\\006\000\038\000\007\000\038\000\008\000\038\000\000\000\
\\001\000\002\000\011\000\005\000\010\000\009\000\009\000\010\000\008\000\000\000\
\\001\000\003\000\023\000\004\000\016\000\005\000\015\000\000\000\
\"
val actionRowNumbers =
"\015\000\011\000\009\000\007\000\
\\004\000\001\000\012\000\014\000\
\\015\000\015\000\008\000\015\000\
\\015\000\015\000\015\000\010\000\
\\016\000\006\000\005\000\003\000\
\\002\000\013\000\000\000"
val gotoT =
"\
\\001\000\022\000\002\000\005\000\003\000\004\000\004\000\003\000\
\\005\000\002\000\006\000\001\000\000\000\
\\000\000\
\\000\000\
\\000\000\
\\000\000\
\\000\000\
\\000\000\
\\000\000\
\\005\000\015\000\006\000\001\000\000\000\
\\002\000\016\000\003\000\004\000\004\000\003\000\005\000\002\000\
\\006\000\001\000\000\000\
\\000\000\
\\004\000\017\000\005\000\002\000\006\000\001\000\000\000\
\\004\000\018\000\005\000\002\000\006\000\001\000\000\000\
\\003\000\019\000\004\000\003\000\005\000\002\000\006\000\001\000\000\000\
\\003\000\020\000\004\000\003\000\005\000\002\000\006\000\001\000\000\000\
\\000\000\
\\000\000\
\\000\000\
\\000\000\
\\000\000\
\\000\000\
\\000\000\
\\000\000\
\"
val numstates = 23
val numrules = 14
val s = ref "" and index = ref 0
val string_to_int = fn () => 
let val i = !index
in index := i+2; Char.ord(String.sub(!s,i)) + Char.ord(String.sub(!s,i+1)) * 256
end
val string_to_list = fn s' =>
    let val len = String.size s'
        fun f () =
           if !index < len then string_to_int() :: f()
           else nil
   in index := 0; s := s'; f ()
   end
val string_to_pairlist = fn (conv_key,conv_entry) =>
     let fun f () =
         case string_to_int()
         of 0 => EMPTY
          | n => PAIR(conv_key (n-1),conv_entry (string_to_int()),f())
     in f
     end
val string_to_pairlist_default = fn (conv_key,conv_entry) =>
    let val conv_row = string_to_pairlist(conv_key,conv_entry)
    in fn () =>
       let val default = conv_entry(string_to_int())
           val row = conv_row()
       in (row,default)
       end
   end
val string_to_table = fn (convert_row,s') =>
    let val len = String.size s'
        fun f ()=
           if !index < len then convert_row() :: f()
           else nil
     in (s := s'; index := 0; f ())
     end
local
  val memo = Array.array(numstates+numrules,ERROR)
  val _ =let fun g i=(Array.update(memo,i,REDUCE(i-numstates)); g(i+1))
       fun f i =
            if i=numstates then g i
            else (Array.update(memo,i,SHIFT (STATE i)); f (i+1))
          in f 0 handle Subscript => ()
          end
in
val entry_to_action = fn 0 => ACCEPT | 1 => ERROR | j => Array.sub(memo,(j-2))
end
val gotoT=Array.fromList(string_to_table(string_to_pairlist(NT,STATE),gotoT))
val actionRows=string_to_table(string_to_pairlist_default(T,entry_to_action),actionRows)
val actionRowNumbers = string_to_list actionRowNumbers
val actionT = let val actionRowLookUp=
let val a=Array.fromList(actionRows) in fn i=>Array.sub(a,i) end
in Array.fromList(map actionRowLookUp actionRowNumbers)
end
in LrTable.mkLrTable {actions=actionT,gotos=gotoT,numRules=numrules,
numStates=numstates,initialState=STATE 0}
end
end
local open Header in
type pos = int
type arg = unit
structure MlyValue = 
struct
datatype svalue = VOID | ntVOID of unit | Int of  (int)
 | Factor of  (AST) | NegFactor of  (AST) | StoreIt of  (AST)
 | Term of  (AST) | Expr of  (AST) | Prog of  (AST)
end
type svalue = MlyValue.svalue
type result = AST
end
structure EC=
struct
open LrTable
infix 5 $$
fun x $$ y = y::x
val is_keyword =
fn _ => false
val preferred_change : (term list * term list) list = 
nil
val noShift = 
fn _ => false
val showTerminal =
fn (T 0) => "EOF"
  | (T 1) => "LParen"
  | (T 2) => "RParen"
  | (T 3) => "Plus"
  | (T 4) => "Minus"
  | (T 5) => "Times"
  | (T 6) => "Div"
  | (T 7) => "Store"
  | (T 8) => "Recall"
  | (T 9) => "Int"
  | _ => "bogus-term"
local open Header in
val errtermvalue=
fn _ => MlyValue.VOID
end
val terms : term list = nil
 $$ (T 8) $$ (T 7) $$ (T 6) $$ (T 5) $$ (T 4) $$ (T 3) $$ (T 2) $$ (T 
1) $$ (T 0)end
structure Actions =
struct 
exception mlyAction of int
local open Header in
val actions = 
fn (i392,defaultPos,stack,
    (()):arg) =>
case (i392,stack)
of  ( 0, ( ( _, ( MlyValue.Expr Expr, Expr1left, Expr1right)) :: 
rest671)) => let val  result = MlyValue.Prog (Expr)
 in ( LrTable.NT 0, ( result, Expr1left, Expr1right), rest671)
end
|  ( 1, ( ( _, ( MlyValue.Term Term, _, Term1right)) :: _ :: ( _, ( 
MlyValue.Expr Expr, Expr1left, _)) :: rest671)) => let val  result = 
MlyValue.Expr (add'(Expr,Term))
 in ( LrTable.NT 1, ( result, Expr1left, Term1right), rest671)
end
|  ( 2, ( ( _, ( MlyValue.Term Term, _, Term1right)) :: _ :: ( _, ( 
MlyValue.Expr Expr, Expr1left, _)) :: rest671)) => let val  result = 
MlyValue.Expr (sub'(Expr,Term))
 in ( LrTable.NT 1, ( result, Expr1left, Term1right), rest671)
end
|  ( 3, ( ( _, ( MlyValue.Term Term, Term1left, Term1right)) :: 
rest671)) => let val  result = MlyValue.Expr (Term)
 in ( LrTable.NT 1, ( result, Term1left, Term1right), rest671)
end
|  ( 4, ( ( _, ( MlyValue.StoreIt StoreIt, _, StoreIt1right)) :: _ :: 
( _, ( MlyValue.Term Term, Term1left, _)) :: rest671)) => let val  
result = MlyValue.Term (prod'(Term,StoreIt))
 in ( LrTable.NT 2, ( result, Term1left, StoreIt1right), rest671)
end
|  ( 5, ( ( _, ( MlyValue.StoreIt StoreIt, _, StoreIt1right)) :: _ :: 
( _, ( MlyValue.Term Term, Term1left, _)) :: rest671)) => let val  
result = MlyValue.Term (div'(Term,StoreIt))
 in ( LrTable.NT 2, ( result, Term1left, StoreIt1right), rest671)
end
|  ( 6, ( ( _, ( MlyValue.StoreIt StoreIt, StoreIt1left, StoreIt1right
)) :: rest671)) => let val  result = MlyValue.Term (StoreIt)
 in ( LrTable.NT 2, ( result, StoreIt1left, StoreIt1right), rest671)

end
|  ( 7, ( ( _, ( _, _, Store1right)) :: ( _, ( MlyValue.NegFactor 
NegFactor, NegFactor1left, _)) :: rest671)) => let val  result = 
MlyValue.StoreIt (store'(NegFactor))
 in ( LrTable.NT 3, ( result, NegFactor1left, Store1right), rest671)

end
|  ( 8, ( ( _, ( MlyValue.NegFactor NegFactor, NegFactor1left, 
NegFactor1right)) :: rest671)) => let val  result = MlyValue.StoreIt (
NegFactor)
 in ( LrTable.NT 3, ( result, NegFactor1left, NegFactor1right), 
rest671)
end
|  ( 9, ( ( _, ( MlyValue.NegFactor NegFactor, _, NegFactor1right)) ::
 ( _, ( _, Minus1left, _)) :: rest671)) => let val  result = 
MlyValue.NegFactor (negate'(NegFactor))
 in ( LrTable.NT 4, ( result, Minus1left, NegFactor1right), rest671)

end
|  ( 10, ( ( _, ( MlyValue.Factor Factor, Factor1left, Factor1right))
 :: rest671)) => let val  result = MlyValue.NegFactor (Factor)
 in ( LrTable.NT 4, ( result, Factor1left, Factor1right), rest671)
end
|  ( 11, ( ( _, ( MlyValue.Int Int, Int1left, Int1right)) :: rest671))
 => let val  result = MlyValue.Factor (integer'(Int))
 in ( LrTable.NT 5, ( result, Int1left, Int1right), rest671)
end
|  ( 12, ( ( _, ( _, _, RParen1right)) :: ( _, ( MlyValue.Expr Expr, _
, _)) :: ( _, ( _, LParen1left, _)) :: rest671)) => let val  result = 
MlyValue.Factor (Expr)
 in ( LrTable.NT 5, ( result, LParen1left, RParen1right), rest671)
end
|  ( 13, ( ( _, ( _, Recall1left, Recall1right)) :: rest671)) => let
 val  result = MlyValue.Factor (recall')
 in ( LrTable.NT 5, ( result, Recall1left, Recall1right), rest671)
end
| _ => raise (mlyAction i392)
end
val void = MlyValue.VOID
val extract = fn a => (fn MlyValue.Prog x => x
| _ => let exception ParseInternal
	in raise ParseInternal end) a 
end
end
structure Tokens : calc_TOKENS =
struct
type svalue = ParserData.svalue
type ('a,'b) token = ('a,'b) Token.token
fun EOF (p1,p2) = Token.TOKEN (ParserData.LrTable.T 0,(
ParserData.MlyValue.VOID,p1,p2))
fun LParen (p1,p2) = Token.TOKEN (ParserData.LrTable.T 1,(
ParserData.MlyValue.VOID,p1,p2))
fun RParen (p1,p2) = Token.TOKEN (ParserData.LrTable.T 2,(
ParserData.MlyValue.VOID,p1,p2))
fun Plus (p1,p2) = Token.TOKEN (ParserData.LrTable.T 3,(
ParserData.MlyValue.VOID,p1,p2))
fun Minus (p1,p2) = Token.TOKEN (ParserData.LrTable.T 4,(
ParserData.MlyValue.VOID,p1,p2))
fun Times (p1,p2) = Token.TOKEN (ParserData.LrTable.T 5,(
ParserData.MlyValue.VOID,p1,p2))
fun Div (p1,p2) = Token.TOKEN (ParserData.LrTable.T 6,(
ParserData.MlyValue.VOID,p1,p2))
fun Store (p1,p2) = Token.TOKEN (ParserData.LrTable.T 7,(
ParserData.MlyValue.VOID,p1,p2))
fun Recall (p1,p2) = Token.TOKEN (ParserData.LrTable.T 8,(
ParserData.MlyValue.VOID,p1,p2))
fun Int (i,p1,p2) = Token.TOKEN (ParserData.LrTable.T 9,(
ParserData.MlyValue.Int i,p1,p2))
end
end
