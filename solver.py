import numpy as np

class Solver:
    PATH = '.'
    GOAL = 'G'
    START = 'M'
    CANS = 'J'
    WALL = 'X'

    def __init__(self):
        self.sm = []


    def DFS(self, maps, goals):
        # loop through map and find initial position
        startPosition = np.where(maps == 'M')
        self.player = startPosition
        OpenSet = []
        ClosedSet = []
        MAXNODES = 2000000
        OpenSet.append(startPosition)

        while(OpenSet):
            currentState = OpenSet.pop()
            if (currentState == (2,1)):
                return "YES"
            else:
                if(maps[currentState[0]-1,currentState[1]] == 'X'):
                    OpenSet.append(maps[currentState[0]-1,currentState[1]])


    def get_map(self):
        with open ("2019_map.txt", "r") as myfile:
            data=myfile.readlines()

        # create map as Numpy array
        maps = np.array(list(data[1]))
        for i in range(len(data)-3):
            add = np.array(list(data[i+2]))
            maps = np.vstack((maps, add))
        self.map = maps


    def get_locations(self, maps):
        goals = []
        initialPos = []
        for i in range(maps.shape[0]):
            for j in range(maps.shape[1]):
                if (maps[i,j] == 'G'):
                    goals.append((i,j))

    def isSolution(self, ClosedSet, goals):
        counter = 0
        for i in goals:
            for j in ClosedSet:
                if (i==j):
                    counter += 1
        if counter == 4:
            return True
        else: 
            return False

    def children(self, pos):
        children = []
        (x,y) = pos
        if (self.map[x-1,y] != self.WALL):
            children.append((x-1,y))
        if (self.map[x,y-1] != self.WALL):
            children.append((x,y-1))
        if (self.map[x+1,y] != self.WALL):
            children.append((x+1,y))
        if (self.map[x,y+1] != self.WALL):
            children.append((x,y+1))
        return children
    

    def BFS(self): 
  
        # Mark all the vertices as not visited 
        visited = np.zeros(self.map.shape, dtype=bool)
        startPosition = np.where(self.map == 'M')

        # Create a queue for BFS 
        OpenSet = []
        ClosedSet = []
        queue = [] 

        # Mark the start node as visited and put it in OpenSet 
        OpenSet.append(startPosition) 
        visited[startPosition] = True
  
        while OpenSet: 
  
            # Dequeue a vertex from queue and print it 
            s = OpenSet.pop(0) 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.map[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True