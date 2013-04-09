'''
  File: cichelli.shell  
  Author: Steve Hubbard and ???
  Date: 11/20/11
  Description: This file implements Cichelli's perfect
    hashing algorithm.  The data file key6.dat, together with
    a maxCode = 15 shows that the perfect hashing function is
    not always minimal!
'''

from sys import stdout
import time

class CichelliKey:
   '''
     Each instance of this class contains a string and a frequencey.  The
     class Cichelli uses this class to implement Cichelli's perfect
     hashing algorithm.
   '''
   def __init__(self):
      ''' Creates an instance of the class CichelliKey which
        has an empty string and a frequency of 0.  We campare two 
        CichelliKey objects on the basis of their frequency instance 
        variables.
      '''  
      self.str = ''
      self.freq = 0

   def __str__(self):
      st = self.str[:] + ' ' + str(self.freq)
      return st

   def __gt__(self, other):
      '''
        key1 > key2 iff key1.frequency > key2.frequency.
      '''
      return self.freq > other.freq 
   
   def __ge__(self, other):
      '''
        key1 >= key2 iff key1.frequency >= key2.frequency.
      '''
      return self.freq >= other.freq 
   
   def __lt__(self, other):
      '''
        key1 < key2 iff key1.frequency > key2.frequency.
      '''
      return self.freq < other.freq 
   
   def __le__(self, other):
      '''
        key1 <= key2 iff key1.frequency <= key2.frequency.
      '''
      return self.freq <= other.freq 
   
   def __eq__(self, other):
      '''
        key1 == key2 iff key1.frequency == key2.frequency.
      '''
      return self.freq == other.freq 

   def __ne__(self, other):
      '''
        key1 != key2 iff key1.frequency != key2.frequency.
      '''
      return self.freq != other.freq 

   def getFirst(self):
      ''' Answer the first character of the receiver's string. '''
      return self.str[0]

   def getFreq(self):
      ''' Answer the frequency of the key. '''
      return self.freq

   def setFreq(self, freq):
      ''' Set the frequency of the key to freq. '''
      self.freq = freq

   def getLast(self):
      ''' Answer the last character of the receiver's string. '''
      return self.str[-1]

   def size(self):
      ''' Answer the number of characters in the receiver's
        string.
      '''
      return len(self.str)

   def getString(self):
      ''' Answer a copy of the receiver's string. '''
      return self.str[:]

   def setString(self, string):
      ''' Set the receiver's string to string. '''
      self.str = string

