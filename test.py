from solver import Solver

Sokoban = Solver()
maps = Sokoban.get_map()
Sokoban.DFS()
path = Sokoban.get_path()
print(path)