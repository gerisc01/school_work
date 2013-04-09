
'''
  File:  heap.she -- change to .py
  Author: 
  Date:
  Description:  This module provides the class Heap.  We can create heaps which
     are either largest-on-top or smallest-on-top.  We can also create heaps 
     with a maximum number of children of our choice.  As written, the default
     number of children is 3 and the default initial capacity is 5.  These
     parameters can be changed by the way we invoke the class constructor.
     
     The module also provides the efficient heap sort method.  By default, the
     methods sorts objects in increasing order.  But we can also sort objects
     in decreasing order.
     
     Our implementation works for objects of any class that understand the
     relational operators.

'''

testing = False

from math import *

def heapSort(aSequence, increasingOrder = True):
   '''  This method will answer a list of the elements of aSequence, which
     by default will be sorted in increasing order.  To sort in decreasing
     order, send a second parameter which is False.
   '''
   h = Heap(largestOnTop = increasingOrder)
   h.buildFrom(aSequence)
   for i in range(len(aSequence)):
      last = len(aSequence)-1-i
      h.data[0],h.data[last] = h.data[last],h.data[0]
      h.size = h.size - 1
      h.siftDownFromTo(0,h.size)
   return h.data

class Heap:
   '''
    The class Heap provides a generic heap abstract data type.
    The instances of this class can hold objects of any sort that
   understand the relational operators.  It also allows us to create
    heaps with any maximum number of children.
   '''
    
   DefaultCapacity = 5           #  A class variable
   DefaultNumberOfChildren = 3   #  Another class variable

   def __init__(self, capacity = DefaultCapacity,
            largestOnTop = True, numberOfChildren =
                DefaultNumberOfChildren):
      self.size = 0
      self.capacity = capacity
      self.largestOnTop = largestOnTop
      self.data = [None]*capacity
      self.numberOfChildren = numberOfChildren

   def __str__(self):
      if self.largestOnTop:
         sortOfHeap = 'largest on top'
      else:
         sortOfHeap = 'smallest on top'
      st = 'It is a ' + sortOfHeap + ' heap:\n'
      st = st + 'The size of the heap is ' + str(self.size) + '\n'
      st = st + 'The capacity of the heap is ' + str(self.capacity) + '\n'
      st = st + 'The elements of the heap are:\n'
      for i in range(self.size):
         st = st + str(self.data[i]) + '\n' 
      return st

   def addToHeap(self,newObject):
      '''If the heap is full, double its current capacity.
         Add the newObject to the heap, maintaining it as a
         heap of the same type.  Answer newObject.
      '''
      if self.size == self.capacity:
         self.data = self.data + ([None]*self.capacity)
         self.capacity = self.capacity * 2
      self.data[self.size] = newObject
      self.siftUpFrom(self.size)
      self.size = self.size + 1
      pass
      # Allows compilation of file.  Replace with actual code.

   def bestChildOf(self, index, lastIndex):
      ''' Answer the "best child" of self.data[index], assuming that
         the valid nodes end with node lastIndex, if it
         exists.  If not, answer None.
      '''
      bestChild = None
      leftChild = index * self.numberOfChildren + 1
      rightMostChild = index * self.numberOfChildren + self.numberOfChildren
      if leftChild < lastIndex:
         nextChild = leftChild+1
         bestChild = leftChild
         while nextChild < lastIndex and nextChild < rightMostChild+1:
            if self.data[bestChild] < self.data[nextChild]:
               bestChild = nextChild
            nextChild = nextChild + 1
      return bestChild
   
   def lowestChildOf(self, index, lastIndex):
      lowestChild = None
      leftChild = index * self.numberOfChildren + 1
      rightMostChild = index * self.numberOfChildren + self.numberOfChildren
      if leftChild < lastIndex:
         nextChild = leftChild+1
         lowestChild = leftChild
         while nextChild < lastIndex and nextChild < rightMostChild+1:
            if self.data[lowestChild] > self.data[nextChild]:
               lowestChild = nextChild
            nextChild = nextChild + 1
      return lowestChild
   def buildFrom(self, aSequence):
      '''  Create a heap from the elements in aSequence. '''
      self.data = []
      for i in range(len(aSequence)):
         self.data = self.data + [aSequence[i]]
      self.size = self.capacity = len(aSequence)
      finalNode = self.size - 1
      parentNode = (finalNode-1)//self.numberOfChildren
      while parentNode >= 0:
         self.siftDownFrom(parentNode)
         parentNode = parentNode - 1
      pass
      
   def siftDownFrom( self, fromIndex ):
      '''fromIndex is the index of an element in the heap.
        Pre: elements[fromIndex..size-1] satisfies the heap condition,
        except perhaps for the element data[fromIndex].
        Post:  That element is sifted down as far as neccessary to
        maintain the heap structure for elements[fromIndex..size-1].
      '''
      self.siftDownFromTo(fromIndex, self.size - 1)

   def siftDownFromTo(self, fromIndex, last):
      '''fromIndex is the index of an element in the heap.
        Pre: elements[fromIndex..last] satisfies the heap condition,
        except perhaps for the element data[fromIndex].
        Post:  That element is sifted down as far as neccessary to
        maintain the heap condition for elements[fromIndex..last].
      '''
      if self.largestOnTop:
         bestChildIndex = self.bestChildOf(fromIndex,last)
         if bestChildIndex != None:
            if self.data[(bestChildIndex)] > self.data[fromIndex]:
               self.data[bestChildIndex],self.data[fromIndex] = self.data[fromIndex],self.data[bestChildIndex]
               self.siftDownFromTo(bestChildIndex,last)
         return
      else:
         lowestChildIndex = self.lowestChildOf(fromIndex,last)
         if lowestChildIndex != None:
            if self.data[(lowestChildIndex)] < self.data[fromIndex]:
               self.data[lowestChildIndex],self.data[fromIndex] = self.data[fromIndex],self.data[lowestChildIndex]
               self.siftDownFromTo(lowestChildIndex,last)
         return
   def siftUpFrom(self, child):
      ''' child is the index of a node in the heap.  Sift that
      node up as far as necessary to ensure that the path satisfies
      the heap condition.
      '''
      parent = (child-1)//self.numberOfChildren
      if child != 0:
         if self.largestOnTop:
            if self.data[child] > self.data[parent]:
               self.data[child],self.data[parent] = self.data[parent],self.data[child]
               self.siftUpFrom(parent)
         else:
            if self.data[child] <= self.data[parent]:
               self.data[child],self.data[parent] = self.data[parent],self.data[child]
               self.siftUpFrom(parent)
      pass
   
   def removeTop(self):
      topObject = self.data.pop(0)
      self.data.insert(0,None)
      bestChild = self.bestChildOf(0,self.size-1)
      noneLocation = 0
      while bestChild != None:
         self.data[noneLocation],self.data[bestChild] = self.data[bestChild],self.data[noneLocation]
         noneLocation = bestChild
         bestChild = self.bestChildOf(noneLocation,self.size)
      self.size = self.size - 1
      return topObject
      
   def levelByLevelString(self):
      ''' Return a string which lists the contents of the heap
         level by level.
      '''
      st = ''
      st = st + 'Level 1' + '\n'
      st = st + str(self.data[0]) + '\n'
      level = 1
      i = 1
      counter = 1
      while i < self.size:
         if counter == self.numberOfChildren ** (level-1):
            level = level + 1
            counter = 0
            st = st + '\n'
            st = st + 'Level ' + str(level) + '\n'
         st = st + str(self.data[i]) + '\n'
         counter = counter + 1
         i = i + 1
      return st

   #  Other methods.
   #  Use Doc strings for all methods!
        
