# coding: utf-8

from collections import Counter
from functools import reduce
import mazes
import json
import os

def _cast_to_lists(narray):
    return [[int(cell) for cell in row] for row in narray]

def _find_far_column(maze):
    return len(maze[0])*2-2

def _find_far_row(maze):
    return len(maze)*2-2

_corners = {"top right":    lambda maze: (_find_far_column(maze), 1),
            "bottom right": lambda maze: (_find_far_column(maze), _find_far_row(maze)),
            "bottom left":  lambda maze: (1, _find_far_row(maze))}

def _determine_complexity(solution):
    return Counter([cell for row in solution for cell in row]).get(1)

def load_maze(path):
    with open(path,'r') as handle:
        return json.load(handle)
    
def save_maze(path, maze):
    if os.path.exists(path):
        print("Path already exists - Nothing saved.")
    else:
        with open(path,'w') as handle:
            json.dump(_cast_to_lists(maze), handle)

def display_maze(maze, in_console = False, solution = None):
    if in_console:
        mazes.display_console(maze)
    else:
        if solution:
            mazes.display_map(solution)
        else:
            mazes.display_window(maze)

def generate_maze(threshold=800, passes=20):
    """ 
        Each maze is assigned a complexity score, based on how much distance the solution covers.  Mazes with low complexity tend to have short, obvious solutions, with very elaborate dead ends.  Mazes with high complexity scores tend to have obvious solutions, with very few dead ends.  My ideal maze complexity score seems to be a maze that uses about 80% of the available pathways, making distinguishing between productive and unproductive pathways difficult, without wasting too much space within the maze on unproductive pathways.  Percentage of maze used will vary depending mostly on size of the maze, making the complexity score non-scalable.

        'generate_maze' will regenerate mazes until a maze with the desired complexity score is achieved, or the number of passes is exceeded.

        Threshold is the minimum complexity score.
        Passes is the maximum number of times that the maze can be regenerated.

        returns a (maze, solution) tuple
    """
    best_sol = None
    maze = None
    for i in range(passes):
        maze = mazes.build_maze(height=20, width=30)

        goal_name_location_tuples_list = [ (key, value(maze) ) for key, value in _corners.items()]

        names_solutions_list = [ (name, mazes.solve_maze(maze, endX=location[0], endY=location[1])) for name, location in goal_name_location_tuples_list]
        names_solutons_complexity_list = [ (name, solution, _determine_complexity(solution)) for name, solution in names_solutions_list ]

        best_goal, best_solution, highest_complexity = max(names_solutons_complexity_list, key=lambda item:item[2])

        if highest_complexity > threshold:
            print(f"Start in the top left corner and go to the {best_goal}.")
            print(f"Complexity Score: {highest_complexity}")
            return maze, best_solution
            
    print("Passes exceeded.")

def main():
    maze, solution = generate_maze(passes = 60)
    display_maze(maze)
    display_maze(maze, solution = solution)

if __name__ == '__main__':
    main()