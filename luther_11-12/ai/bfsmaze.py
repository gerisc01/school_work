from turtle import *
import tkinter

data = {}
data['globVisited'] = []


class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, anitem):
        self.items.insert(0,anitem)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def sort(self):
        self.items.sort()
    def empty(self):
        self.items = []

class Node:
    def __init__(self,col,row):
        self.row = row
        self.col = col
    def getCol(self):
        return self.col
    def getRow(self):
        return self.row
    def __str__(self):
        return str(self.col) + ',' + str(self.row)
    def __eq__(self,other):
        if self.row == other.row and self.col == other.col:
            return True
        
def main():
    root = tkinter.Tk()
    root.title("Breadth First Search")
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
    Q = Queue()
    squareWidth = 600/cols
    squareHeight = 600/rows
    
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
                if currentWidth == 600:
                    currentWidth = 0
                    currentHeight -= squareHeight
        screen.tracer(1)
        
    def adjacentNode(stackObject):
        turtle,visitedList = stackObject
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
        if len(adjList) != 0:
            if len(adjList) > 1:
                temp = adjList.pop()
                newVisitedList = [temp] + visitedList
                turtle.goto((temp.getCol() * squareWidth) + (squareWidth/2),600 - (temp.getRow() * squareHeight) - (squareHeight/2))
                newStackObject = (turtle,newVisitedList)
                Q.enqueue(newStackObject)
                while adjList != []:
                    temp1 = adjList.pop()
                    newTurtle = RawTurtle(cv)
                    newTurtle.pu()
                    newTurtle.goto((temp1.getCol() * squareWidth) + (squareWidth/2),600 - (temp1.getRow() * squareHeight) - (squareHeight/2))
                    newTurtle.pd()
                    newTurtle.pencolor("red")
                    newTurtle.pensize(7)
                    newVisitedList = [temp1] + visitedList
                    newStackObject = (newTurtle,newVisitedList)
                    Q.enqueue(newStackObject)
            else:
                temp = adjList.pop()
                newVisitedList = [temp] + visitedList
                newStackObject = (turtle,newVisitedList)
                turtle.goto((newVisitedList[0].getCol() * squareWidth) + (squareWidth/2),600 - (newVisitedList[0].getRow() * squareHeight) - (squareHeight/2))
                Q.enqueue(newStackObject)
            
    def bfs(startingNode,goalNode):
        visitedList = [startingNode]
        startRow = startingNode.getRow()
        startCol = startingNode.getCol()
        data['globVisited'].append((startCol,startRow))
        t.pu()
        t.pensize(7)
        t.pencolor("red")
        t.goto((startCol * squareWidth) + (squareWidth/2),600 - (startRow * squareHeight) - (squareHeight/2))
        t.pd()
        Q.enqueue((t,visitedList))
        while not Q.isEmpty():
            stackObject = Q.dequeue()
            turtle,visitedList = stackObject
            if visitedList[0] == goalNode:
                drawFinishedPath(visitedList)
                Q.empty()
            else:
                adjacentNode(stackObject)
    
    def drawFinishedPath(finishedPath):
        t.pencolor("green")
        t.pensize(7)
        t.pu()
        while finishedPath != []:
            nextNode = finishedPath.pop(0)
            c = nextNode.getCol()
            r = nextNode.getRow()
            prevc = nextNode.getCol()
            prevr = nextNode.getRow()
            t.goto((c * squareWidth) + (squareWidth/2),600 - (r * squareHeight) - (squareHeight/2))
            t.pd()
            
    drawmaze()
    bfs(Node(21,0),Node(39,15))
    root.mainloop()
    
    
                
main()       