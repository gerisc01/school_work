from cTurtle import *
import random

def drawTree(t, length):
    if length >= 1:
        if length > 2:
            t.color("brown")
        if length <= 2:
            t.color("green")
        t.forward(length)
        numbranches = random.randint(3,4)
        if numbranches == 3:
            n = random.randint(20,40)      
            t.right(n)
            t.left(n-30)
            drawTree(t,length/(random.random() + 2))
            m = random.randint(20,40)
            t.left(m)
            t.right(m-30)
            drawTree(t,length/(random.random() + 2))
            p = random.randint(20,40)
            t.left(p)
            t.right(p-30)
            drawTree(t,length/(random.random() + 2))
            q = random.randint(20,40)
            t.right(q)
            t.left(q-30)
            t.backward(length)
            t.color("brown")
        if numbranches == 4:
            n = random.randint(26,46)
            t.right(n)
            t.left(n - 36)
            drawTree(t,length/(random.random() + 2))
            m = random.randint(14,34)
            t.left(m)
            t.right(m-24)
            drawTree(t,length/(random.random() + 2))
            p = random.randint(14,34)
            t.left(p)
            t.right(p-24)
            drawTree(t,length/(random.random() + 2))
            q = random.randint(14,34)
            t.left(q)
            t.right(q-24)
            drawTree(t,length/(random.random() + 2))
            r = random.randint(26,46)
            t.right(r)
            t.left(r-36)
            t.backward(length)
            t.color("brown")
def main():
    myt = Turtle()
    
    #position at bottom center, facing up
    
    myt.up()
    myt.right(90)
    myt.forward(200)
    myt.left(180)
    myt.down()

    myt.tracer(0)
    drawTree(myt, 200)
    myt.tracer(1)

    myt.exitOnClick()

main()
