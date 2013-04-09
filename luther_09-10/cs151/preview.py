from cImage import *

mywin = ImageWin("fun",500,500)
oldim = FileImage("/Users/scottgerike/Downloads/koren.gif")
black = Pixel(0,0,0)

def blackOut(oldim, ulcol, ulrow, lrcol, lrrow):
    for row in range(ulrow,lrrow+1):
        for col in range(ulcol, lrcol+1):
            oldim.setPixel(col,row,black)
    return oldim

blackoutim = blackOut(oldim, 100, 100, 150, 150)

blackoutim.draw(mywin)
                  