def main():
   h = Heap()
   h.addToHeap(20)
   h.addToHeap(40)
   h.addToHeap(-10)
   h.addToHeap(72)
   h.addToHeap(84)
   h.addToHeap(-100)
   h.addToHeap(54)
   h.addToHeap(66)
   h.addToHeap(99)
   h.addToHeap(1000)
   h.addToHeap(900)
   print(h)

   h.data[0] = 50
   h.siftDownFromTo(0, 10)
   print(h)

   h.data[0] = 60
   h.siftDownFrom(0)
   print(h)

   h = Heap(3, False)
   h.buildFrom((20,40,-10, 72, 84, -100, 54,66, 99))
   print(h)

   theList = heapSort([10, 30, -100, 50, 20, 30, -40,70, 5, 50])
   print(theList)

   theList = heapSort([10, 30, -100, 50, 20, 30, -40,70, 5, 50], False)
   print(theList)
    
   print( "\nThe following is the extra output that happens when we" )
   print( " create a heap that can have 5 children per node. \n" )
   heap = Heap(numberOfChildren = 5)
   heap.buildFrom((10, 20, -29, 16, 70, 30, 20, 100, 38, -293, \
     77, -19, -77, 230, 91, -230, -48, 23))
   print(heap)

   a = heapSort((10, 20, -29, 16, 70, 30, 20, 100, 38, -293, \
     77, -19, -77, 230, 91, -230, -48, 23))
   print(a)


   #  Extra stuff to test removeTop()
   h = Heap()
   h.addToHeap(20)
   h.addToHeap(40)
   h.addToHeap(-10)
   h.addToHeap(72)
   h.addToHeap(84)
   h.addToHeap(-100)
   h.addToHeap(54)
   h.addToHeap(66)
   h.addToHeap(99)
   h.addToHeap(1000)
   h.addToHeap(900)
   print(h)

   print(h.removeTop())
   print(h)

   print( "trying heapSort method:" )
   print( heapSort((20, -30, 45, 921, 37, 200, -1000, 4000, 57)) )
   print(  heapSort((20, -30, 45, 921, 37, 200, -1000, 4000, 57), False))
   
   h = Heap()
   h.addToHeap(20)
   h.addToHeap(40)
   h.addToHeap(-10)
   h.addToHeap(72)
   h.addToHeap(84)
   h.addToHeap(-100)
   h.addToHeap(54)
   h.addToHeap(66)
   h.addToHeap(99)
   h.addToHeap(1000)
   h.addToHeap(900)
   print()
   print( 'A level by level listing of the heap:' )
   print( h.levelByLevelString() )


