#Scott Gerike
#CS150
#09/12/09
#Drawing rectangles through functions

import cTurtle
t = cTurtle.Turtle()

def drawRectangle(someturtle, width, height, fill_color):
    someturtle.fillcolor(fill_color)
    someturtle.begin_fill()
    someturtle.forward(width)
    someturtle.right(90)
    someturtle.forward(height)
    someturtle.right(90)
    someturtle.forward(width)
    someturtle.right(90)
    someturtle.forward(height)
    someturtle.right(90)
    someturtle.end_fill()

t.up()
t.goto(0,175)
t.left(90)
drawRectangle(t, 100, 50, "blue")
t.left(90)
t.forward(50)
t.right(180)
drawRectangle(t, 150, 200, "red")
t.right(90)
t.forward(90)
t.right(90)
drawRectangle(t, 75, 25, "green")
t.right(180)
t.forward(150)
drawRectangle(t, 75, -25, "green")
t.right(90)
t.forward(110)
t.right(90)
t.forward(145)
t.left(180)
drawRectangle(t, 35, 130, "black")
t.forward(105)
drawRectangle(t, 35, 130, "black")
t.goto(15,255)
t.dot(5)
t.forward(20)
t.dot(5)
t.goto(10,215)
t.down()
t.forward(30)


t.exitOnClick()
