# coding: utf-8
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
import random
import numpy

# This Code is Based Heavily on The Following Sources:
# Article: http://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking
# Original Ruby Version: https://gist.github.com/jamis/755866
# https://en.wikipedia.org/wiki/Maze_generation_algorithm
# https://en.wikipedia.org/wiki/Maze_solving_algorithm


def build_maze(height=25, width=50):
  grid = build_empty_grid(height=height, width=width)
  grid = carve_passages_from(0, 0, grid)
  return grid
  
def display_console(grid):
  print_maze(grid=grid, height=len(grid), width=len(grid[0]))

def display_window(grid):
  binary_grid = map_maze(grid)
  display_map(binary_grid)

def display_solution(grid, **kwargs):
  solution = solve_maze(grid, **kwargs)

  if solution:
    display_map(solution)
  else:
    print("No Solution Found")

def solve_maze(grid, **kwargs):
  maze_binary_grid = map_maze(grid)

  endX = kwargs.get('endX', len(maze_binary_grid[0]) - 2)
  endY = kwargs.get('endY', 1)

  solution_found, _visited_cells, solution_binary_grid = _solve_maze(maze_binary_grid, endX, endY)

  if solution_found:
    return merge_solutions(solution_binary_grid, maze_binary_grid)
  else:
    None

def merge_solutions(solution_cells, binary_grid):
  solution = build_empty_list(height=len(solution_cells), width=len(solution_cells[0]), dval=0)

  solution = rebase_grid(solution_cells, solution, 1)
  solution = rebase_grid(binary_grid, solution, 2)

  return solution

def rebase_grid(solution_cells, solution, nvalue):
  for y, row in enumerate(solution_cells):
    for x, cell in enumerate(row):
      if cell:
        solution[y][x] = nvalue
  
  return solution

# --------------------------------------------------------------------
# 2. Set up constants to aid with describing the passage directions
# --------------------------------------------------------------------

N, S, E, W = 1, 2, 4, 8
DX         = { E: 1, W: -1, N:  0, S: 0 }
DY         = { E: 0, W:  0, N: -1, S: 1 }
OPPOSITE   = { E: W, W:  E, N:  S, S: N }

def carve_passages_from(cx, cy, grid):
  """
  --------------------------------------------------------------------
    3. The recursive-backtracking algorithm itself
  --------------------------------------------------------------------  
  """
  cardinal_directions = [N, S, E, W]
  directions = random.sample(cardinal_directions, len(cardinal_directions))

  for direction in directions:
    nx, ny = cx + DX[direction], cy + DY[direction]

    if ny in range(0, len(grid)) and nx in range(0, len(grid[ny])) and grid[ny][nx] == 0:
      grid[cy][cx] |= direction
      grid[ny][nx] |= OPPOSITE[direction]
      carve_passages_from(nx, ny, grid)
      
  return grid

def print_maze(grid, width, height):
  """
  --------------------------------------------------------------------
    4. A simple routine to emit the maze as ASCII
  --------------------------------------------------------------------  
  """
  print(" " + "_" * (width * 2 - 1))
  for y in range(height):
    print("|", end='')
    for x in range(width):
      print(" " if (grid[y][x] & S != 0) else "_", end='')
      if ( grid[y][x] & E != 0 ):
        print(" " if ((grid[y][x] | grid[y][x+1]) & S != 0) else "_", end='')
      else:
        print("|", end='')
    print()
  

def map_maze(grid):
  """
  --------------------------------------------------------------------
    X. Convert the maze to a two layered list of booleans.
  --------------------------------------------------------------------  
  """
  width = len(grid[0])
  height = len(grid)
  maze_map = []
  
  # Add top border
  maze_map.append([True] * (width * 2 + 1))
  for y in range(height):
    # Left side vertical bar.
    row  = []
    row2 = []
    
    row.append(  True )
    row2.append( True )
    
    for x in range(width):
      if not (grid[y][x] & S != 0):          
        # Underside Horizontal Bar.
        row.append( False )
        row2.append(True  )
      else:
        # Underside Clear
        row.append(  False )
        row2.append( False )

      if ( grid[y][x] & E != 0 ):
        if not ((grid[y][x] | grid[y][x+1]) & S != 0):
          # Underside Horizontal Bar.
          row.append( False )
          row2.append(True)
        else:
          row.append(  False )
          row2.append( True )
      else:
        # Right Side Vertical Bar.
        row. append(True)
        row2.append(True)

    maze_map.append(row )
    maze_map.append(row2)

  return maze_map

def display_map(maze):
    pyplot.figure(figsize=(10, 5))
    pyplot.imshow(maze, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()

def build_empty_grid(height, width, dtype=int):
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    grid = numpy.zeros(shape, dtype=dtype)

    return grid

def build_empty_list(height, width, dval=False):
    return [ [dval] * width for _ in range(height)]

def _solve_maze(maze, endX, endY, startX=1, startY=1):
    correctPath = build_empty_list(height= len(maze), width=len(maze[0]), dval=False)
    wasHere     = build_empty_list(height= len(maze), width=len(maze[0]), dval=False)

    return recursiveSolve(maze, startX, startY, endX, endY, wasHere, correctPath)

def recursiveSolve(maze, x, y, endX, endY, wasHere, correctPath, i=0):
    if x == endX and y == endY:  # Reached the end.
        return (True, wasHere, correctPath)

    if maze[y][x] == True or wasHere[y][x]:  # No solution found.
        return (False, wasHere, correctPath)
    
    wasHere[y][x] = True # If you are on a wall or already were here
    
    if x > 0:  # Checks if not on left edge
        (possible, wasHere, correctPath) = recursiveSolve(maze, x-1, y, endX, endY, wasHere, correctPath, i+1)
        # Recalls method one to the left
        if possible:
            correctPath[y][x] = True  # Sets that path value to true;
            return (True, wasHere, correctPath)

    width = len(maze[0])

    if (x < width - 1):   # Checks if not on right edge
        # Recalls method one to the right
        possible, wasHere, correctPath = recursiveSolve(maze, x+1, y, endX, endY, wasHere, correctPath, i+1)
        if possible:
            correctPath[y][x] = True
            return (True, wasHere, correctPath)

    if y > 0:  # Checks if not on top edge
        # Recalls method one up
        possible, wasHere, correctPath = recursiveSolve(maze, x, y-1, endX, endY, wasHere, correctPath, i+1)
        if possible:
            correctPath[y][x] = True
            return (True, wasHere, correctPath)
        
    height = len(maze)

    if (y < height - 1):   # Checks if not on bottom edge
        # Recalls method one down
        possible, wasHere, correctPath = recursiveSolve(maze, x, y+1, endX, endY, wasHere, correctPath, i+1)
        if possible:
            correctPath[y][x] = True
            return (True, wasHere, correctPath)


    return (False, wasHere, correctPath)