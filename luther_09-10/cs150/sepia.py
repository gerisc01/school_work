from cImage import *

mypic = FileImage("/Users/scottgerike/Downloads/koren.gif")
w = mypic.getWidth()
h = mypic.getHeight()
ei = EmptyImage(w,h)

for row in range(h):
    for col in range(w):
        pix = mypic.getPixel(col,row)
        r = pix[0]
        g = pix[1]
        b = pix[2]
        newR = (r*0.393+g*0.769+b*0.189)
        if newR > 255:
            newR = 255
        newG = (r*0.349+g*0.686+b*0.168)
        if newG > 255:
            newG = 255
        newB = (r*0.272+g*0.534+b*0.131)
        if newB > 255:
            newB = 255
        ei.setPixel(col,row,Pixel(newR,newG,newB))

myWin = ImageWin("Original and Sepia",w*2,h)
mypic.draw(myWin)
ei.setPosition(w+1,0)
ei.draw(myWin)


myWin.exitOnClick()