class Cichelli:
   def __str__(self):
      st = 'The Cichelli object:\n'
      for key in self.keys:
         st += str(key) + '\n'
      return st
         
   def hash(self, aKey):
      ''' Answer the hash value of aKey. '''
      return len(aKey.getString()) + self.code[aKey.getFirst()] \
                       + self.code[aKey.getLast()] 
      # This method is complete.

   def initFromSequence(self, theStrings):
      ''' Initialize the ordered collection of keys to the
        elements of theStrings.  theStrings is a sequence of
        strings.  Also initialze the code and charFreq
        dictionaries. Do the sorting and modifying as required
        by the Cichelli algorithm.
      '''
      self.undefined = -1  # Undefined char code
      self.letters = set()
      for x in range(ord('a'), ord('z')+ 1):
         self.letters.add(chr(x))
      self.keys = [None]*len(theStrings)
      for x in range(len(theStrings)):
         q = CichelliKey()
         q.setString(theStrings[x])
         self.keys[x] = q

      self.code = {}
      self.charFreq = {}
      # self.charFreq[ch] is the number of times ch appears
      # as a first or last letter of one of the keys.
      for x in self.letters:
         self.code[x] = self.undefined
         self.charFreq[x] = 0
      
      for i in self.keys:
         keyString = i.getString()
         firstChar = keyString[0]
         lastChar = keyString[-1]
         if firstChar in self.charFreq:
            self.charFreq[firstChar] += 1
         else:
            self.charFreq[firstChar] = 1
         if lastChar in self.charFreq:
            self.charFreq[lastChar] += 1
         else:
            self.charFreq[lastChar] = 1
      
      for i in self.keys:
         keyString = i.getString()
         frontFreq = self.charFreq[keyString[0]]
         lastFreq = self.charFreq[keyString[-1]]
         i.setFreq(frontFreq+lastFreq)
      
      self.keys.sort(reverse = True)
      self.modify()

         
   def initFromFile(self, aFile):
      ''' Initialize the ordered collection of keys to the
        elements of aFile.  aFile is a file of strings, one
        string per line.  Also do the sorting and modifying
        as required by the Cichelli algorithm.
        aFile is the name of a file.
      '''
      input =  open(aFile, "r")
      aList = []
      st = input.readline()
      while st != '':
         aList.append(st.strip())
         st = input.readline()
      input.close()
      self.initFromSequence(aList)
      # This method is complete

   def modify(self):
      ''' Modify the list of keys so that any key that has both
        of its first and last letters appear as either first or
        last letters in some earlier keys now appear as high in
        the list as possible to satisfy this condition.
      '''
      aSet = set()
      for i in range(len(self.keys)):
         firstChar = self.keys[i].getString()[0]
         lastChar = self.keys[i].getString()[-1]
         if i < 2:
            aSet.add(firstChar)
            aSet.add(lastChar)
         else:
            if firstChar in aSet:
               if lastChar in aSet:
                  foundFirstChar = False
                  foundLastChar = False
                  for key in range(len(self.keys)):
                     if foundFirstChar and foundLastChar:
                        pass
                     else:
                        keyString = self.keys[key].getString()
                        if keyString[0] == firstChar or keyString[-1] == firstChar:
                           foundFirstChar = True
                        if keyString[-1] == lastChar or keyString[0] == lastChar:
                           foundLastChar = True
                        if foundFirstChar and foundLastChar:
                           aboveValue = key
                           temp = self.keys.pop(i)
                           self.keys.insert(key+1,temp)
            aSet.add(firstChar)
            aSet.add(lastChar)
      
   def noConflict(self, index):
      ''' The precondition is that the character codes are
        defined for the first index + 1 keys of self.keys,
        self.keys[0..index].  Answer True if the hash value
        of self.keys[index] is different from the hash
        values of all the earlier keys.
      '''
      # This method is complete
      for x in range(index):
         if (self.hash(self.keys[index]) == \
             self.hash(self.keys[x])):
            return False
      return True

   def printNoSolution(self,maxCode, aFile):
      ''' Print, on aFile, the fact that with an upper bound
        of maxCode, there is no solution.
      '''
      # This method is complete
      aFile.write('With a max code of ' + str(maxCode) \
                    + ' there is no solution.')

   def printSolution(self, maxCode, aFile):
      ''' Display the solution on aFile. '''
      count = 0
      aFile.write('A solution for maxCode = ' + str(maxCode) \
                  + ':\n')
      for x in range(ord('a'),ord('z')+1):
         ch = chr(x)
         if self.code[ch] != self.undefined:
            st = str(self.code[ch])
            if (self.code[ch] < 10):
               st = ' ' + st                    
            aFile.write(ch + ' ' + st + '  ')
            count += 1
            if (count % 6 == 0):
               aFile.write('\n')
      aFile.write('\n\n')
      maxLength = 0
      for index in range(len(self.keys)):
         maxLength = max(maxLength,
                         len(self.keys[index].getString()))
      for index in range(len(self.keys)):
         aFile.write(self.keys[index].getString())
         st = ' '*(maxLength - len(self.keys[index].getString()))
         st += ' ---> '
         aFile.write(st + str(self.hash(self.keys[index])))
         aFile.write('\n')
      # This method is complete

   def solutionExistsFromIndex(self, index, maxCode):
      ''' If the algorithm finds a perfect hashing function for
        an upper limit on the code of maxCode, starting from
        self.keys[index], answer True.  If not, answer False.
        We are assuming that there is no conflict with earlier keys, and
        that their char codes have been defined for the first and last letters.
      '''
      solutionExists = False
      if index >= len(self.keys):
         solutionExists = True
      else:
         firstChar = self.keys[index].getString()[0]
         lastChar = self.keys[index].getString()[-1]
         firstCharDefined = self.code[firstChar]
         lastCharDefined = self.code[lastChar]
         if firstCharDefined != -1 and lastCharDefined != -1:
            if self.noConflict(index):
               solutionExists = self.solutionExistsFromIndex(index+1,maxCode)
         elif firstCharDefined == -1 and lastCharDefined != -1:
            firstCharDefined = 0
            while firstCharDefined <= maxCode and not solutionExists:
               self.code[firstChar] = firstCharDefined
               if self.noConflict(index):
                  solutionExists = self.solutionExistsFromIndex(index+1,maxCode)
               firstCharDefined += 1
            if not solutionExists:
               self.code[firstChar] = -1
               firstCharDefined = -1
         elif firstCharDefined != -1 and lastCharDefined == -1:
            lastCharDefined = 0
            while lastCharDefined <= maxCode and not solutionExists:
               self.code[lastChar] = lastCharDefined
               if self.noConflict(index):
                  solutionExists = self.solutionExistsFromIndex(index+1,maxCode)
               lastCharDefined += 1
            if not solutionExists:
               self.code[lastChar] = -1
               lastCharDefined = -1
         else:
            firstCharDefined = 0
            while firstCharDefined <= maxCode and not solutionExists:
               lastCharDefined = 0
               while lastCharDefined <= maxCode and not solutionExists:
                  self.code[lastChar] = lastCharDefined
                  self.code[firstChar] = firstCharDefined
                  if self.noConflict(index):
                     solutionExists = self.solutionExistsFromIndex(index+1,maxCode)
                  lastCharDefined += 1
               firstCharDefined += 1
            if not solutionExists:
               self.code[lastChar] = -1
               lastCharDefined = -1
               self.code[firstChar] = -1
               firstCharDefined = -1
      #print(solutionExists)
      return solutionExists
      
   def solve(self, maxCode, aFile):
      ''' Print on aFile a solution ot the perfect hashing
        problem if one is found.  This includes the code for
        each letter and the corresponding hashing of the keys.
        If not, indicate that no solution was found using
        maxCode as an upper bound for the code values.
      '''
      self.code = {}
      for ch in self.letters :
         self.code[ch] = self.undefined
      startTime = time.clock() # get the current time, in seconds
      if (self.solutionExistsFromIndex(0, maxCode)):
         endTime = time.clock()
         seconds = endTime - startTime
         aFile.write('The time in seconds is: ' +
                     str(seconds) + '\n')
         self.printSolution(maxCode, aFile)
      else:
         endTime = time.clock()
         seconds = endTime - startTime
         aFile.write('The time in seconds is: ' +
                     str(seconds) + '\n')
         self.printNoSolution(maxCode, aFile)

   def getStrings(self):
      '''
        Answer a list of the strings we are trying to find
        a perfect hashing function for.
      '''
      temp = []*len(self.keys)
      for k in range(len(self.keys)):
         temp.append(self.keys[k].getString())
      return temp

   def getLetters(self, aString):
      ''' Answer a set of the first and last letter of
        aString
      '''
      x = set()
      x.add(aString[0])
      x.add(aString[len(aString)-1])
      return x
   
   def check(self):
      '''
        This method answers True if and only if no two keys have
        the same length and the same set of first and last
        characters.
      '''  
      ok = True
      z = []
      # Construct a list of lists.  Each inner list contains the
      # length of the corresponding key and its set of first
      # and last letters.
      for x in range(len(self.keys)):
         y = self.keys[x].getString()
         z.append( [str(len(y)), self.getLetters(y)])
      for i in range(len(z)):
         for k in range(i+1,len(z)):
            if z[i] == z[k]:
               ok = False
      return ok

      
