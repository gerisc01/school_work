from vertex import *

class Graph:
   def __init__(self):
      self.vertList = {}
      self.numVertices = 0
        
   def addVertex(self,key):
      self.numVertices = self.numVertices + 1
      newVertex = Vertex(key)
      self.vertList[key] = newVertex
      return newVertex
    
   def getVertex(self,n):
      if n in self.vertList:
         return self.vertList[n]
      else:
         return None

   def has_key(self,n):
       return n in self.vertList
    
   def addEdge(self,f,t,c=0):
       if f not in self.vertList:
          nv = self.addVertex(f)
       if t not in self.vertList:
          nv = self.addVertex(t)
       self.vertList[f].addNeighbor(self.vertList[t],c)
    
   def getVertices(self):
       return list(self.vertList.values())
        
   def __iter__(self):
       return iter(self.vertList.values())
