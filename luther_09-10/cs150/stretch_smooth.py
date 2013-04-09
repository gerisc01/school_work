from cImage import *

def enlarge(mypic,multw,multh):
    w = mypic.getWidth()
    h = mypic.getHeight()
    ei = EmptyImage(w*multw,h*multh)
    for row in range(h*multh):
        for col in range(w*multw):
            originalCol = col//multw
            originalRow = row//multh
            oldpixel = mypic.getPixel(originalCol,originalRow)

            ei.setPixel(col,row,oldpixel)
            
    return ei

def smooth(badpic):
    newpic = EmptyImage(badpic.getWidth(),badpic.getHeight())

    w = badpic.getWidth()
    h = badpic.getHeight()
    
    for r in range(h):
        for c in range(w):
            tr = 0
            tg = 0
            tb = 0
            pc = 0
            for innerrow in range(max(0,r-1),min(r+2,h)):
                for innercol in range(max(0,c-1),min(c+2,w)):
                    tr = tr + badpic.getPixel(innercol,innerrow).getRed()
                    tg = tg + badpic.getPixel(innercol,innerrow).getGreen()
                    tb = tb + badpic.getPixel(innercol,innerrow).getBlue()
                    pc = pc + 1
            avgRed = tr/pc
            avgGreen = tg/pc
            avgBlue = tb/pc
            newpic.setPixel(c,r,Pixel(avgRed,avgGreen,avgBlue))
    return newpic


def main():
    mypic = FileImage("/Users/scottgerike/Downloads/koren.gif")
    w = mypic.getWidth()
    h = mypic.getHeight()
    multw = input("enlarge by what width:")
    multh = input("enlarge by what height:")
    multw = int(multw)
    multh = int(multh)
    myWin = ImageWin("Original and Sepia",w*multw,h*multh)
    ei = enlarge(mypic,multw,multh)
    ei.draw(myWin)
    print("*Done enlarging*")
    newpic = smooth(enlarge(mypic,multw,multh))
    newpic.draw(myWin)
    print("*Done smoothing*")
    myWin.exitOnClick()

main()
