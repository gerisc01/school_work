'''
 File: splaytree.shell
 Author: Steve Hubbard and 
 Date: 9/17/11
 Description: This module implements the SplayTree class. This
   class in uses by the SplayNode class.  The classes
   use bottom up splaying rather than top down splaying.  We
   do not allow duplicate objects in the tree.
'''


from splaynode import SplayNode
from person import Person
from copy import deepcopy

class SplayTree:
   
   def __init__(self):
      self.size = 0
      self.root = None

   def __str__(self):
      if self.root != None:
         return str(self.root)
      else:
         return ""
   
   def delete(self, anItem):
      '''  Atempt to find a match (==) for anItem in the receiver.
      If found, splay the corresponding node to the root and answer
      the item of the node. If not found, splay the last node on
      the search path to the root. In this case, answer None.  If
      found, we remove the node and make the largest element of the
      new left subtree (from the splaying of the node to the root
      position) the new root node of the tree.  Of course finding
      the largest element uses a splaying on that left subtree.
      If there is no left subtree, the right subtree becomes the
      root.  This may leave us with an empty tree.  If found,
      decrement the size of the tree and answer the item deleted.
      If not found, answer None.
      '''
      found = self.root.find(anItem)
      self.root = found
      if anItem == found.item:
         if self.root.getLeft() != None:
            maxVal = self.root.getLeft().findMax()
            maxVal.setRight(self.root.getRight())
            self.root = maxVal
            self.size -= 1
         elif self.root.getRight() != None:
            rightVal= self.root.getRight()
            self.root = rightVal
            self.size -= 1
         else:
            self.root = None
            self.size -= 1
         return found.item
      else:
         return found.item

   def findMax(self):
      ''' Find the largest element in the splay tree.  Splay that
      element to the root.  Answer a deep copy of the element.
      If the tree is empty, answer None.
      '''
      if (self.root == None):
         return None
      self.root = self.root.findMax()
      return deepcopy(self.root.getValue())

   def findMin(self):
      ''' Find the smallest element in the splay tree.  Splay that
      element to the root.  Answer a deep copy of the element.  If
      the tree is empty, answer None.
      '''
      if (self.root == None):
         return None
      self.root = self.root.findMin()
      return deepcopy(self.root.getValue())

   def getSize(self):
      return self.size

   def inorder(self):
      ''' Print the contents of the receiver, in inorder.
        Print one item per line.
      '''
      if self.root != None:
         self.root.inorder()

   def insert(self, anItem):
      ''' Insert a deep copy of anItem into the bottom up splay tree.
      If anItem is already present in the tree, do not insert a new 
      copy of anItem.  If anItem is added, increment the size of
      the receiver.  In either case, we splay from
      the last node.  If anItem was added, answer anItem.  If not,
      answer None.
      '''
      if self.root == None:
         self.root = SplayNode(anItem)
         self.size += 1
         return anItem
      else:
         added, self.root = self.root.insertInNode(deepcopy(anItem))
         if added == True:
            self.size += 1
            return anItem
         else:
            return None
         
   def retrieve(self, anItem):
      if self.root != None:
         temp = self.root.find(anItem)
         if temp.item == anItem:
            self.root = temp
            return self.root.item
         else:
            return None
      else:
         print("Can't retreive from an empty tree")
         return None

   def update(self, anItem):
      PersonID = anItem.getId()
      found = self.retrieve(Person('',PersonID))
      if found != None:
         Name = anItem.getName()
         found.setName(Name)
         return found
      else:
         return None


def main():
   # splay0
   
   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.retrieve(1)
   print( t )
   print( 'The size of the tree is ' + str(t.getSize()) )
   
   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.findMin()
   print( t )
   
   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.retrieve(1)
   t.delete(3)
   print( t )
   
   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.retrieve(1)
   t.delete(3)
   t.findMax()
   print( t )

   t = SplayTree()
   t.insert(Person('Joe', 25))
   t.insert(Person('Jill',35))
   t.insert(Person('Jon',15))
   t.insert(Person('Jack',25))
   t.insert(Person('John',30))
   t.insert(Person('Jud',95))
   t.insert(Person('Joey',27))
   st = str(t) + '\n'
   t.update(Person('James', 25))
   st += str(t) + '\n'
   x = t.retrieve(Person('',15))
   st += str(x) + '\n'
   st += str(t) + '\n'
   x = t.delete(Person('', 35))
   st += str(x) + '\n'
   st += str(t) + '\n'
   x = t.findMax()
   st += str(x) + '\n'
   st += str(t) + '\n'
   print( st )

   print( 'The size of the tree is ' + str(t.getSize()) )

   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.insert(3.5)
   print( t )
   
   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.insert(3.5)
   t.delete(3.5)
   print( t )
   print( 'The size of the tree is ' + str(t.getSize()) )
   

   t = SplayTree()
   t.insert(3)
   t.insert(2)
   t.insert(1)
   t.delete(1)
   print( 'The size of the tree is ' + str(t.getSize()) )

   t = SplayTree()
   t.insert(Person('Joe', 25))
   t.insert(Person('Jill',35))
   t.insert(Person('Jon',15))
   t.insert(Person('Jack',25))
   t.insert(Person('John',30))
   t.insert(Person('Jud',95))
   t.insert(Person('Joey',27))
   t.inorder()
      

if __name__ == '__main__': main()

''' Output, from splaytree.py, wrapped around!
(*1(((*2(*3*))4(*5*))6(*7*)))
The size of the tree is 7
(*1(((*2(*3*))4(*5*))6(*7*)))
((*1*)2((*4(*5*))6(*7*)))
((((*1*)2(*4(*5*)))6*)7*)
(((*Name: Jon Id: 15 *)Name: Joe Id: 25 *)Name: Joey Id: 27 ((*Name: John Id: 30 *)Name: Jill Id: 35 (*Name: Jud Id: 95 *)))
((*Name: Jon Id: 15 *)Name: James Id: 25 (*Name: Joey Id: 27 ((*Name: John Id: 30 *)Name: Jill Id: 35 (*Name: Jud Id: 95 *))))
Name: Jon Id: 15 
(*Name: Jon Id: 15 (*Name: James Id: 25 (*Name: Joey Id: 27 ((*Name: John Id: 30 *)Name: Jill Id: 35 (*Name: Jud Id: 95 *)))))
Name: Jill Id: 35 
(((*Name: Jon Id: 15 (*Name: James Id: 25 *))Name: Joey Id: 27 *)Name: John Id: 30 (*Name: Jud Id: 95 *))
Name: Jud Id: 95 
((((*Name: Jon Id: 15 (*Name: James Id: 25 *))Name: Joey Id: 27 *)Name: John Id: 30 *)Name: Jud Id: 95 *)

The size of the tree is 5
((((*1*)2*)3*)3.5(((*4*)5(*6*))7*))
(((*1*)2*)3(((*4*)5(*6*))7*))
The size of the tree is 7
The size of the tree is 2
Name: Jon Id: 15 
Name: Joe Id: 25 
Name: Joey Id: 27 
Name: John Id: 30 
Name: Jill Id: 35 
Name: Jud Id: 95 
'''
   
      
   
      
