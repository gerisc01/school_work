from turtle import *
import tkinter
from math import fabs
from copy import deepcopy

data = {}
data['globVisited'] = []
data['drawnList'] = []

class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        if len(self.items)==0:
            return True
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]
    def empty(self):
        self.items = []
        
def main():
    root = tkinter.Tk()
    root.title("Hill Climbing")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT)
    t = RawTurtle(cv)
    t.ht()
    m = RawTurtle(cv)
    screen = t.getscreen()
    screen.setworldcoordinates(0,0,600,600)
    mazeFile = open("maze.txt","r")
    rows = int(mazeFile.readline())
    cols = int(mazeFile.readline())
    maze = []
    for line in mazeFile:
        maze.append(line)
    S = Stack()
    squareWidth = 600/cols
    squareHeight = 600/rows
    
    class Node:
        def __init__(self,col,row):
            self.row = row
            self.col = col
        def __str__(self):
            st = str(self.col) + ',' + str(self.row)
            return st
        def getCol(self):
            return self.col
        def getRow(self):
            return self.row
        def __lt__(self,other):
            if manhattenDistance(self) < manhattenDistance(other):
                return True
        def __eq__(self,other):
            if self.row == other.row and self.col == other.col:
                return True
    
    for c in range(cols):
        if maze[0][c] == ' ':
            startCol = c
    for c in range(cols):
        if maze[rows-1][c] == ' ':
            endCol = c
    startNode = Node(startCol,0)
    goalNode = Node(endCol,rows-1)
    
    def manhattenDistance(currentNode):
        curRow = currentNode.getRow()
        curCol = currentNode.getCol()
        goalRow = goalNode.getRow()
        goalCol = goalNode.getCol()
        rowDiff = goalRow - curRow
        colDiff = goalCol - curCol
        return fabs(colDiff) + fabs(rowDiff)
    
    def drawmaze():
        screen.tracer(0)
        mazeSquares = ((0,0),(squareHeight,0),(squareHeight,squareWidth),(0,squareWidth))
        screen.register_shape("square",mazeSquares)
        m.shape("square")
        m.ht()
        m.up()
        currentWidth = 0
        currentHeight = 600
        m.goto(300,300)
        for i in range(rows):
            screen.update()
            for j in range(cols):
                if maze[i][j] == "*":
                    m.goto(currentWidth,currentHeight)
                    m.stamp()
                currentWidth += squareWidth
                if currentWidth >= 600:
                    currentWidth = 0
                    currentHeight -= squareHeight
        screen.tracer(1)
        
    def adjacentNode(visitedList):
        currentNode = visitedList[0]
        row = currentNode.getRow()
        col = currentNode.getCol()
        adjList = []
        if col != cols-1:
            if maze[row][col+1] == ' ':
                if data['globVisited'].count((col+1,row)) == 0:
                    data['globVisited'].append((col+1,row))
                    adjList.append(Node(col+1,row))
        if col != 0:
            if maze[row][col-1] == ' ':
                if data['globVisited'].count((col-1,row)) == 0:
                    data['globVisited'].append((col-1,row))
                    adjList.append(Node(col-1,row))
        if row != rows-1:
            if maze[row+1][col] == ' ':
                if data['globVisited'].count((col,row+1)) == 0:
                    data['globVisited'].append((col,row+1))
                    adjList.append(Node(col,row+1))
        if row != 0:
            if maze[row-1][col] == ' ':
                if data['globVisited'].count((col,row-1)) == 0:
                    data['globVisited'].append((col,row-1))
                    adjList.append(Node(col,row-1))
        adjList.sort()
        if len(adjList) == 0:
            t.pencolor("red")
            t.pensize(7)
            t.pu()
            if data['drawnList'] != []:
                visitedList = backTracking(visitedList)
            while visitedList != []:
                nextNode = visitedList.pop()
                c = nextNode.getCol()
                r = nextNode.getRow()
                data['drawnList'].append((c,r))
                t.goto((c * squareWidth) + (squareWidth/2),600 - (r * squareHeight) - (squareHeight/2))
                t.pd()
        while len(adjList) != 0:
            temp = adjList.pop()
            newVisitedList = [temp] + visitedList
            S.push(newVisitedList)
    
    def dfs(startingNode,goalNode):
        visitedList = [startingNode]
        startRow = startingNode.getRow()
        startCol = startingNode.getCol()
        data['globVisited'].append((startCol,startRow))
        S.push(visitedList)
        while not S.isEmpty():
            temp = S.pop()
            if temp[0] == goalNode:
                drawFinishedPath(temp)
                S.empty()
            else:
                adjacentNode(temp)
    
    def backTracking(nextPath):
        backvar = False
        while not backvar:
            temp = nextPath.pop()
            if data['drawnList'].count((temp.getCol(),temp.getRow())) == 0:
                nextPath.append(temp)
                backvar = not backvar
        return nextPath
                
    def drawFinishedPath(finishedPath):
        t.pencolor("red")
        t.pensize(7)
        t.pu()
        visitedList = deepcopy(finishedPath)
        visitedList = backTracking(visitedList)
        while visitedList != []:
                nextNode = visitedList.pop()
                c = nextNode.getCol()
                r = nextNode.getRow()
                data['drawnList'].append((c,r))
                t.goto((c * squareWidth) + (squareWidth/2),600 - (r * squareHeight) - (squareHeight/2))
                t.pd()
        t.pencolor("green")
        while finishedPath != []:
            nextNode = finishedPath.pop(0)
            c = nextNode.getCol()
            r = nextNode.getRow()
            prevc = nextNode.getCol()
            prevr = nextNode.getRow()
            t.goto((c * squareWidth) + (squareWidth/2),600 - (r * squareHeight) - (squareHeight/2))
            t.pd()
    drawmaze()
    dfs(startNode,goalNode)
    root.mainloop()
                 
main()    