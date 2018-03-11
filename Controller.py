'''
Created on Mar 21, 2017

@author: Madalina
'''

from heapq import heappop, heappush

class Controller:
    def __init__(self, repo):
        self.__repo = repo
        self.result = []
        
    def getGraph(self):
        return self.__repo.graph
        
    def getNrVertices(self):
        return self.__repo.getNrVertices()
    
    def getNrEdges(self):
        return self.__repo.getNrEdges()
    
    def isEdge(self, v1, v2):
        return self.__repo.isEdge(v1, v2)
    
    def getDegree(self, v):
        return self.__repo.getDegree(v)
    
    def getNeighbours(self, v):
        return self.__repo.getNeighbours(v)
    
    def showAll(self):
        return self.__repo.showAll()
    
    def addEdge(self, v1, v2, c):
        return self.__repo.addEdge(v1, v2, c)
    
    def valid(self, stack, v):
        if v == 0 and len(stack) == self.getNrVertices():
            return True
        
        if v in stack:
            return False
        
        return True
    
    def back(self, stack):
        if self.result == []:
            if len(stack) == self.getNrVertices() + 1:
                print(stack)
                for v in stack:
                    self.result.append(v)
            else:
                for v in self.getNeighbours(stack[-1]):
                    if self.valid(stack, v) == True:
                        stack.append(v)
                        self.back(stack)
                        del stack[-1]
        
    def hamiltonian(self):
        stack = [0]
        
        self.back(stack)

        if self.result == []:
            return False
        else:
            return self.result
        
    def df(self, v, visited, processed):
        g = self.getGraph()
        for x in g.parseNeighbours(v):
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
                    for y in g.parseNeighbours(x):
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
            
    def find(self,parent,i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find(parent, parent[i])

    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set



    def Kruskal(self):

        result = []  # This will store the resultant MST

        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        # Step 1:  Sort all the edges in non-decreasing order of their
        # cost/weight.
        self.graph = sorted(self.graph, key=lambda item: item[2])
        print(self.graph)

        parent = []

        # Create V subsets with single elements
        parent = [-1] * (self.v)

        # Number of edges to be taken is equal to V-1
        while e < self.v - 1:

            # Step 2: Pick the smallest edge and increment the index
            # for next iteration
            u, v, c = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't cause cycle, include it
            # in result and increment the index of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, c])
                self.union(parent, x, y)
                # Else discard the edge

        # print the contents of result[] to display the built MST
        print("Following are the edges in the constructed MST")
        totalCost=0
        for u, v, cost in result:
            print(str(u)+"->"+str(v)+" with cost: "+str(cost))
            totalCost+=cost

        print("\nThe total cost is: ", totalCost)
        
    def PrimAlgorithm(self, graph):
        '''
        Given an undirected connected graph, constructs a minimum cost spanning tree using the Prim's algorithm.
        Input: graph - undirected connected graph
        Output: edges - a collection of edges, forming a minimum cost spanning tree
        '''
        q = []
        prev = {}
        dist = {}
        edges = []
        s = 0
        vertices = [s]
        for x in graph.getN(s):
            dist[x] = graph.getCost(x,s)
            prev[x] = s
            heappush(q, (dist[x],x))
        while len(q)!=0 and len(vertices) != graph.getVertices():
            x = heappop(q)
            if x[1] not in vertices:
                edges.append((x[1],prev[x[1]]))
                vertices.append(x[1])
                for y in graph.getN(x[1]):
                    if y not in vertices:
                        if y not in dist.keys() or graph.getCost(x[1],y) < dist[y]:
                            dist[y] = graph.getCost(x[1],y)
                            heappush(q,(dist[y],y))
                            prev[y]=x[1]
        return edges