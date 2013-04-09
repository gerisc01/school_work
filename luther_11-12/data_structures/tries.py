''' File: tries.py
    Author:  Steve Hubbard, ...
    Date:  11/3/2011
    Description:  This module uses the class BinaryNode to implement 
      binary linked tries.  This allows us to perform spelling correction, 
      implement a prefix trie, etc.
'''
test1 = True
from sys import *
from copy import *

class BinaryNode:
   ''' This class is used to implement a binary linked trie.  The item in each
      node is a character, including perhaps the null character, '\0'.  The 
      instance variables left and right are either positive integers, which 
      refer to other BinaryNode objects in the trie, are negative integers, 
      which indirectly refer to a string represented by the trie, or are 0. 
      The use of 0 plays the role of "NULL", indicating that there is no 
      right sibling of the node.
   '''

   def __init__(self, left = 0, item = None, right = 0):
      self.left = left
      self.right = right
      self.item = item

   def __str__(self):
      st = str(self.left) + ' ' + str(self.item) + \
           ' ' + str(self.right)
      return st

   def __repr__(self):
      st = str(self.left) + ' ' + str(self.item) + \
           ' ' + str(self.right)
      return st
   
   def getLeft(self):
      return self.left

   def getRight(self):
      return self.right
      
   def getItem(self):
      return self.item

   def setLeft(self, newLeft):
      self.left = newLeft 
      
   def setRight(self, newRight):
      self.right = newRight
      
   def setItem(self, newItem):
      self.item  = newItem
      

