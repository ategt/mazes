# coding: utf-8

from collections import Counter
from functools import reduce
import mazes
import json
import os

def _cast_to_lists(narray):
    return [[int(cell) for cell in row] for row in narray]

def load_maze(path):
    with open(path,'r') as handle:
        return json.load(handle)
    
def save_maze(path, maze):
    if os.path.exists(path):
        print("Path already exists - Nothing saved.")
    else:
        with open(path,'w') as handle:
            json.dump(_cast_to_lists(maze), handle)

def display_maze(maze, in_console = False):
    if in_console:
        mazes.display_window(maze)
    else:
        mazes.display_console(maze)

def generate_maze(threshold=800, passes=20):
    """ 
        Each maze is assigned a complexity score, based on how much distance the solution covers.  Mazes with low complexity tend to have short, obvious solutions, with very elaborate dead ends.  Mazes with high complexity scores tend to have obvious solutions, with very few dead ends.  My ideal maze complexity score seems to be a maze that uses about 80% of the available pathways, making distinguishing between productive and unproductive pathways difficult, without wasting too much space within the maze on unproductive pathways.  Percentage of maze used will vary depending mostly on size of the maze, making the complexity score non-scalable.

        'generate_maze' will regenerate mazes until a maze with the desired complexity score is achieved, or the number of passes is exceeded.

        Threshold is the minimum complexity score.
        Passes is the maximum number of times that the maze can be regenerated.
    """
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