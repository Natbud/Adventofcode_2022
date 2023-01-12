import string
import numpy as np
import tabulate as tab

thefilepath = "12_01_Test_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n
    
#FUNCTIONS:

def niceprint_grid (grid):
    print (tab.tabulate(grid))

#MAIN CODE:

heightmap_grid = np.full((int(len(file_list)), int(len(file_list[0]))), ".")
alphabet = list(map(chr, range(97, 123)))

#Read file_list into heightmap_grid:
for m, map_row in enumerate(heightmap_grid):
    for h, height in enumerate(map_row):
        heightmap_grid[m][h] = file_list[m][h]

niceprint_grid(heightmap_grid)
