import numpy as np
from solver import Solver
import math

PATH = '.'
GOAL = 'G'
START = 'M'
CANS = 'J'
WALL = 'X'


def get_map():
    with open ("2019_map.txt", "r") as myfile:
        data=myfile.readlines()

    # create map as Numpy array
    maps = np.array(list(data[1]))
    for i in range(len(data)-3):
        add = np.array(list(data[i+2]))
        maps = np.vstack((maps, add))

    return maps


def children(pos):
    children = []
    (x,y) = pos
    if (maps[x-1,y] != WALL):
        children.append((x-1,y))
    if (maps[x,y-1] != WALL):
        children.append((x,y-1))
    if (maps[x+1,y] != WALL):
        children.append((x+1,y))
    if (maps[x,y+1] != WALL):
        children.append((x,y+1))
    return children

def heuristic(child, GoalPos):
    dist = math.sqrt(pow(child[0]-GoalPos[0],2)+pow(child[1]-GoalPos[1],2))
    return dist

def DFS(maps):
    # loop through map and find initial position
    startPosition = np.where(maps == START)
    GoalPos = (1,10)
    OpenSet = []
    ClosedSet = []

    OpenSet.append(startPosition)

    for i in range(10):
        Node = OpenSet.pop(0)
        distGoal = []
        if (Node == GoalPos):
            return ClosedSet
        else:      
            children_nodes = children(Node)
            ClosedSet.append(Node)
            for i in children_nodes:
                if i in ClosedSet:
                    children_nodes.remove(i)
            for i in range(len(children_nodes)):
                dist = heuristic(children_nodes[i], GoalPos)
                distGoal.append(dist)
            index = distGoal.index(min(distGoal))
            OpenSet.insert(0,children_nodes[index])

maps = get_map()
mål = (1,10)

path = []

nodes = DFS(maps)
for i in range(len(nodes)-1):
    pos = nodes[i]
    newpos = nodes[i+1]
    if(pos[0] > newpos[0]):
        path.append('f')
    if(pos[0] < newpos[0]):
        path.append('b')
    if(pos[1] > newpos[1]):
        path.append('l')
    if(pos[1] < newpos[1]):
        path.append('r')

print(path)
#Sokoban.DFS(maps)



print("Hej")