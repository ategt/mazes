# coding: utf-8

import mazes
maze = mazes.build_maze(height=20, width=30)
mazes.display_solution(maze)
maze_binary_grid = mazes.map_maze(mazes)
maze_binary_grid = mazes.map_maze(maze)
endX = len(maze_binary_grid[0]) - 2
endX
len(maze[0])
import importlib
mazes = importlib.reload(mazes)
mazes.solve_maze(maze, endX=len(mazes[0])*2-2, endY=1)
mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=1)
solution = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=1)
from collections import Counter
Counter([cell for row in solution for cell in row])
solution = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=len(maze)*2-2)
len(solution)
Counter([cell for row in solution for cell in row])
mazes.display_map(solution)
maze = mazes.build_maze(height=20, width=30)

solutiona = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=1)
solutionb = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=len(maze)*2-2)
solutionc = mazes.solve_maze(maze, endX=1, endY=len(maze)*2-2)

dxa = Counter([cell for row in solutiona for cell in row])
dxb = Counter([cell for row in solutionb for cell in row])
dxc = Counter([cell for row in solutionc for cell in row])
dxa
dxa.get(1)
[dxa, dxb, dxc]
map(lambda ct: ct.get(1), [dxa, dxb, dxc])
list(map(lambda ct: ct.get(1), [dxa, dxb, dxc]))
dict(map(lambda ct: ct.get(1), [dxa, dxb, dxc]))
list(map(lambda ct: ct.get(1), [dxa, dxb, dxc]))
mazes.display_map(solutionb)
import json
with open('nice_maze.json','w') as handle:
    json.dump(maze, handle)
    
def cast_to_lists(narray):
    return [[int(cell) for cell in row] for row in narray]
with open('nice_maze.json','w') as handle:
    json.dump(cast_to_lists(maze), handle)
    
with open('nice_maze.json','r') as handle:
    mz3 = json.load(handle)
    
solve_br = lambda maze: mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=len(maze)*2-2)
s3 = solve_br(mz3)
mazes.display_map(s3)
maze = mazes.build_maze(height=20, width=30)

solutiona = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=1)
solutionb = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=len(maze)*2-2)
solutionc = mazes.solve_maze(maze, endX=1, endY=len(maze)*2-2)

dxa = Counter([cell for row in solutiona for cell in row])
dxb = Counter([cell for row in solutionb for cell in row])
dxc = Counter([cell for row in solutionc for cell in row])
list(map(lambda ct: ct.get(1), [dxa, dxb, dxc]))
mazes.display_map(dxc)
mazes.display_map(solutionc)
def save_maze(path, maze):
    with open(path,'w') as handle:
        json.dump(cast_to_lists(maze), handle)
    
save_maze('bottom_left_maze.json',maze)
def load_maze(path):
    with open(path,'r') as handle:
        return json.load(handle)
    
import os
os.path.exists('bill')
os.path.exists('bottom_left_maze.json')
def save_maze(path, maze):
    if os.path.exists(path):
        print("Path already exists.")
    else:
        with open(path,'w') as handle:
            json.dump(cast_to_lists(maze), handle)
    
save_maze('bottom_left_mazex.json',maze)
save_maze('bottom_left_mazex.json',maze)
def save_maze(path, maze):
    if os.path.exists(path):
        print("Path already exists - Nothing saved.")
    else:
        with open(path,'w') as handle:
            json.dump(cast_to_lists(maze), handle)
    
max([2,5,7])
from functools import reduce
best_sol = None
for i in range(20):
    maze = mazes.build_maze(height=20, width=30)

    optionals = {}
    
    solutiona = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=1)
    solutionb = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=len(maze)*2-2)
    solutionc = mazes.solve_maze(maze, endX=1, endY=len(maze)*2-2)
    
    dxa = Counter([cell for row in solutiona for cell in row])
    dxb = Counter([cell for row in solutionb for cell in row])
    dxc = Counter([cell for row in solutionc for cell in row])    

    complexity = max(list(map(lambda ct: ct.get(1), [dxa, dxb, dxc])))
    if complexity > 650:
        print(complexity)
        pairs = [{k: v} for k, v in zip(map(lambda ct: ct.get(1), [dxa, dxb, dxc]), [solutiona, solutionb, solutionc])]
        best_sol = reduce(lambda acc, item: {**item, **acc}, pairs, {})
        break
    
