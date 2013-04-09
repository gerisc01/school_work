#Scott Gerike
#CS150
#9/18/09
#drawing concentric circles

import cTurtle

def drawSquare(someturtle, somedistance):
    for counter in range(4):
        someturtle.forward(somedistance)
        someturtle.right(90)

t = cTurtle.Turtle()

def drawConcentric(someturtle, numberofsquares, initialside, growth):
        for bigger in range(initialside, numberofsquares*growth+initialside, growth):
            drawSquare(someturtle, bigger)
            someturtle.left(90)
            someturtle.up()
            someturtle.forward(growth/2)
            someturtle.left(90)
            someturtle.forward(growth/2)
            someturtle.right(180)
            someturtle.down()
            

drawConcentric(t, 15, 20, 15)

    
        
        

t.exitOnClick()
