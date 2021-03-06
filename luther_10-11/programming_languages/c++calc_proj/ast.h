#ifndef ast_h
#define ast_h

using namespace std;

class AST {
 public:
   AST();
   virtual ~AST() = 0;
   virtual void evaluate() = 0;
};

class BinaryNode : public AST {
 public:
   BinaryNode(AST* left, AST* right);
   ~BinaryNode();

   AST* getLeftSubTree() const;
   AST* getRightSubTree() const;

 private:
   AST* leftTree;
   AST* rightTree;
};

class UnaryNode : public AST {
 public:
   UnaryNode(AST* sub);
   ~UnaryNode();

   AST* getSubTree() const;

 private:
   AST* subTree;
};

class StoreNode : public UnaryNode {
 public:
   StoreNode(AST* sub);

   void evaluate();
};

class RecallNode : public AST {
 public:
   RecallNode();
   void evaluate();
};

class InputNode : public AST {
 public:
    InputNode();
    void evaluate();
};

class AddNode : public BinaryNode {
 public:
   AddNode(AST* left, AST* right);
   
   void evaluate();
};

class SubNode : public BinaryNode {
 public:
   SubNode(AST* left, AST* right);

   void evaluate();
};

class MultNode : public BinaryNode {
 public:
   MultNode(AST* left, AST* right);

   void evaluate();
};

class DivNode : public BinaryNode {
 public:
   DivNode(AST* left, AST* right);

   void evaluate();
};

class NumNode : public AST {
 public:
   NumNode(int n);

   void evaluate();

 private:
   int val;
};




#endif

