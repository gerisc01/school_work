#include "parser.h"
#include "calcex.h"
#include <string>
#include <sstream>

Parser::Parser(istream* in) {
   scan = new Scanner(in);
}

Parser::~Parser() {
   try {
      delete scan;
   } catch (...) {}
}

AST* Parser::parse() {
   return Prog();
}

AST* Parser::Prog() {
   AST* result = Expr();
   Token* t = scan->getToken();

   if (t->getType() != eof) {
      cout << "Syntax Error: Expected EOF, found token at column " << t->getCol() << endl;
      throw ParseError;
   }

   return result;
}

AST* Parser::Expr() {
   return RestExpr(Term());
}

AST* Parser::RestExpr(AST* e) {
   Token* t = scan->getToken();

   if (t->getType() == add) {
      return RestExpr(new AddNode(e,Term()));
   }

   if (t->getType() == sub)
      return RestExpr(new SubNode(e,Term()));

   scan->putBackToken();

   return e;
}

AST* Parser::Term() {
   return RestTerm(Storable());
}

AST* Parser::RestTerm(AST* e) {
   Token* t = scan->getToken();

   if (t->getType() == times)
      return RestExpr(new MultNode(e,Storable()));

   if (t->getType() == divide)
      return RestExpr(new DivNode(e,Storable()));

   scan->putBackToken();

   return e;
}

AST* Parser::Storable() {
   AST* fact = Factor();
   Token* t = scan->getToken();

   if (t->getType() == keyword) {
      if (t->getLex() == "S") {
         return new StoreNode(fact);} 
      else {return fact;} 
      }  
   else {
      scan->putBackToken(); 
      return fact; 
      }
}

AST* Parser::Factor() {
   Token* t = scan->getToken();

   if (t->getType() == number) {
      istringstream in(t->getLex());
      int val;
      in >> val;
      return new NumNode(val);
   }

   if (t->getType() == keyword) {
      if (t->getLex() == "R") {
         return new RecallNode();}
      if (t->getLex() == "I") {
         return new InputNode();;} }

   if (t->getType() == lparen) {
      AST* e = Expr();
      Token* t = scan->getToken();
      
      if (t->getType() == rparen) {
         return e; } 
      else { scan->putBackToken(); }
   }
}
   