best_sol
best_sol.keys()
best_sol[682]
type(best_sol[682])
mazes.display_map(best_sol[682]))
mazes.display_map(best_sol[682])
from functools import reduce
best_sol = None
for i in range(20):
    maze = mazes.build_maze(height=20, width=30)

    optionals = {}
    
    solutiona = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=1)
    solutionb = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=len(maze)*2-2)
    solutionc = mazes.solve_maze(maze, endX=1, endY=len(maze)*2-2)
    
    dxa = Counter([cell for row in solutiona for cell in row])
    dxb = Counter([cell for row in solutionb for cell in row])
    dxc = Counter([cell for row in solutionc for cell in row])    

    complexity = max(list(map(lambda ct: ct.get(1), [dxa, dxb, dxc])))
    if complexity > 800:
        print(complexity)
        pairs = [{k: v} for k, v in zip(map(lambda ct: ct.get(1), [dxa, dxb, dxc]), [solutiona, solutionb, solutionc])]
        best_sol = reduce(lambda acc, item: {**item, **acc}, pairs, {})
        mazes.display_map(best_sol[complexity])
        break
    
save_maze('bottom_left_again.json', maze)
mx4 = load_maze('bottom_left_again.json')
mazes = importlib.reload(mazes)
mazes.display_solution(mx4)
mazes = importlib.reload(mazes)
mazes.display_solution(mx4)
mazes.display_solution(mx4, endX=1, endY=len(maze)*2-2)
from functools import reduce

def generate_maze(threshold=800, passes=20):
  best_sol = None
  for i in range(passes):
    maze = mazes.build_maze(height=20, width=30)

    optionals = {}
    
    solutiona = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=1)
    solutionb = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=len(maze)*2-2)
    solutionc = mazes.solve_maze(maze, endX=1, endY=len(maze)*2-2)
    
    dxa = Counter([cell for row in solutiona for cell in row])
    dxb = Counter([cell for row in solutionb for cell in row])
    dxc = Counter([cell for row in solutionc for cell in row])    

    complexity = max(list(map(lambda ct: ct.get(1), [dxa, dxb, dxc])))
    if complexity > threshold:
        print(complexity)
        pairs = [{k: v} for k, v in zip(map(lambda ct: ct.get(1), [dxa, dxb, dxc]), [solutiona, solutionb, solutionc])]
        best_sol = reduce(lambda acc, item: {**item, **acc}, pairs, {})
        mazes.display_map(best_sol[complexity])
        return maze
        break
    
maze = generate_maze()
maze = generate_maze()
from functools import reduce

def generate_maze(threshold=800, passes=20):
  best_sol = None
  maze = None
  for i in range(passes):
    maze = mazes.build_maze(height=20, width=30)

    optionals = {}
    
    solutiona = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=1)
    solutionb = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=len(maze)*2-2)
    solutionc = mazes.solve_maze(maze, endX=1, endY=len(maze)*2-2)
    
    dxa = Counter([cell for row in solutiona for cell in row])
    dxb = Counter([cell for row in solutionb for cell in row])
    dxc = Counter([cell for row in solutionc for cell in row])    

    complexity = max(list(map(lambda ct: ct.get(1), [dxa, dxb, dxc])))
    if complexity > threshold:
        print(complexity)
        pairs = [{k: v} for k, v in zip(map(lambda ct: ct.get(1), [dxa, dxb, dxc]), [solutiona, solutionb, solutionc])]
        best_sol = reduce(lambda acc, item: {**item, **acc}, pairs, {})
        mazes.display_map(best_sol[complexity])
        return maze
        
 print("Passes exceeded.")
from functools import reduce

def generate_maze(threshold=800, passes=20):
  best_sol = None
  maze = None
  for i in range(passes):
    maze = mazes.build_maze(height=20, width=30)

    optionals = {}
    
    solutiona = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=1)
    solutionb = mazes.solve_maze(maze, endX=len(maze[0])*2-2, endY=len(maze)*2-2)
    solutionc = mazes.solve_maze(maze, endX=1, endY=len(maze)*2-2)
    
    dxa = Counter([cell for row in solutiona for cell in row])
    dxb = Counter([cell for row in solutionb for cell in row])
    dxc = Counter([cell for row in solutionc for cell in row])    

    complexity = max(list(map(lambda ct: ct.get(1), [dxa, dxb, dxc])))
    if complexity > threshold:
        print(complexity)
        pairs = [{k: v} for k, v in zip(map(lambda ct: ct.get(1), [dxa, dxb, dxc]), [solutiona, solutionb, solutionc])]
        best_sol = reduce(lambda acc, item: {**item, **acc}, pairs, {})
        mazes.display_map(best_sol[complexity])
        return maze
        
  print("Passes exceeded.")
  
maze = generate_maze()
save_maze('bottom_right.json', maze)
maze = generate_maze()
maze = generate_maze()
maze = generate_maze(passes=50)
maze = generate_maze(passes=50)
maze = generate_maze(passes=50)
maze = generate_maze(passes=50)
get_ipython().run_line_magic('save', 'more_mazes 0-79')
