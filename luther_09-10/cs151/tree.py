from cTurtle import *
import random

def drawTree(t, length):
    if length >= 1:
        t.forward(length)
        numbranches = random.randint(3,5)
        if numbranches == 3:
            n = random.randint(25,35)      
            t.right(n)
            t.left(n-30)
            drawTree(t,length/random.randrange(2,5))
            m = random.randint(25,35)
            t.left(m)
            t.right(m-30)
            drawTree(t,length/random.randrange(2,5))
            p = random.randint(25,35)
            t.left(p)
            t.right(p-30)
            drawTree(t,length/random.randrange(2,5))
            q = random.randint(25,35)
            t.right(q)
            t.left(q-30)
            t.backward(length)
        if numbranches == 4:
            n = random.randint(13,23)      
            t.right(n)
            t.left(n-18)
            drawTree(t,length/random.randrange(2,5))
            m = random.randint(13,23)
            t.left(m)
            t.right(m-18)
            drawTree(t,length/random.randrange(2,5))
            p = random.randint(13,23)
            t.left(p)
            t.right(p-18)
            drawTree(t,length/random.randrange(2,5))
            q = random.randint(13,23)
            t.left(q)
            t.right(q-18)
            r = random.randint(13,23)
            t.right(r)
            t.left(r-18)
            t.backward(length)

def main():
    myt = Turtle()
    
    #position at bottom center, facing up
    
    myt.up()
    myt.right(90)
    myt.forward(200)
    myt.left(180)
    myt.down()

    myt.tracer(10)
    drawTree(myt, 200)

    myt.exitOnClick()

main()

