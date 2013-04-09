from cs151queue import *
import random

class SortingMachine:
    def __init__(self):
        self.mainbin = Queue()
        self.binList = []
        for i in range(10):
            self.binList.append(Queue())
    def load(self, numList):
        for anum in numList:
            self.mainbin.enqueue(anum)
    def passes(self):
        while self.mainbin.isEmpty() == False:
            num = self.mainbin.dequeue()
            ones = num%10
            self.binList[ones].enqueue(num)
        for aqueue in range(len(self.binList)):
            while self.binList[aqueue].isEmpty() == False:
                self.mainbin.enqueue(self.binList[aqueue].dequeue())
        while self.mainbin.isEmpty() == False:
            num = self.mainbin.dequeue()
            tens = (num%100)//10
            self.binList[tens].enqueue(num)
        for aqueue in range(len(self.binList)):
            while self.binList[aqueue].isEmpty() == False:
                self.mainbin.enqueue(self.binList[aqueue].dequeue())
        while self.mainbin.isEmpty() == False:
            num = self.mainbin.dequeue()
            hundreds = (num%1000)//100
            self.binList[hundreds].enqueue(num)
        for aqueue in range(len(self.binList)):
            while self.binList[aqueue].isEmpty() == False:
                self.mainbin.enqueue(self.binList[aqueue].dequeue())
        
    def unload(self):
        sortedList = []
        while self.mainbin.isEmpty() == False:
            num = self.mainbin.dequeue()
            print(num)

def numList(amount):
    numList = []
    for i in range(amount+1):
        numList.append(random.randrange(1000))
    return numList
        
def main():
    m = SortingMachine()
    numberlist = numList(15)
    m.load(numberlist)
    m.passes()
    m.unload()

main()
