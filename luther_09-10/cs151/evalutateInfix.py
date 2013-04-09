from stack import *

class Expression:
   def __init__(self,exprstr):
       self.infix = exprstr.split()
       
   def __str__(self):
       return " ".join(self.infix)
       
   def evaluate(self):
      operator = Stack()
      operand = Stack()

      prec = {}
      prec["*"] = 3
      prec["/"] = 3
      prec["+"] = 2
      prec["-"] = 2
      prec["("] = 1

      for op in self.infix:
         if op in "0123456789":
            operand.push(int(op))
         elif op == "(":
            operator.push(op)
         elif op == ")":
            topOperator = operator.pop()
            while topOperator != "(":
               op1 = operand.pop()
               op2 = operand.pop()
               result = doMath(topOperator, op2, op1)
               operand.push(result)
               topOperator = operator.pop()

         else:
            while (not operator.isEmpty()) and (prec[operator.peek()] >= prec[op]):
               topOperator = operator.pop()
               op1 = operand.pop()
               op2 = operand.pop()
               result = doMath(topOperator, op2, op1)
               operand.push(result)

            operator.push(op)

      while (not operator.isEmpty()):
         topOperator = operator.pop()
         op1 = operand.pop()
         op2 = operand.pop()
         result = doMath(topOperator, op2, op1)
         operand.push(result)

      return operand.pop()


def doMath(operator, num, num1):
   if operator == "*":
      return num * num1
   elif operator == "/":
      return num / num1
   elif operator == "+":
      return num + num1
   else:
      return num - num1

def main():
   
   infile = open("infix.dat","r")
   
   for aline in infile:
      expr = Expression(aline)
      
      print(expr,"=",expr.evaluate())



main()
