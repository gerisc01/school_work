#include "calculator.h"
#include "parser.h"
#include "ast.h"
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

Calculator::Calculator(ostream& outStream):
   memory(0),
   out(outStream)
{}

void Calculator::eval(string expr) {

   Parser* parser = new Parser(new istringstream(expr));
   
   AST* tree = parser->parse();
   out << "#This is a set up code for the program" << endl;
   out << "zero := 0" << endl;
   out << "one := 1" << endl;
   out << "memory := 0" << endl;
   out << "sp := 99" << endl;
   out << "prompt := \"Please enter an integer...\"" << endl;

   tree->evaluate();

   out << "s := \"The result is \"" << endl;
   out << "writeStr(s)" << endl;
   out << "writeInt(M[100])"<< endl;
   out << "halt" << endl;
   out << "equ zero M[0] equ one M[1]" << endl;
   out << "equ memory M[2] equ sp M[3]" << endl;
   out << "equ A M[4] equ B M[5]" << endl;
   out << "equ s M[10] equ prompt M[31] equ x M[30]" << endl;
   
   delete tree;
   
   delete parser;

}

ostream& Calculator::getOutputStream() {
   return out;
}
