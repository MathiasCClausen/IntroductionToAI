from solver import Solver

Sokoban = Solver()
maps = Sokoban.get_map()
Sokoban.DFS()
Sokoban.BFS()
path = Sokoban.get_path()