def main():
   print('My name is  .')
   c = Cichelli()
   c.initFromSequence(['steve', 'sue','stan'])
   print(c)

   c = Cichelli()
   c.initFromFile('key0.dat')
   print(c)
   
   ci = Cichelli()
   aList = [None]*4
   aList[0] = 'aa'
   aList[1] = 'ac'
   aList[2] = 'ab'
   aList[3] = 'bc'
   ci.initFromSequence(aList)
   ci.solve(2, stdout)
   print('\n')
    
   ci = Cichelli()
   ci.initFromFile('key0.dat')
   ci.solve(1, stdout)
   print('\n')
   
   ci = Cichelli()
   ci.initFromFile('key0.dat')
   ci.solve(4, stdout)
   print('\n')

   ci = Cichelli()
   ci.initFromFile('key1.dat')
   ci.solve(4, stdout)
   print('\n')
   
   
   ci = Cichelli()
   ci.initFromFile('key2.dat')
   ci.solve(20, stdout)
   print('\n')
   
   ci = Cichelli()
   ci.initFromFile('key3.dat')
   ci.solve(3, stdout)
   print('\n')
   
   ci = Cichelli()
   ci.initFromFile('key4.dat')
   ci.solve(5, stdout)
   print('\n')
   
   ci = Cichelli()
   ci.initFromFile('key5.dat')
   ci.solve(3, stdout)
   print('\n')
   
   ci = Cichelli()
   ci.initFromFile('key6.dat')
   ci.solve(15, stdout)
   print('\n')
   
