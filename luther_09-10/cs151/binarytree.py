#methods: Inserting Left & Right, Setting and getting the rootvalue, Getting Left and Right Child
#Also includes Preorder traversal, Inorder Traversal and Postorder Traversal
#Reconstructed from "Problem solving with Algorithms and Data Structures", Listings 5.5 - 5.13

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.left = None
        self.right = None
    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
    def getRootVal(self):
        return self.key
    def setRootVal(self,obj):
        self.key = obj
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.key)
    def inorder(self):
            if self.left:
                self.left.inorder()
            print(self.key)
            if self.right:
                self.right.inorder()
        
    
