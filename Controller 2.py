'''
Created on Mar 21, 2017

@author: Madalina
'''
from cmath import inf

class Controller:
    def __init__(self, repo):
        self.__repo = repo
        
    def getGraph(self):
        return self.__repo.graph
        
    def getNrVertices(self, g):
        return self.__repo.getNrVertices(g)
    
    def getNrEdges(self, g):
        return self.__repo.getNrEdges(g)
    
    def isEdge(self, g, v1, v2):
        return self.__repo.isEdge(g, v1, v2)
    
    def getInDegree(self, g, v):
        return self.__repo.getInDegree(g, v)
    
    def getOutDegree(self, g, v):
        return self.__repo.getOutDegree(g, v)
    
    def getOutbound(self, g, v):
        return self.__repo.getOutbound(g, v)
    
    def getInbound(self, g, v):
        return self.__repo.getInbound(g, v)
    
    def showAll(self, g):
        return self.__repo.showAll(g)
    
    def getCost(self, g, v1, v2):
        return self.__repo.getCost(g, v1, v2)
    
    def setCost(self, g, v1, v2, c):
        return self.__repo.setCost(g, v1, v2, c)
    
    def addEdge(self, g, v1, v2, c):
        return self.__repo.addEdge(g, v1, v2, c)
    
    def removeEdge(self, g, v1, v2):
        return self.__repo.removeEdge(g, v1, v2)
    
    def addVertex(self, g, v):
        return self.__repo.addVertex(g, v)
    
    def removeVertex(self, g, v):
        return self.__repo.removeVertex(g, v)
    
    def topologicalSort(self, g):
        sortedList = []
        q = []
        count = {}
        for vertex in g.parseAll():
            count[vertex] = g.getInDegree(vertex)
            if count[vertex] == 0:
                q.append(vertex)
        
        while q != []:
            vertex = q.pop(0)
            sortedList.append(vertex)
            for x in g.parseOutbound(vertex):
                count[x] = count[x] - 1
                if count[x] == 0:
                    q.append(x)
    
        if len(sortedList) < g.getNrVertices():
            return None
        
        return sortedList
    
    def negateCosts(self, allCosts):
        for pair in allCosts:
            allCosts[pair] = 0 - allCosts[pair]
            
        return allCosts
    
    def ford(self, g, start, end):
        costs = self.negateCosts(g.getAllCosts())
        dist = {}
        prev = {}
        for vertex in g.parseAll():
            dist[vertex] = inf
            
        dist[start] = 0
        prev[start] = False
        changed = True
        while changed:
            changed = False
            for (x,y) in g.getAllCosts():
                if dist[y] > dist[x] + costs[(x, y)]:
                    dist[y] = dist[x] + costs[(x, y)]
                    prev[y] = x
                    changed = True
        return prev, dist
    
    def maxCost(self, g, start, end):
        prev, dist = self.ford(g, start, end)
        if end not in prev:
            return False, 0
        
        q = []
        last = end
        while last != start:
            q.insert(0, last)
            last = prev[last]
        q.insert(0, last)
        return q, -dist[end]
    
    def df(self, v, visited, processed):
        g = self.getGraph()
        for x in g.parseOutbound(v):
            if x not in visited:
                visited.append(x)
                self.df(x, visited, processed)
        processed.append(v)
        
    def connectedComponents(self):
        g = self.getGraph()
        visited = []
        processed = []
        for s in g.parseAll():
            if s not in visited:
                visited.append(s)
                self.df(s, visited, processed)
        
        while len(visited) > 0:
            visited.pop()
            
        q = []
        c = 0
        comp = {}
        
        while processed != []:
            s = processed.pop()
            if s not in visited:
                c = c + 1
                comp[s] = c
                q.append(s)
                visited.append(s)
                while q != []:
                    x = q.pop(0)
                    for y in g.parseOutbound(x):
                        if y not in visited:
                            visited.append(y)
                            q.append(y)
                            comp[y] = c
                            
        return comp
                            
    def printConnectedComponents(self):
        comp = self.connectedComponents()
        c = 0
        for x in comp:
            if comp[x] > 0:
                c = comp[x]
                
        for i in range(1, c + 1):
            result = str(i) + ": "
            for x in comp:
                if comp[x] == i:
                    result = result + str(x) + " "
            print(result)

    def dijkstra(self, s, t):
        g = self.getGraph()
        q = []
        dist = {}
        prev = {}
        q.append((s,0))
        dist[s] = 0
        found = False
        while q != [] and found != True:
            x = q.pop(0)[0]
            for y in g.parseOutbound(x):
                if y not in dist.keys() or dist[x] + g.getCost(x, y) < dist[y]:
                    dist[y] = dist[x] + g.getCost(x, y)
                    q.append((y, dist[y]))
                    prev[y] = x
                    
            if x == t:
                found = True
                
        return prev, dist
                
    def minCost(self, start, end):
        prev, dist = self.dijkstra(start, end)
        if end not in prev:
            return False, 0
        
        q = []
        last = end
        while last != start:
            q.insert(0, last)
            last = prev[last]
        q.insert(0, last)
        return q, dist[end]