class Trie:
   ''' This class is used to implement a binary linked trie.  The item in each
      node is a character, including perhaps the null character, '\0'.  The 
      instance variables left and right are either positive integers, which 
      refer to other BinaryNode objects in the trie, are negative integers, 
      which indirectly refer to a string represented by the trie, or are 0. 
      The use of 0 plays the role of "NULL", indicating that there is no 
      right sibling of the node.
   '''

   NullChar = chr(0)
   invalidIndex = 0  # NULL
   
   def __str__(self):
      # Answer a string which represents the nodes of the trie.
      st =  ''
      for k in range(1,len(self.nodes)+ 1):
         st += 'At index ' + str(k) + ' :\n'
         st += str(self.nodes[k]) + '\n'
      return st

   def createFromFile(self, fileName):
      ''' fileName is the name of a file of words with one lower case
      word per line.  Modify the receiver to form a trie representing 
      the corresponding collection of words in fileName.
      '''
      self.init()
      temp = ''
      self.installString(temp,self.nodes[self.rootIndex])
      inputFile = open(fileName, 'r')
      word = inputFile.readline()
      word = word.strip()
      while word != '':
         self.insert(word)
         word = inputFile.readline()
         word = word.strip()
      inputFile.close()
   
   def correctAndPrint(self, aString, aFile):
      ''' Print, on aFile, a set of possible corrections for aString.
      1) If aString is in the trie, the set will contain only
         aString.
      2) If aString is not in the trie but is a substring of one or
         more strings repesented in the trie, then the set will
         contain all the superstrings of aString in the trie.
      3) If neither 1) or 2) apply, perform the 8 step correction
         algorithm (or 4 step if only one character matches), printing all 
         the resulting possible matches on aFile.
      '''
      result = self.search(aString)
      parent = result['parent']
      grand = result['grand']
      stringIndex = result['stringIndex']
      if (result['found']):# All chars of aString matched!
         if (self.nodes[parent].getLeft() < 0) or \
           ((self.nodes[self.nodes[parent].left].left < 0)\
             and (self.nodes[self.nodes[parent].left].item == \
                  Trie.NullChar)):
            aFile.write( '   ' + aString + \
                         ' is spelled correctly.\n')
         else:
            aFile.write('  Superstrings :  ') 
            self.superStringsFrom(self.nodes[parent].left, aFile)
            aFile.write('\n')
      else: #not found
         if (parent > 0):
            # Corrections from the parent node.
            self.insertedCharIn(aString,stringIndex,parent,
                                'parent', aFile)
            self.deletedCharIn(aString,stringIndex,parent,
                               'parent',aFile)
            self.substitutedCharIn(aString,stringIndex,parent,
                                   'parent',aFile)
            self.transposedCharIn(aString,stringIndex,parent,
                                  'parent',aFile)
         if (parent > 0) and (grand > 0):
            #  Corrections from the grandparent node.
            self.insertedCharIn(aString,stringIndex-1,grand,
                                'grandparent',aFile)
            self.deletedCharIn(aString,stringIndex-1,grand,
                               'grandparent',aFile)
            self.substitutedCharIn(aString,stringIndex-1,grand,
                                   'grandparent',aFile)
            self.transposedCharIn(aString,stringIndex-1,grand,
                                  'grandparent',aFile)

   def correctFromFileAndPrint(self, fileName, aFile):
      ''' fileName is the name of a file of words with one lower case
      word per line.  For each word in the file, print the possible
      corrections on aFile. 
      '''
      inputFile = open(fileName, 'r')
      word = inputFile.readline()
      word = word.strip()
      while word != '':
         aFile.write('Corrections for ' + word + ':\n')
         self.correctAndPrint(word, aFile)
         word = inputFile.readline()
         word = word.strip()
      inputFile.close()

   def correctFromFile(self, fileName):
      ''' fileName is the name of a file of words with one lower case
      word per line.  For each word in the file, print the possible
      corrections on stdout. 
      '''
      self.correctFromFileAndPrint( fileName, stdout )
 
   def deletedCharIn(self, aString, stringIndex,nodeIndex, nodeName, aFile):
      ''' We assume that aString[stringIndex] == self.nodes[nodeIndex].item.  
        Here we check to see if a char was deleted.  If so, we write each of
        the possible strings on aFile.  We are checking if a character was left
        out of aString in the next position.  Node name will either be 'parent'
        or 'grandparent'.
      '''
      solutions = set([]) 
      ''' Lots more!! solutions.add(aString) will be used if aString is a 
         candidate for a correction.  We can also use "for str in solutions:"
      '''
      nodeIndex = self.nodes[nodeIndex].getLeft()
      while nodeIndex > 0:
         if self.nodes[nodeIndex].getLeft() > 0:
            match = self.match(aString,stringIndex+1,self.nodes[nodeIndex].getLeft())
         else:
            match = None
         if match != None:
            if len(match) == len(aString)+1:
                solutions.add(match)
         nodeIndex = self.nodes[nodeIndex].getRight()
      if len(solutions) != 0:
         aFile.write("     deleted char from " + nodeName + ": ")
         for i in solutions:
            aFile.write(i + '  ')
         aFile.write('\n')
        
        
   def getFreeNodeIndex(self):
      # Answer the index of the next free node.  Update
      # self.freeIndex.
      self.freeIndex += 1
      return self.freeIndex - 1

   def init(self):
      ''' Define the rootIndex, freeIndex, fileIndex, words and nodes.
      Install the rootNode in nodes with all fields except left
      (which points to the string consisting of the empty string) defined.
      '''
      self.rootIndex = 1
      self.freeIndex = 2  # Next index for a node in the trie.
      self.fileIndex = 1  # Next index for a word in the dictionary self.nodes
      self.words = {}
      self.nodes = {}
      self.nodes[self.rootIndex] = BinaryNode()
      self.nodes[self.rootIndex].item = Trie.NullChar

   def insert(self, aString):
      ''' Add any nodes necessary to the trie to represent the
      string aString in the trie.  Answer False if aString is
      already in the trie.  If not, answer True.
      '''
      results = self.search(aString)
      found = False
      if results['found']:
         if self.nodes[results['parent']].getLeft() < 0:
            found = True
      if found:
         return False
      else:
         stringIndex = results['stringIndex'] + 1
         if stringIndex == len(aString):
            stringChar = Trie.NullChar
         else:
            stringChar = aString[stringIndex]
         parent = results['parent']
         if results['previousChild'] ==  0:
            newNodeIndex = self.getFreeNodeIndex()
            if self.nodes[parent].getLeft() < 0:               
               saveString = self.nodes[parent].getLeft()
               self.nodes[newNodeIndex] = BinaryNode(saveString,Trie.NullChar,0) #adds null node to next level
               self.nodes[parent].setLeft(newNodeIndex)
               self.insertRight(aString, stringIndex, self.nodes[newNodeIndex])
            else:
               newRight = self.nodes[parent].getLeft()
               tempNode = BinaryNode(0,Trie.NullChar,newRight)
               self.nodes[parent].setLeft(newNodeIndex)
               self.freeIndex -= 1
               self.insertRight(aString, stringIndex, tempNode)
         else:
            self.insertRight(aString, stringIndex, self.nodes[results['previousChild']])

   def insertedCharIn(self, aString, stringIndex,
                      nodeIndex, nodeName, aFile):
      ''' Print, on aFile, a matching string (if any) in the receiver.  
         We assume that aString[stringIndex] == self.nodes[nodeIndex].item.  
         Here we see if an extra char was inserted into the string.  nodeName 
         is either the string 'parent' or 'grandparent'.
      '''
      st = self.match(aString, stringIndex + 2,      
                      self.nodes[nodeIndex].left)
      if st:
         aFile.write('    inserted char from '+ nodeName \
                     + ':  ' + st + '\n')
      # This method is complete!
      
   def insertRight(self, aString, index, aNode):
      ''' Modify the trie as follows.  Insert nodes representing
      each of the characters of aString from index to the end of
      aString.  Make the first node of this list the right sibling
      of aNode.  Finally, install the string in the text file.
      '''
      newNodeIndex = self.getFreeNodeIndex()
      if index == len(aString):
            stringChar = Trie.NullChar
      else:
         stringChar = aString[index]
      newRight = aNode.getRight()
      self.nodes[newNodeIndex] = BinaryNode(0,stringChar,newRight)
      aNode.setRight(newNodeIndex)
      index += 1
      while index < len(aString):
         previousIndex = newNodeIndex
         newNodeIndex = self.getFreeNodeIndex()
         stringChar = aString[index]
         self.nodes[newNodeIndex] = BinaryNode(0,stringChar,0)
         self.nodes[previousIndex].setLeft(newNodeIndex)
         index += 1
      self.installString(aString,self.nodes[newNodeIndex])
      

   def installString(self, aString, aNode):
      ''' Right now we are sticking the word in a dictionary at
      self.fileIndex
      '''
      aNode.left = - self.fileIndex
      self.fileIndex += 1
      self.words[self.fileIndex - 1] = aString

   def match(self, aString, stringIndex, nodeIndex):
      ''' If the trie contains a word which matches the characters
        of aString, from stringIndex to the end of the string,
        starting at the subtree rooted at nodeIndex, answer the
        matching string.  If not, answer None.  
      '''
      while nodeIndex > 0:
         if self.nodes[nodeIndex].getItem() == Trie.NullChar and stringIndex == len(aString):
               nodeIndex = self.nodes[nodeIndex].getLeft()
         else:
            if stringIndex >= len(aString):
               return None
            stringChar = aString[stringIndex]
            if self.nodes[nodeIndex].getItem() == stringChar:
               stringIndex += 1
               nodeIndex = self.nodes[nodeIndex].getLeft()
            elif self.nodes[nodeIndex].getItem() < stringChar:
               if self.nodes[nodeIndex].getRight() != 0:
                  nodeIndex = self.nodes[nodeIndex].getRight()
               else:
                  return None
            else:
               return None
      return self.words[abs(nodeIndex)]

   def readFromWordFileAt(self, anIndex):
      ''' anIndex is an index (an integer) to the dictionary of
      words.  Return the corresponding word, or None if index is
      not a valid key.
      '''
      if self.words.__contains__(anIndex):
         return self.words[anIndex]
      else:
         return None

   def search(self, aString):
      ''' Answer a dictionary, result,  which contains the result
      of the search.
        If all the letters of aString match entries of the
        receiver, then
          result['found'] -- True
          result['parent'] -- the index of the last node where a
            match occurred.
          result['grand'] -- the index of the node one level up where
            the second to the last match occurred, or 0 if there is
            only one character in aString.
        If not all of the characters of aString match entries of the
        trie, then
          result['found'] -- False
          result['parent'] -- the index of the last node where a
            match occurred, or the index of the rootnode if no
            matches occurred.
          result['grand'] -- the index of the node one level up where
            the second to the last match occurred, index of the root node
            if only one match, and 0 for no matches.
          result['stringIndex'] -- the index of the last character of
            aString which matched the character of the parent node, or
            -1 if no characters matched.
          result['previousChild'] -- the index of the left sibling
            (or 0) of the first character which is greater than
            the character we are trying to match (or last child if
            all the characters are smaller than the character we
            are trying to match').  0 means our current character in aString
            is smaller than all of the characters at the current level.
      '''
      result = {}
      result['parent'] = 1
      result['grand'] = 0
      result['previousChild'] = 0
      result['found'] = False
      stringIndex = 0
      currentNode = 1
      while stringIndex != len(aString):
         continueSearch = True
         stringChar = aString[stringIndex] 
         while continueSearch:
            if currentNode < 0:
               result['stringIndex'] = stringIndex - 1
               return result
            if self.nodes[currentNode].getItem() == stringChar:
               result['previousChild'] = 0
               result['grand'] = result['parent']
               result['parent'] = currentNode
               currentNode = self.nodes[currentNode].getLeft()
               stringIndex += 1
               continueSearch = False
            elif self.nodes[currentNode].getItem() > stringChar:
               stringIndex -= 1
               result['stringIndex'] = stringIndex
               return result
            else:
               result['previousChild'] = currentNode
               currentNode = self.nodes[currentNode].getRight()
               if currentNode == 0:
                  stringIndex -= 1
                  result['stringIndex'] = stringIndex
                  return result
      stringIndex -= 1
      result['stringIndex'] = stringIndex
      result['found'] = True
      return result
      
      
   def substitutedCharIn(self, aString, stringIndex,nodeIndex, nodeName, aFile):
      ''' Print, on aFile, all corresponding matching strings in the
      receiver.  We assume that aString[stringIndex] ==
      self.nodes[nodeIndex].item.  Here we check to see if there
      has been a char substituted in the string, aString.
      '''
      solutions = set([]) 
      ''' Lots more!! solutions.add(aString) will be used if aString is a 
         candidate for a correction.  We can also use "for str in solutions:"
      '''
      temp = self.nodes[nodeIndex].getLeft()
      stringIndex += 2
      done = False
      while not done:
         if temp < 0:
            done = True
            return self.words[abs(temp)]
         if self.nodes[temp].getLeft() < 0:
            if len(self.words[abs(self.nodes[temp].getLeft())]) == len(aString):
               solutions.add(self.words[abs(self.nodes[temp].getLeft())])
         else:
            match = self.match(aString,stringIndex,self.nodes[temp].getLeft())
            if match != None:
               if len(match) == len(aString):
                  solutions.add(match)
         temp = self.nodes[temp].getRight()
         if temp == 0:
            done = True
      if len(solutions) != 0:
         aFile.write("     substituted char from " + nodeName + ": ")
         for i in solutions:
            aFile.write(i + '  ')
         aFile.write('\n')
            
   def superStringsFrom(self, parent, aFile):
      ''' Print, on aFile, all strings which are represented by
      the terminal nodes of the subtree rooted at index parent in
      self.nodes
      '''
      if self.nodes[parent].getLeft() > 0:
         self.superStringsFrom(self.nodes[parent].getLeft(), aFile)
      if self.nodes[parent].getLeft() < 0:
         wordsIndex = self.nodes[parent].getLeft()
         aFile.write(self.words[abs(wordsIndex)])
         aFile.write('  ')
      if self.nodes[parent].getRight() != 0:
         self.superStringsFrom(self.nodes[parent].getRight(), aFile)

   def transposedCharIn(self, aString, stringIndex, nodeIndex, nodeName, aFile):
      ''' Print, on aFile, all corresponding strings in the
      receiver.  We assume that aString[stringIndex] ==
      self.nodes[nodeIndex].item.  Here we check to see if two
      chars were transposed in aString.
      '''
      if len(aString) <= stringIndex +1:
         stringChar1 = ''
      else:
         stringChar1 = aString[stringIndex+1]
      if len(aString) <= stringIndex+2:
         stringChar2 = ''
      else:
         stringChar2 = aString[stringIndex+2]
      newString = aString[0:stringIndex+1] + stringChar2 + stringChar1 + aString[stringIndex+3:]
      match = self.match(newString,stringIndex,nodeIndex)
      if match != None:
         if len(match) == len(aString):
            aFile.write("    transposed char from " + nodeName + ": " + match)
            aFile.write('\n')
      
   
