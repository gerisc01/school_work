from binarytree import *

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def main():
    mytree = BinaryTree("+")
    mytree.insertLeft("*")
    mytree.getLeftChild().insertLeft("+")
    mytree.getLeftChild().getLeftChild().insertLeft(3)
    mytree.getLeftChild().getLeftChild().insertRight(4)
    mytree.getLeftChild().insertRight("*")
    mytree.getLeftChild().getRightChild().insertLeft(7)
    mytree.getLeftChild().getRightChild().insertRight(2)
    mytree.insertRight(9)

    preorder(mytree)
    print( )
    postorder(mytree)
    print( )
    inorder(mytree)
    
main()
