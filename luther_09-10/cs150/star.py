import cTurtle

def drawStar(someturtle, sidelength, sidenumber):
    for counter in range(sidenumber):
        angle = 180/sidenumber

        someturtle.forward(sidelength)
        someturtle.right(180-angle)

t = cTurtle.Turtle()

drawStar(t, 75, 7)

t.up()
t.goto(100,100)
t.down()

drawStar(t, 125, 11)

t.up()
t.goto(-100,-100)
t.down()

drawStar(t, 30, 5)

t.exitOnClick()
