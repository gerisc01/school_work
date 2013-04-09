import cTurtle

class Canvas:
    def __init__(self):
        self.turtle = cTurtle.Turtle()
        self.turtle.hideturtle()
    def draw(self, gobject):
        gobject.draw(self.turtle)
    def close(self):
        self.turtle.exitOnClick()

class GeometricObject: #Parent Fuction - takes care of both size and color
    def __init__(self):
        self.color = "black"
        self.size = 1
        self.turtle = cTurtle.Turtle()
    def getSize(self):
        return self.size
    def getColor(self):
        return self.color
    def setColor(self,acolor):
        self.color = acolor
    def setSize(self,asize):
        self.size = asize

class Point(GeometricObject):
    def __init__(self,x,y): #creates a point at the inputed x and y coordinates
        GeometricObject.__init__(self)
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,xvalue):
        self.x = xvalue
    def setY(self,yvalue):
        self.y = yvalue
    def draw(self, apoint):
        self.turtle.hideturtle()
        self.turtle.dot(self.size, self.color)
        
class Line(GeometricObject):
    def __init__(self,p1,p2): #Line constructed from point 1(p1) to point 2(p2)
        GeometricObject.__init__(self)
        self.p1 = p1
        self.p2 = p2
    def getP1(self):
        return self.p1
    def getP2(self):
        return self.p2
    def setP1(self,p1value):
        self.p1 = p1value
    def setP2(self,p2value):
        self.p2 = p2value
    def draw(self, aLine):
        self.turtle.hideturtle()
        self.turtle.up()
        self.turtle.goto(p1.getX(),p1.getY())
        self.turtle.down()
        self.turtle.goto(p2.getX(),p2.getY())

class Polygon(GeometricObject): #A figure created from a list of points (drawn in the order of the list)
    def __init__(self,cornerlist):
        GeometricObject.__init__(self)
        self.cornerPoints = cornerlist
    def numPoints(self):
        return len(self.cornerPoints)
    def addPoint(self,newpoint):
        self.cornerPoints.append(newpoint)
    def draw(self, apolygon):
        self.turtle.up()
        self.turtle.goto(self.cornerPoints[0].getX(),self.cornerPoints[0].getY())
        for i in self.cornerPoints:
            self.turtle.down()
            self.turtle.goto(i.getX(),i.getY())
        point1 = self.cornerPoints[0]
        self.turtle.goto(point1.getX(),point1.getY()) # Finishes the last line of the polygon

class Rectangle(Polygon):
    def __init__(self,p1,p2): #Where p1 and p2 have to be the points in opposite corners
        self.rectpoints = [p1,p2]
        Polygon.__init__(self, self.rectpoints)
    def getWidth(self):
        return abs(self.rectpoints[1].getX() - self.rectpoints[0].getX())
    def getHeight(self):
        return abs(self.rectpoints[0].getY() - self.rectpoints[1].getY())
    def draw(self, arect):
        self.turtle.up()
        self.turtle.goto(self.rectpoints[0].getX(),self.rectpoints[0].getY())
        self.turtle.down()
        self.turtle.goto(self.rectpoints[1].getX(),self.rectpoints[0].getY())
        self.turtle.goto(self.rectpoints[1].getX(),self.rectpoints[1].getY())
        self.turtle.goto(self.rectpoints[0].getX(),self.rectpoints[1].getY())
        self.turtle.goto(self.rectpoints[0].getX(),self.rectpoints[0].getY())

class Triangle(Polygon):
    def __init__(self,p1,p2,p3):
        self.tri = [p1,p2,p3]
        Polygon.__init__(self, self.tri)
        
        
    