def main():
   print('Our names are Scott Gerike and Erik Streufert')
   trie = Trie()
   trie.createFromFile('trie5.dat')
   aFile = open('trie5.me','w')
   aFile.write( str(trie) + '\n')
   trie.correctFromFileAndPrint('trie5.tes', aFile);
   aFile.close()
   aFile = open('trie5.me','r')  # Compare with trie5.out
   print(aFile.read())
   aFile.close()
   
   
   trie = Trie()
   trie.createFromFile('trie1.dat')
   print( trie )
   trie.correctFromFile('trie1.tes')
   print(trie.words)
   

if __name__ == '__main__': main()
'''
>>> [evaluate tries.py]
At index 1 :
-1 \000 2
At index 2 :
15 b 12
At index 3 :
4 o 8
At index 4 :
5 l 6
At index 5 :
-2 d 0
At index 6 :
7 m 10
At index 7 :
-3 b 0
At index 8 :
9 u 0
At index 9 :
-4 t 0
At index 10 :
11 o 0
At index 11 :
-5 t 0
At index 12 :
13 d 0
At index 13 :
14 a 0
At index 14 :
-6 m 0
At index 15 :
16 m 3
At index 16 :
-7 o 0

Corrections for bonb:
    substituted char from parent:  bomb 
Corrections for blod:
    transposed char from parent:  bold
Corrections for bopmb:
    inserted char from parent:  bomb
Corrections for bod:
    deleted char from parent:  bold 
Corrections for bom:
  Superstrings :  bomb 
Corrections for bmut:
    inserted char from grandparent:  but
Corrections for bot:
    deleted char from parent:  boot 
    deleted char from grandparent:  boot 
    substituted char from grandparent:  but 
Corrections for bomb:
   bomb is spelled correctly.
Corrections for bo:
  Superstrings :  bold bomb boot 

At index 1 :
-1 \000 17
At index 2 :
11 m 13
At index 3 :
19 i 8
At index 4 :
20 l 6
At index 5 :
-2 k 0
At index 6 :
7 n 0
At index 7 :
-3 d 0
At index 8 :
9 o 0
At index 9 :
10 s 0
At index 10 :
-4 t 0
At index 11 :
12 a 3
At index 12 :
-5 d 0
At index 13 :
15 o 0
At index 14 :
-6 k 0
At index 15 :
16 d 14
At index 16 :
-7 d 0
At index 17 :
18 a 2
At index 18 :
-8 t 0
At index 19 :
-9 a 4
At index 20 :
-10 \000 5

Corrections for moot:
    substituted char from parent:  most 
Corrections for maad:
    inserted char from parent:  mad
    inserted char from grandparent:  mad
Corrections for ma:
  Superstrings :  mad 
Corrections for md:
    deleted char from parent:  mad 
Corrections for midn:
    transposed char from parent:  mind
Corrections for mi:
  Superstrings :  mia mil milk mind 
Corrections for mond:
    substituted char from grandparent:  mind 
Corrections for miost:
    inserted char from grandparent:  most
Corrections for mond:
    substituted char from grandparent:  mind 
Corrections for mint:
    substituted char from parent:  mind 
Corrections for miont:
Corrections for moint:
{1: '', 2: 'milk', 3: 'mind', 4: 'most', 5: 'mad', 6: 'ok', 7: 'odd', 8: 'at', 9: 'mia', 10: 'mil'}
>>> 
'''

