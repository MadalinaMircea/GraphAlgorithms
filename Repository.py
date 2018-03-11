'''
Created on Mar 21, 2017

@author: Madalina
'''
from Graph import Graph

class Repository:
    def __init__(self, filename = "graph1.txt"):
        self._loadFromFile(filename)
    
    def _loadFromFile(self, filename):
        '''
        Reads data from file
        :param filename:
        '''
        file = open(filename, 'r')
        text = file.readline()
        text = text.split()
        self.graph = Graph(int(text[0]))
        text = file.readline()
        while text != '':
            text = text.split()
            self.graph.addEdge(int(text[0]), int(text[1]))
            self.graph.addEdge(int(text[1]), int(text[0]))
            text = file.readline()
        file.close()
        
    def getNrVertices(self):
        return self.graph.getNrVertices()
    
    def getNrEdges(self, g):
        return g.getNrEdges()
    
    def isEdge(self, v1, v2):
        return self.graph.isEdge(v1, v2)
    
    def getDegree(self, v):
        return self.graph.getDegree(v)
    
    def getNeighbours(self, v):
        return self.graph.parseNeighbours(v)
    
    def showAll(self):
        return self.graph.parseAll()
    
    def addEdge(self, v1, v2, c):
        return self.graph.addEdge(v1, v2, c)