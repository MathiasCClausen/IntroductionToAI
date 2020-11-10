import numpy as np
import math

class Solver:
    PATH = '.'
    GOAL = 'G'
    START = 'M'
    CANS = 'J'
    WALL = 'X'

    def __init__(self):
        self.sm = []

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

    def DFS(self):
        # loop through map and find initial position
        GoalPos = (1,2)
        OpenSet = []
        ClosedSet = []

        OpenSet.append(self.startPosition)

        while(OpenSet):
            Node = OpenSet.pop(0)
            distGoal = []
            if (Node == GoalPos):
                ClosedSet.append(Node)
                self.nextPath = ClosedSet
            else:      
                children_nodes = self.children(Node)
                ClosedSet.append(Node)
                for i in children_nodes:
                    if i in ClosedSet:
                        children_nodes.remove(i)
                for i in range(len(children_nodes)):
                    dist = self.heuristic(children_nodes[i], GoalPos)
                    distGoal.append(dist)
                index = distGoal.index(min(distGoal))
                OpenSet.insert(-1,children_nodes[index])   # if -1 then BFS


    def get_map(self):
        with open ("2019_map.txt", "r") as myfile:
            data=myfile.readlines()

        # create map as Numpy array
        maps = np.array(list(data[1]))
        for i in range(len(data)-3):
            add = np.array(list(data[i+2]))
            maps = np.vstack((maps, add))
        self.map = maps
        self.GOALS = np.where(self.map == self.GOAL)
        self.startPosition = np.where(self.map == self.START)
        self.currentPos = self.startPosition


    def heuristic(self, child, GoalPos):
        dist = math.sqrt(pow(child[0]-GoalPos[0],2)+pow(child[1]-GoalPos[1],2))
        return dist

    def get_path(self):
        path = []
        for i in range(len(self.nextPath)-1):
            pos = self.nextPath[i]
            newpos = self.nextPath[i+1]
            if(pos[0] > newpos[0]):
                path.append('f')
            if(pos[0] < newpos[0]):
                path.append('b')
            if(pos[1] > newpos[1]):
                path.append('l')
            if(pos[1] < newpos[1]):
                path.append('r')
        self.path = path
        return path

    def print_path(self):
        for i in range(len(self.nextPath)-1):
            pos = self.nextPath[i]
            self.map[pos] = 'o'
            print(self.map)

    

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