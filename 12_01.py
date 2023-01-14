import string
import numpy as np
import tabulate as tab
import ascii_lowercase

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

def get_height(s):
    if s in ascii_lowercase:
        return ascii_lowercase.index(s)
    if s == "S":
        return 0
    if s == "E":
        return 25

    # Determine Neighbours function
def get_neighbours(i,j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj

#MAIN CODE using PATHFINDING module





niceprint_grid(grid_2d)







"""
OLD CODE:


#Converting grid to height integers and add to a new grid.
for r, row in enumerate(grid_2d):
    for c, char in enumerate(row):
        if char == "S":
            char = "a"
        elif char == "E":
            char = "z" 
        grid_2d[r][c] = alphabet.index(char)+1
        #grid_2d[r][c] = 1


"""