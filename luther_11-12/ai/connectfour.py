from turtle import *
import tkinter
from tkinter.messagebox import showinfo

def main():
    root = tkinter.Tk()
    root.title("Connect Four")
    cv = ScrolledCanvas(root,950,816,950,816)
    cv.pack(side = tkinter.LEFT)
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT)
    whoseTurn = tkinter.StringVar()
    whoseTurn.set("Player 1")
    turnTitle =tkinter.Label(frame,text="Turn")
    turnTitle.pack()
    turnFrame = tkinter.Frame(frame,height=2,bd=1,relief=tkinter.SUNKEN)
    turnFrame.pack()
    turn = tkinter.Label(turnFrame,height=2,width=20,textvariable=whoseTurn,fg="white",bg="black")
    turn.pack()
    t = RawTurtle(cv)
    t.ht()
    screen = t.getscreen()
    
    
    class Board:
        def __init__(self,board=None,):
            self.boardSpaces = []
            self.previousMove = None
            for i in range(6):
                rowList = []
                for j in range(7):
                    if board==None:
                        rowList.append(Dummy())
                    else:
                        rowList.append(int(board[i][j]))
                self.boardSpaces.append(rowList)
                
        def __len__(self):
            return len(self.boardSpaces)
        
        def __getitem__(self,key):
            return self.boardSpaces[key]
            
        def reset(self):
            self.boardSpaces = []
            for i in range(6):
                rowList = []
                for j in range(7):
                    rowList.append(Dummy())
                self.boardSpaces.append(rowList)
                
        def drop(self,col,humanTurn):
            if int(self.boardSpaces[0][col]) != 0:
                return
            else:
                row = 5
                while row != -1:
                    if int(self.boardSpaces[row][col]) != 0:
                        row -= 1
                    else:
                        if humanTurn == True:
                            self.boardSpaces[row][col] = Human()
                            self.previousMove = (row,col)
                            return (row,col)
                        else:
                            self.boardSpaces[row][col] = Computer()
                            self.previousMove = (row,col)
                            return (row,col)
                            
        def eval(self,boardPosition):
            row,col = boardPosition
            moveValue = int(self.boardSpaces[row][col])
            boardValue = 0
            
            counter = 0
            for i in range(7): #check for horizontal wins
                if int(self.boardSpaces[row][i]) == moveValue:
                    counter += 1
                    if counter == 4:
                        return moveValue
                elif int(self.boardSpaces[row][i]) == 0:
                    if counter == 2:
                        boardValue += (.01)*moveValue
                    if counter == 3:
                        boardValue += (.025)*moveValue
                    counter = 0
                else:
                    counter = 0
        
            counter = 0
            for i in range(4): #check for vertical wins
                if (row+i) < 6:
                    if int(self.boardSpaces[row+i][col]) == moveValue:
                        counter += 1
                        if counter == 4:
                            return moveValue
                    else:
                        counter = 0
            if counter == 2:
                boardValue += (.01)*moveValue
            if counter == 3:
                boardValue += (.025)*moveValue
            
            newRow = row + 3
            newCol = col - 3
            counter = 0
            for i in range(7): #check for bottom left to top right
                if newRow > -1 and newRow < 6 and newCol > -1 and newCol < 7:
                    if int(self.boardSpaces[newRow][newCol]) == moveValue:
                        counter += 1
                        newRow -= 1
                        newCol += 1
                        if counter == 4:
                            return moveValue
                    elif int(self.boardSpaces[newRow][newCol]) == 0:
                        if counter == 2:
                            boardValue += (.01)*moveValue
                        if counter == 3:
                            boardValue += (.025)*moveValue
                        counter = 0
                    else:
                        counter = 0
            
            newRow = row + 3
            newCol = col + 3
            for i in range(7): #check for bottom right to top left
                if newRow > -1 and newRow < 6 and newCol > -1 and newCol < 7:
                    if int(self.boardSpaces[newRow][newCol]) == moveValue:
                        counter += 1
                        newRow -= 1
                        newCol -= 1
                        if counter == 4:
                            return moveValue
                    elif int(self.boardSpaces[newRow][newCol]) == 0:
                        if counter == 2:
                            boardValue += (.01)*moveValue
                        if counter == 3:
                            boardValue += (.025)*moveValue
                        counter = 0
                    else:
                        counter = 0
            return boardValue
        
        def numPieces(self):
            num = 0
            for i in self.boardSpaces:
                x = i.count(1)
                y = i.count(-1)
                num += (x+y)
            return num
        
        def getPreviousMove(self):
            return (self.previousMove)
            
    class Dummy:
        def __init__(self):
            self.value = 0
        def __int__(self):
            return int(self.value)
    
    class Human:
        def __init__(self):
            self.value = -1
        def __int__(self):
            return int(self.value)
        def getTurtle(self):
            screen.tracer(0)
            t = RawTurtle(cv)
            t.shape("circle")
            t.shapesize(6,6)
            t.color("black")
            t.ht()
            t.up()
            screen.tracer(1)
            return t
        
    class Computer:
        def __init__(self):
            self.value = 1
        def __int__(self):
            return int(self.value)
        def getTurtle(self):
            screen.tracer(0)
            t = RawTurtle(cv)
            t.shape("circle")
            t.shapesize(6,6)
            t.color("red")
            t.ht()
            t.up()
            screen.tracer(1)
            return t
    
    class DrawBoard:
        def __init__(self,board):
            self.board = board
            self.vertLine = RawTurtle(cv)
            self.horzLine = RawTurtle(cv)
            self.vertLine.ht()
            self.vertLine.up()
            self.horzLine.ht()
            self.horzLine.up()
            screen.register_shape("vertLine",((0,0),(816,0),(816,5),(0,5)))
            screen.register_shape("horzLine",((0,0),(0,950),(5,950),(5,0)))
            self.vertLine.shape("vertLine")
            self.horzLine.shape("horzLine")
            self.computerTurn = False
            screen.listen()
            screen.onclick(self.mouseHandler)
        def draw(self):
            screen.tracer(0)
            screen.setworldcoordinates(0,816,950,0)
            vertStart = 0
            horzStart = 0
            for i in range(8):
                self.vertLine.goto(horzStart,0)
                self.vertLine.stamp()
                horzStart += 135
            for i in range(7):
                self.horzLine.goto(0,vertStart)
                self.horzLine.stamp()
                vertStart += 135
            screen.tracer(1)
        def dropPiece(self,boardPosition):
            row,col = boardPosition
            t = self.board[row][col].getTurtle()
            t.goto((col*135)+70,-200)
            t.st()
            t.goto((col*135)+70,(row*135)+70)
            evalNum = self.board.eval(boardPosition)
            if evalNum == 1:
                tkinter.messagebox.showinfo(None,"Computer is the winner!!")
                self.clear()
                self.board.reset()
            if evalNum == -1:
                tkinter.messagebox.showinfo(None,"Player 1 is the winner!!")
                self.clear()
                self.board.reset()
        def clear(self):
            screen.clear()
            screen.resetscreen()
            self.__init__(self.board)
            self.draw()
            self.setComputerTurn()
        def setComputerTurn(self):
            self.computerTurn = not self.computerTurn
        def mouseHandler(self,x,y):
            if self.computerTurn == True:
                pass
            else:
                col = x//135
                boardSpace = self.board.drop(int(col),True)
                if boardSpace != None:
                    self.dropPiece(boardSpace)
                    whoseTurn.set("Computer")
                    self.computerTurn = True
                    computerTurn(self.board)
                    self.computerTurn = False
                    whoseTurn.set("Player 1")
    
    def minimax(board,humanTurn,depth):
        children = []
        if board.eval(board.getPreviousMove()) == abs(1):
            return board.eval(board.getPreviousMove())
        elif depth == 0:
            return board.eval(board.getPreviousMove())
        else:
            if humanTurn == True:
                for i in range(7):
                    if int(board[0][i]) == 0:
                        newBoard = Board(board)
                        newBoard.drop(i,True)
                        children += [newBoard]
                for i in range(len(children)):
                    children[i] = minimax(children[i], False, depth-1)
                return min(children)
            if humanTurn == False:
                for i in range(7):
                    if int(board[0][i]) == 0:
                        newBoard = Board(board)
                        newBoard.drop(i,False)
                        children += [newBoard]
                for i in range(len(children)):
                    children[i] = minimax(children[i], True, depth-1)
                return max(children)
            
    def computerTurn(board):
        possibleMoves = []
        boardPosition = -1
        depth = board.numPieces() + 4 + (board.numPieces()//10)
        for i in range(3): #check for three in a row in vertical
            for j in range(7):
                threeInRow = 0
                for r in range(4):
                    threeInRow += int(board[5-(i+r)][j])
                if threeInRow == -3:
                    for r in range(4):
                        if int(board[5-(i+r)][j]) == 0:
                            boardPosition = board.drop(j,False)
                            viewBoard.dropPiece(boardPosition)
                            return
        for i in range(3): #check for three in a row, diagonal bottom left to top right
            for j in range(4):
                threeInRow = 0
                for r in range(4):
                    threeInRow += int(board[5-(i+r)][j+r])
                if threeInRow == -3:
                    for r in range(4):
                        if int(board[5-(i+r)][j+r]) == 0:
                            if (6-(i+r)) < 6:
                                if int(board[6-(i+r)][j+r]) != 0:
                                    boardPosition = board.drop(j+r,False)
                                    viewBoard.dropPiece(boardPosition)
                                    return
        for i in range(3): #check for three in a row, diagonal bottom right to top left 
            for j in range(4):
                threeInRow = 0
                for r in range(4):
                    threeInRow += int(board[5-(i+r)][6-(j+r)])
                if threeInRow == -3:
                    for r in range(4):
                        if int(board[5-(i+r)][6-(j+r)]) == 0:
                            if (6-(i+r)) < 6:
                                if int(board[6-(i+r)][6-(j+r)]) != 0:
                                    boardPosition = board.drop(6-(j+r),False)
                                    viewBoard.dropPiece(boardPosition)
                                    return
        for i in range(6): #check for three in a row in horizontals
            for j in range(4):
                threeInRow = 0
                for r in range(4):
                    threeInRow += int(board[i][j+r])
                if threeInRow == -3:
                    for r in range(4):
                        if i != 5:
                            if int(board[i+1][j+r]):
                                if int(board[i][j+r]) == 0:
                                    boardPosition = board.drop(j+r, False)
                                    viewBoard.dropPiece(boardPosition)
                                    return
                if threeInRow == -2:
                    if int(board[i][j]) == 0:
                        if int(board[i][j+3]) == 0:
                            if i != 5:
                                if int(board[i+1][j]) != 0:
                                    if int(board[i+1][j+3]) != 0:
                                        boardPosition = board.drop(j+3, False)
                                        viewBoard.dropPiece(boardPosition)
                                        return
        for i in range(7):
            if int(board[0][i]) == 0:
                newBoard = Board(board)
                newBoard.drop(i, False)
                x = minimax(newBoard, True, depth)
                possibleMoves.append(x)
        maxValue = max(possibleMoves)
        computerMove = possibleMoves.index(maxValue)
        counter = -1
        for i in range(7):
            if int(board[0][i]) == 0:
                counter += 1
                if counter == computerMove:
                    if max(possibleMoves) < abs(.015):
                        if int(board[0][3]) == 0:
                            boardPosition = board.drop(3, False)
                        elif int(board[0][4]) == 0:
                            boardPosition = board.drop(4, False)
                        elif int(board[0][2]) == 0:
                            boardPosition = board.drop(2,False)
                        else:
                            pass
                    if boardPosition != -1:
                        viewBoard.dropPiece(boardPosition)
                        return
                    boardPosition = board.drop(i, False)
                    viewBoard.dropPiece(boardPosition)
                    return
                    
    board = Board()
    viewBoard = DrawBoard(board)
    viewBoard.draw()
    
    def newGameHandler():
        viewBoard.clear()
        board.reset()
        
    def passHandler():
        viewBoard.setComputerTurn()
        whoseTurn.set("Computer")
        computerTurn(board)
        whoseTurn.set("Player 1")
        viewBoard.setComputerTurn()
    
    newGameButton = tkinter.Button(frame, text = "New Game", command=newGameHandler)
    newGameButton.pack(side = tkinter.TOP)
    passButton = tkinter.Button(frame, text = "Pass", command=passHandler)
    passButton.pack(side = tkinter.TOP)
    
    root.mainloop()
    
main()