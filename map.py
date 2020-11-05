import numpy as np
from solver import Solver

Sokoban = Solver()
maps = Sokoban.get_map()

visited = np.zeros(Sokoban.map.shape, dtype=bool)


'''
#def depth_first_search__scan(sm, h):
    MAXNODES = 20000000
    openSet = [sm]
    ht = HashTable.HashTable()
    ht.checkAdd(sm)
    nodes = 0

    while len(openSet) > 0:
        currentState = openSet.pop()
        #currentState.printMap()

        nodes += 1
        if currentState.isSolution():
            return currentState # SOLUTION FOUND!!!

        if nodes % 1000 == 0:
            print nodes, " nodes checked"
            sys.stdout.flush()
        if nodes == MAXNODES:
            print "Limit of nodes reached: exiting without a solution."
            sys.exit(1)

        for x in currentState.children():
            # check if this has already been generated
            if ht.checkAdd(x):
                continue

            openSet.append(x)
    return None
'''

print("Hej")