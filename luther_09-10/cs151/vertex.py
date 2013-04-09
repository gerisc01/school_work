import sys

class Vertex:
    def __init__(self,num):
        self.id = num
        self.adj = []
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0
        self.cost = {}
        
    def addNeighbor(self,nbr,cost=0):
        self.adj.append(nbr)
        self.cost[nbr] = cost

    def __str__(self):
        return str(self.id) + ":color " + self.color + \
               ":dist " + str(self.dist) + \
               ":pred [" + str(self.pred)+ "]\n"

    def getCost(self,nbr):
        return self.cost[nbr]
    def setCost(self,nbr,cost):
        self.cost[nbr] = cost
    def setColor(self,color):
        self.color = color
    def setDistance(self,d):
        self.dist = d
    def setPred(self,p):
        self.pred = p
    def setDiscovery(self,dtime):
        self.disc = dtime
    def setFinish(self,ftime):
        self.fin = ftime
    def getFinish(self):
        return self.fin
    def getDiscovery(self):
        return self.disc
    def getPred(self):
        return self.pred
    def getDistance(self):
        return self.dist
    def getColor(self):
        return self.color
    def getAdj(self):
        return self.adj
    def getId(self):
        return self.id
