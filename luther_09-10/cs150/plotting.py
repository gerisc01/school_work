#Scott Gerike
#CS 150

#Plotting program

import cTurtle
import math

t = cTurtle.Turtle()

t.up()
t.goto(-200,0)
t.down()
t.forward(400)
t.up()
t.goto(0,-200)
t.left(90)
t.down()
t.forward(400)
t.up()

t.color("green")
 
for angle in range(0,360):
	x = 50*(2*math.cos(math.radians(angle)) + math.cos(8*math.radians(angle)))
	y = 50*(2*math.sin(math.radians(angle)) + math.sin(8*math.radians(angle)))

	t.goto(x,y)
	t.dot(5)



t.exitOnClick()
