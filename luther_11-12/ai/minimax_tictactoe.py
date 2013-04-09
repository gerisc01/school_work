#Just so you know why my memoization stuff is commented out...
#So before I tried to implement memoization everything seemed to move quite quick
#after the first move. My problem though was that after I implemented memoization
#it was taking way too long to save all the boards to the dictionary... Making the
#time I waited for the first move unacceptable (it ran for over 5 minutes before
#I stopped it). I'm pretty sure the problem is that I have an inefficient
#minimax right now, which in this time frame I wasn't able to re-write without it blowing
#up. I'm still going to try and fix this though (especially because it will be useful
#for connect four coming up) so I still might stop by to get some help if I can't figure it out.

#Long story short, everything should work fine without the memoization, it just might be
#a couple of seconds slower than it would be if memoization was implemented correctly

from turtle import *
import tkinter
from tkinter.messagebox import showinfo


def main():
    #memo = {}
    root = tkinter.Tk()
    root.title("Tic Tac Toe")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT)
    whoseTurn = tkinter.StringVar()
    whoseTurn.set("Player 1(X)")
    turnTitle =tkinter.Label(frame,text="Turn")
    turnTitle.pack()
    turnFrame = tkinter.Frame(frame,height=2,bd=1,relief=tkinter.SUNKEN)
    turnFrame.pack()
    turn = tkinter.Label(turnFrame,height=2,width=20,textvariable=whoseTurn,fg="white",bg="black")
    turn.pack()
    turnIns1 = tkinter.Label(frame,text="When Game is Finished, New Game")
    turnIns1.pack()
    turnIns2 = tkinter.Label(frame,text="Will Automatically Start")
    turnIns2.pack()

    class Board:
        def __init__(self,board=None):
            self.list = []
            for i in range(3):
                rowlist = []
                for j in range(3):
                    if board == None:
                        rowlist.append(Dummy())
                    else:
                        rowlist.append(board[i][j])
                self.list.append(rowlist)
        
        def __getitem__(self,key):
            return self.list[key]
        
        def __hash__(self):
            boardValue = 0
            for i in range(3):
                for j in range(3):
                    piece = self.list[i][j].eval() + 2
                    location = (i+1)*(j+1)
                    boardValue += (piece*location)
            return boardValue
        
        def __eq__(self,other):
            if other != None:
                return self.list == other.list
            else:
                return False
        
        def reset(self):
            self.list = []
            for i in range(3):
                rowlist = []
                for j in range(3):
                    rowlist.append(Dummy())
                self.list.append(rowlist)
        
        def eval(self):
            for i in range(3): #evaluates the horizontal lines to see if there is a winning combination
                rowValue = 0
                for j in range(3):
                    squareValue = self.list[i][j].eval()
                    rowValue = rowValue + squareValue
                if abs(rowValue) == 3:
                    return rowValue//3
            
            for j in range(3): #evaluates the vertical lines to see if there is a winning combination
                colValue = 0
                for i in range(3):
                    squareValue = self.list[i][j].eval()
                    colValue = colValue + squareValue
                if abs(colValue) == 3:
                    return colValue//3
            diagValue = 0    
            for i in range(3): #evaluates diagonal from top left to bottom right
                squareValue = self.list[i][i].eval()
                diagValue = diagValue + squareValue
                if abs(diagValue) == 3:
                    return diagValue//3
            
            diagValue = 0    
            for i in range(3): #evaluates diagonal from bottom left to top right
                squareValue = self.list[i][2-i].eval()
                diagValue = diagValue + squareValue
                if abs(diagValue) == 3:
                    return diagValue//3
            
            return 0
        
        def full(self):
            isDummy = False
            for i in range(3):
                for j in range(3):
                    if self.list[i][j].eval() == 0:
                        return False
            return True
        
        def empty(self):
            isDummy = True
            for i in range(3):
                for j in range(3):
                    if self.list[i][j].eval() != 0:
                        isDummy = False
            return isDummy
    
    class X: #X is the human player, so it evaluates to 1
        def __init__(self):
            self.value = 1
            self.t = RawTurtle(cv)
            self.t.ht()
            self.t.up()
            screen = self.t.getscreen()
            diagonalA = ((0,0),(100,100),(102,98),(2,0))
            diagonalB = ((0,98),(2,100),(98,2),(100,0))
            s = Shape("compound")
            s.addcomponent(diagonalA,"black")
            s.addcomponent(diagonalB,"black")
            screen.register_shape("x",s)
            self.t.shape("x")
        def eval(self):
            return self.value
        def getTurtle(self):
            return self.t
        
    class O: #O is the computer player, so it evaluates to -1
        def __init__(self):
            self.value = -1
            self.t = RawTurtle(cv)
            self.t.ht()
            self.t.shape("circle")
            self.t.shapesize(7,7)
            self.t.up()
        def eval(self):
            return self.value
        def getTurtle(self):
            return self.t
    
    class Dummy:
        def __init__(self):
            self.value = 0
            self.t = RawTurtle(cv)
            self.t.ht()
        def eval(self):
            return self.value
        def getTurtle(self):
            return self.t
    
    class DrawBoard:
        def __init__(self,board):
            self.board = board
            self.vertLine = RawTurtle(cv)
            self.horzLine = RawTurtle(cv)
            self.vertLine.ht()
            self.vertLine.up()
            self.horzLine.ht()
            self.horzLine.up()
            self.screen = self.vertLine.getscreen()
            self.screen.register_shape("vertLine",((0,0),(600,0),(600,5),(0,5)))
            self.screen.register_shape("horzLine",((0,0),(0,600),(5,600),(5,0)))
            self.vertLine.shape("vertLine")
            self.horzLine.shape("horzLine")
            self.humanTurn = True
            self.invalidMove = False
            self.screen.listen()
            self.screen.onclick(self.mouseHandler)
        def draw(self):
            self.screen.tracer(0)
            self.horzLine.st()
            self.vertLine.st()
            self.vertLine.setpos(-100,300)
            self.vertLine.clone()
            self.vertLine.setpos(100,300)
            self.horzLine.setpos(-300,100)
            self.horzLine.clone()
            self.horzLine.setpos(-300,-100)
            self.screen.update()
        def clear(self):
            self.screen.clear()
            self.screen.resetscreen()
            self.__init__(self.board)
            self.draw()
        def findCoordinates(self,boardPosition):
            row,col = boardPosition
            if row == 0:
                rowPos = 250
            elif row == 1:
                rowPos = 50
            else:
                rowPos = -150
            
            if col == 0:
                colPos = -250
            elif col == 1:
                colPos = -50
            else:
                colPos = 150
            
            return (rowPos,colPos)
        def drawX(self,boardPosition): #boardPosition is given as a tuple... (row,col)
            whoseTurn.set("Computer(O)")
            row,col = boardPosition
            rowPos,colPos = self.findCoordinates(boardPosition)
            self.board.list[row][col] = X()
            t = self.board.list[row][col].getTurtle()
            t.goto(colPos,rowPos)
            t.st()
            self.screen.update()
            if self.board.eval() == 1:
                tkinter.messagebox.showinfo(None,"Player 1(X) is the winner!!")
                self.board.reset()
                self.clear()
            if self.board.full() == True:
                tkinter.messagebox.showinfo(None,"The game is a tie. Try Again!!")
                self.board.reset()            
                self.clear()
            self.humanTurn = False
            self.computerTurn(self.board)
            self.humanTurn = True
            whoseTurn.set("Player 1(X)")
        def drawO(self,boardPosition):
            row,col = boardPosition
            rowPos,colPos = self.findCoordinates(boardPosition)
            self.board.list[row][col] = O()
            s = self.board.list[row][col].getTurtle()
            s.goto(colPos+50,rowPos-50)
            s.st()
            self.screen.update()
            if self.board.eval() == -1:
                tkinter.messagebox.showinfo(None,"Computer(O) is the winner!!")
                self.clear()
                self.board.reset()
            if self.board.full() == True:
                tkinter.messagebox.showinfo(None,"The game is a tie. Try Again!!")
                self.board.reset()
                self.clear()
        def mouseHandler(self,x,y):
            if self.humanTurn == False:
                print("pass")
            else:
                self.humanTurn = True
                if x>-300 and x<=-100 and 100<=y and y<300: #boardSpace = (0,0)
                    if self.board.list[0][0].eval() == 0:
                        boardSpace = (0,0)
                    else:
                        self.invalidMove = True
                elif x>-100 and x<=100 and 100<=y and y<300:
                    if self.board.list[0][1].eval() == 0:
                        boardSpace = (0,1)
                    else:
                        self.invalidMove = True
                elif x>100 and x<=300 and 100<=y and y<300:
                    if self.board.list[0][2].eval() == 0:
                        boardSpace = (0,2)
                    else:
                        self.invalidMove = True
                elif x>-300 and x<=-100 and -100<=y and y<100:
                    if self.board.list[1][0].eval() == 0:
                        boardSpace = (1,0)
                    else:
                        self.invalidMove = True
                elif x>-100 and x<=100 and -100<=y and y<100:
                    if self.board.list[1][1].eval() == 0:
                        boardSpace = (1,1)
                    else:
                        self.invalidMove = True
                elif x>100 and x<=300 and -100<=y and y<100:
                    if self.board.list[1][2].eval() == 0:
                        boardSpace = (1,2)
                    else:
                        self.invalidMove = True
                elif x>-300 and x<=-100 and -300<=y and y<-100:
                    if self.board.list[2][0].eval() == 0:
                        boardSpace = (2,0)
                    else:
                        self.invalidMove = True
                elif x>-100 and x<=100 and -300<=y and y<-100:
                    if self.board.list[2][1].eval() == 0:
                        boardSpace = (2,1)
                    else:
                        self.invalidMove = True
                elif x>100 and x<=300 and -300<=y and y<-100:
                    if self.board.list[2][2].eval() == 0:
                        boardSpace = (2,2)
                    else:
                        self.invalidMove = True
                if self.invalidMove == False:
                    if self.humanTurn == True:
                        self.drawX(boardSpace)
                    else:
                        self.drawO(boardSpace)
                self.invalidMove = False
    
        def minimax(self,board,humanTurn):
            children = []
           # if list(memo.keys()).count(board) != 0:
                #return memo[board]
            if board.eval() == abs(1) or board.full():
                return board.eval()
            else:
                if humanTurn == True:
                    for i in range(3):
                        for j in range(3):
                            if board[i][j].eval() == 0:
                                newBoard = Board(board)
                                newBoard[i][j] = X()
                                children += [newBoard]
                    for i in range(len(children)):
                        #memo[children[i]] = self.minimax(children[i], not humanTurn)
                        #children[i] = memo[children[i]]
                        children[i] = self.minimax(children[i], not humanTurn)
                    return max(children)
                else:
                    for i in range(3):
                        for j in range(3):
                            if board[i][j].eval() == 0:
                                newBoard = Board(board)
                                newBoard[i][j] = O()
                                children += [newBoard]
                    for i in range(len(children)):
                        #memo[children[i]] = self.minimax(children[i], not humanTurn)
                        #children[i] = memo[children[i]]
                        children[i] = self.minimax(children[i], not humanTurn)
                    return min(children)
        
        def computerTurn(self,board):
            possibleMoves = []
            if board.empty() == True:
                self.drawO((0,0))
                return
            for i in range(3):
                    for j in range(3):
                        if board[i][j].eval() == 0:
                            newBoard = Board(board)
                            newBoard[i][j] = O()
                            x = self.minimax(newBoard, True)
                            possibleMoves.append(x)
            minValue = min(possibleMoves)
            computerMove = possibleMoves.index(minValue)
            counter = -1
            for i in range(3):
                for j in range(3):
                    if board[i][j].eval() == 0:
                        counter += 1
                        if counter == computerMove:
                            self.drawO((i,j))
                            return
        
    gameBoard = Board()
    globalBoard = DrawBoard(gameBoard)
    globalBoard.draw()
    root.mainloop()

main()
    
