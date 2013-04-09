from turtle import *
import math
import tkinter

data = {}
data["previousNode"] = None
data["path"] = None

def isAdjacent(m,c,b,visitedList):
    oppm = 3 - m
    oppc = 3 - c
    if m < 0 or c < 0 or m >3 or c>3:
        return False
    elif visitedList.count((m,c,b)) == 1:
        return False
    elif m < c and m != 0:
        return False
    elif oppm < oppc and oppm != 0:
        return False
    else:
        return True
        
def adjacent(currentNode,visitedList,adjacentList):
    m,c,b = currentNode
    oppb = 1 - b
    if b == 1:
        if isAdjacent(m-2,c,oppb,visitedList) == True:
            adjacentList += [(m-2,c,oppb)]
        if isAdjacent(m,c-2,oppb,visitedList) == True:
            adjacentList += [(m,c-2,oppb)]
        if isAdjacent(m-1,c,oppb,visitedList) == True:
            adjacentList += [(m-1,c,oppb)]
        if isAdjacent(m,c-1,oppb,visitedList) == True:
            adjacentList += [(m,c-1,oppb)]
        if isAdjacent(m-1,c-1,oppb,visitedList) == True:
            adjacentList += [(m-1,c-1,oppb)]
    else:
        if isAdjacent(m+2,c,oppb,visitedList) == True:
            adjacentList += [(m+2,c,oppb)]
        if isAdjacent(m,c+2,oppb,visitedList) == True:
            adjacentList += [(m,c+2,oppb)]
        if isAdjacent(m+1,c,oppb,visitedList) == True:
            adjacentList += [(m+1,c,oppb)]
        if isAdjacent(m,c+1,oppb,visitedList) == True:
            adjacentList += [(m,c+1,oppb)]
        if isAdjacent(m+1,c+1,oppb,visitedList) == True:
            adjacentList += [(m+1,c+1,oppb)]
            
def dfs(currentNode,goalNode,visitedList):
    adjacentList = []
    if currentNode == goalNode:
        visitedList += [currentNode]
        return
    elif visitedList.count(currentNode) == 1:
        visitedList = []
        return
    else:
        visitedList += [currentNode]
        adjacent(currentNode,visitedList,adjacentList)
        if adjacentList == []:
            return
        else:
            i = adjacentList.pop(0)
            dfs(i,goalNode,visitedList)
    return visitedList

def main():
    root = tkinter.Tk()
    root.title("Missionaries And Cannibals")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT)
    turnIns1 = tkinter.Label(frame,text="Red = Cannibals")
    turnIns1.pack()
    turnIns2 = tkinter.Label(frame,text="Yellow = Missionaries")
    turnIns2.pack()
    data["path"] = dfs((3,3,1),(0,0,0),[])
    river = RawTurtle(cv)
    screen = river.getscreen()
    screen.tracer(0)
    can1 = RawTurtle(cv)
    can2 = RawTurtle(cv)
    can3 = RawTurtle(cv)
    mis1 = RawTurtle(cv)
    mis2 = RawTurtle(cv)
    mis3 = RawTurtle(cv)
    boat = RawTurtle(cv)
    boat.shape("square")
    boat.color("brown")
    boat.up()
    boat.goto(-150,0)
    can1.shape("circle")
    can1.color("red")
    can1.up()
    can1.goto(-150,-215)
    can2.shape("circle")
    can2.color("red")
    can2.up()
    can2.goto(-150,-150)
    can3.shape("circle")
    can3.color("red")
    can3.up()
    can3.goto(-150,-75)
    mis1.shape("circle")
    mis1.color("yellow")
    mis1.up()
    mis1.goto(-150,75)
    mis2.shape("circle")
    mis2.color("yellow")
    mis2.up()
    mis2.goto(-150,150)
    mis3.shape("circle")
    mis3.color("yellow")
    mis3.up()
    mis3.goto(-150,215)
    screen.register_shape("River",((0,0),(600,0),(600,50),(0,50)))
    river.shape("River")
    river.up()
    river.color("brown","blue")
    river.goto(0,300)
    screen.update()
    data["previousNode"] = data["path"].pop(0)
    
    
    def nextMoveHandler():
        if data["previousNode"] == (0,0,0):
            data["path"] = dfs((3,3,1),(0,0,0),[])
            data["previousNode"] = data["path"].pop(0)
        pos = boat.xcor()
        currentNode = data["path"].pop(0)
        a,b,c = data["previousNode"]
        x,y,z = currentNode
        movMis = x - a
        movCan = y - b
        for i in range(int(math.fabs(movMis))):
            if mis1.xcor() == pos:
                mis1.forward(300)
                mis1.right(180)
            elif mis2.xcor() == pos:
                mis2.forward(300)
                mis2.right(180)
            else:
                mis3.forward(300)
                mis3.right(180)
        for i in range(int(math.fabs(movCan))):
            if can1.xcor() == pos:
                can1.forward(300)
                can1.right(180)
            elif can2.xcor() == pos:
                can2.forward(300)
                can2.right(180)
            else:
                can3.forward(300)
                can3.right(180)
        boat.forward(300)
        boat.right(180)
        screen.update()
        data["previousNode"] = currentNode
    nextMoveButton = tkinter.Button(frame, text = "Next Move", command=nextMoveHandler)
    nextMoveButton.pack()
    root.mainloop()

main()

        