from bfs import *
from graph import *
from vertex import *

g = Graph()

g.addVertex(4)
g.addVertex(7)
g.addVertex(55)
g.addVertex(12)
g.addVertex(54)

g.addEdge(4,7, "A")
g.addEdge(7,55 , "B")
g.addEdge(55,12, "C")
g.addEdge(12,54, "D")

g.addEdge(7,4, "A")
g.addEdge(55,7, "B")
g.addEdge(12,55, "C")
g.addEdge(54,12, "D")

bfs(g, 4)