if __name__ == '__main__': main()

''' The output of main():
>>> [evaluate cichelli.py]
My name is  .
The Cichelli object:
steve 5
sue 5
stan 4

The Cichelli object:
cat 7
gnat 7
toad 7
dog 4
ant 6
rat 6
chimp 3

The time in seconds is: 9.95936634405e-05
A solution for maxCode = 2:
a  0  b  2  c  1  

aa ---> 2
ac ---> 3
ab ---> 4
bc ---> 5


The time in seconds is: 0.000263511144573
With a max code of 1 there is no solution.

The time in seconds is: 0.000766368351285
A solution for maxCode = 4:
a  2  c  0  d  4  g  0  p  4  r  3  
t  0  

cat   ---> 3
gnat  ---> 4
toad  ---> 8
dog   ---> 7
ant   ---> 5
rat   ---> 6
chimp ---> 9


The time in seconds is: 0.000286628607826
A solution for maxCode = 4:
a  0  b  2  d  4  f  1  

aa  ---> 2
ab  ---> 4
bb  ---> 6
baa ---> 5
aad ---> 7
fa  ---> 3


The time in seconds is: 0.296829764677
A solution for maxCode = 20:
a  2  b 19  c 20  d  0  e  0  f  5  
g 10  h 12  i 19  l 20  m 20  n  9  
o  0  p  7  r  9  s 19  t  6  u 10  
v 17  w 20  y 20  

end       ---> 3
else      ---> 4
do        ---> 2
downto    ---> 6
forward   ---> 12
of        ---> 7
file      ---> 9
type      ---> 10
to        ---> 8
record    ---> 15
or        ---> 11
for       ---> 17
repeat    ---> 21
not       ---> 18
function  ---> 22
then      ---> 19
packed    ---> 13
procedure ---> 16
and       ---> 5
div       ---> 20
var       ---> 29
mod       ---> 23
program   ---> 34
case      ---> 24
const     ---> 31
nil       ---> 32
label     ---> 45
while     ---> 25
if        ---> 26
in        ---> 30
set       ---> 28
begin     ---> 33
goto      ---> 14
until     ---> 35
array     ---> 27
with      ---> 36


The time in seconds is: 7.42412792687e-05
A solution for maxCode = 3:
a  1  b  0  c  2  

ab ---> 3
ac ---> 5
bc ---> 4


The time in seconds is: 4.46984183744e-05
A solution for maxCode = 5:
a  0  b  1  c  2  

aa ---> 2
ab ---> 3
ac ---> 4
bc ---> 5


The time in seconds is: 0.000149250812603
A solution for maxCode = 3:
b  0  e  3  l  0  t  2  

ball ---> 4
lab  ---> 3
turb ---> 6
bree ---> 7
tee  ---> 8


The time in seconds is: 1.32329702518
A solution for maxCode = 15:
a 13  b 15  c  5  d  6  e  0  f  1  
g  6  i 14  k  9  l 15  m  7  n 12  
o  9  p 11  r  3  s 15  t  0  w  6  
y 15  

else     ---> 4
elif     ---> 5
except   ---> 6
raise    ---> 8
for      ---> 7
continue ---> 13
exec     ---> 9
def      ---> 10
if       ---> 17
import   ---> 20
assert   ---> 19
and      ---> 22
finally  ---> 23
yield    ---> 26
try      ---> 18
not      ---> 15
return   ---> 21
in       ---> 28
while    ---> 11
print    ---> 16
del      ---> 24
lambda   ---> 34
from     ---> 12
is       ---> 31
pass     ---> 30
class    ---> 25
or       ---> 14
global   ---> 27
break    ---> 29

'''
