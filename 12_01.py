import string
import numpy as np
import tabulate as tab
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

thefilepath = "12_01_Test_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n
    
    grid_2d = [list(str(line)) for line in file_list] #create a list of separate items from a string
    orig_grid = grid_2d

alphabet = list(map(chr, range(97, 123)))


#FUNCTIONS:
def niceprint_grid (grid):
    print (tab.tabulate(grid))

#MAIN CODE using PATHFINDING module

niceprint_grid(grid_2d)

#Converting grid to height integers.
for r, row in enumerate(grid_2d):
    for c, char in enumerate(row):
        if char == "S":
            char = "a"
        elif char == "E":
            char = "z" 
        #grid_2d[r][c] = alphabet.index(char)+1
        grid_2d[r][c] = 1
        
niceprint_grid(grid_2d)

#Create 'pathfinder' Grid
grid = Grid(matrix = grid_2d)

#Establish start and end points for path
start = grid.node(0,0)
end = grid.node(5,2)

#Create a 'finder' with a movement style:
finder = AStarFinder()

#Find a path:
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))




