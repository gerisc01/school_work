signature calc_TOKENS =
sig
type ('a,'b) token
type svalue
val Int: (int) *  'a * 'a -> (svalue,'a) token
val Recall:  'a * 'a -> (svalue,'a) token
val Store:  'a * 'a -> (svalue,'a) token
val Div:  'a * 'a -> (svalue,'a) token
val Times:  'a * 'a -> (svalue,'a) token
val Minus:  'a * 'a -> (svalue,'a) token
val Plus:  'a * 'a -> (svalue,'a) token
val RParen:  'a * 'a -> (svalue,'a) token
val LParen:  'a * 'a -> (svalue,'a) token
val EOF:  'a * 'a -> (svalue,'a) token
end
signature calc_LRVALS=
sig
structure Tokens : calc_TOKENS
structure ParserData:PARSER_DATA
sharing type ParserData.Token.token = Tokens.token
sharing type ParserData.svalue = Tokens.svalue
end