if __name__ == '__main__': main()

'''  The following is the output from running this code:
It is a largest on top heap:
The size of the heap is 11.
The capacity of the heap is 20.
The elements of the heap are: 
1000
72
99
900
20
-100
54
-10
66
84
40

It is a largest on top heap:
The size of the heap is 11.
The capacity of the heap is 20.
The elements of the heap are: 
900
72
99
50
20
-100
54
-10
66
84
40

It is a largest on top heap:
The size of the heap is 11.
The capacity of the heap is 20.
The elements of the heap are: 
99
72
84
50
20
-100
54
-10
66
60
40

It is a smallest on top heap:
The size of the heap is 9.
The capacity of the heap is 9.
The elements of the heap are: 
-100
20
-10
72
84
40
54
66
99

[-100, -40, 5, 10, 20, 30, 30, 50, 50, 70]
[70, 50, 50, 30, 30, 20, 10, 5, -40, -100]

The following is the extra output that happens when we
 create a heap that can have 5 children per node. 

It is a largest on top heap:
The size of the heap is 18.
The capacity of the heap is 18.
The elements of the heap are: 
230
100
91
23
70
30
20
20
38
-293
77
-19
-77
-29
10
-230
-48
16

[-293, -230, -77, -48, -29, -19, 10, 16, 20, 20, 23, 30, 38, 70, 77, 91, 100, 230]
It is a largest on top heap:
The size of the heap is 11.
The capacity of the heap is 20.
The elements of the heap are: 
1000
72
99
900
20
-100
54
-10
66
84
40

1000
It is a largest on top heap:
The size of the heap is 10.
The capacity of the heap is 20.
The elements of the heap are: 
900
72
99
40
20
-100
54
-10
66
84

trying heapSort method:
[-1000, -30, 20, 37, 45, 57, 200, 921, 4000]
[4000, 921, 200, 57, 45, 37, 20, -30, -1000]

A level by level listing of the heap:
Level 1:
1000

Level 2:
72
99
900

Level 3:
20
-100
54
-10
66
84
40
'''
