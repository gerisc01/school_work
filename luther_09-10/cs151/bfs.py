from cs151queue import *
from vertex import *

def bfs(g,vertKey):
    s = g.getVertex(vertKey)
    s.setDistance(0)
    s.setPred(None)
    s.setColor('gray')
    Q = Queue()
    Q.enqueue(s)
    while (Q.size() > 0):
        w = Q.dequeue()
        for v in w.getAdj():
            if v.getColor() == 'white':
                v.setColor('gray')
                v.setDistance( w.getDistance() + 1 )
                v.setPred(w)
                Q.enqueue(v)
        w.setColor('black')
