#ifndef calculator_h
#define calculator_h

#include <string>
#include <fstream>
 
using namespace std;


class Calculator {
 public:
   Calculator(ostream& outStream);

   void eval(string expr);

   ostream& getOutputStream();

 private:
   int memory;
   ostream& out;
};

extern Calculator* calc;

#endif

