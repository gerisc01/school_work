#include "ast.h"
#include <iostream>
#include "calculator.h"

// for debug information uncomment
//#define debug

AST::AST() {}

AST::~AST() {}

BinaryNode::BinaryNode(AST* left, AST* right):
   AST(),
   leftTree(left),
   rightTree(right)
{}

BinaryNode::~BinaryNode() {
#ifdef debug
   cout << "In BinaryNode destructor" << endl;
#endif

   try {
      delete leftTree;
   } catch (...) {}

   try {
      delete rightTree;
   } catch(...) {}
}
   
AST* BinaryNode::getLeftSubTree() const {
   return leftTree;
}

AST* BinaryNode::getRightSubTree() const {
   return rightTree;
}

UnaryNode::UnaryNode(AST* sub):
   AST(),
   subTree(sub)
{}

UnaryNode::~UnaryNode() {
#ifdef debug
   cout << "In UnaryNode destructor" << endl;
#endif

   try {
      delete subTree;
   } catch (...) {}
}
   
AST* UnaryNode::getSubTree() const {
   return subTree;
}

AddNode::AddNode(AST* left, AST* right):
   BinaryNode(left,right)
{}

void AddNode::evaluate() {
   ostream& out = calc->getOutputStream();
   getLeftSubTree()->evaluate();
   getRightSubTree()->evaluate();
   out << "A := M[sp+0]" << endl;
   out << "sp := sp - one" << endl;
   out << "B := M[sp+0]" << endl;
   out << "A := A+B" << endl;
   out << "M[sp+0] := A" <<endl;
   //return getLeftSubTree()->evaluate() + getRightSubTree()->evaluate();
}

SubNode::SubNode(AST* left, AST* right):
   BinaryNode(left,right)
{}

void SubNode::evaluate() {
   ostream& out = calc->getOutputStream();
   getLeftSubTree()->evaluate();
   getRightSubTree()->evaluate();
   out << "A := M[sp+0]" << endl;
   out << "sp := sp - one" << endl;
   out << "B := M[sp+0]" << endl;
   out << "A := B-A" << endl;
   out << "M[sp+0] := A" << endl;
}

MultNode::MultNode(AST* left, AST* right):
   BinaryNode(left,right)
{}

void MultNode::evaluate() {
   ostream& out = calc->getOutputStream();
   getLeftSubTree()->evaluate();
   getRightSubTree()->evaluate();
   out << "A := M[sp+0]" << endl;
   out << "sp := sp - one" << endl;
   out << "B := M[sp+0]" << endl;
   out << "A := A*B" << endl;
   out << "M[sp+0] := A" << endl;
}

DivNode::DivNode(AST* left, AST* right):
   BinaryNode(left,right)
{}

void DivNode::evaluate() {
   ostream& out = calc->getOutputStream();
   getLeftSubTree()->evaluate();
   getRightSubTree()->evaluate();
   out << "A := M[sp+0]" << endl;
   out << "sp := sp - one" << endl;
   out << "B := M[sp+0]" << endl;
   out << "A := B/A" << endl;
   out << "M[sp+0] := A" << endl;
}

StoreNode::StoreNode(AST* sub):
   UnaryNode(sub)
{}

void StoreNode::evaluate() {
   ostream& out = calc->getOutputStream();
   getSubTree()->evaluate();
   out << "memory := M[sp+0]" << endl;
}

RecallNode::RecallNode():
   AST()
{}

void RecallNode::evaluate() {
   ostream& out = calc->getOutputStream();
   out << "sp := sp + one" << endl;
   out << "M[sp+0] := memory" << endl;
}

InputNode::InputNode():
   AST()
{}

void InputNode::evaluate() {
   ostream& out = calc->getOutputStream();
   out << "writeStr(prompt)" << endl;
   out << "readInt(x)" << endl;
   out << "A := x" << endl;
   out << "sp := sp + one" << endl;
   out << "M[sp+0] := A" << endl;
}

NumNode::NumNode(int n) :
   AST(),
   val(n)
{}

void NumNode::evaluate() {
   ostream& out = calc->getOutputStream();
   out << "A :=" << val << endl;
   out << "sp := sp + one" << endl;
   out << "M[sp+0] := A" << endl;
}
