import numpy as np
import tabulate as tab
from string import ascii_lowercase
from heapq import heappop, heappush


thefilepath = "12_01_Test_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n
    
    grid_2d = [list(str(line)) for line in file_list] #create a list of separate items from a string
    
    n = len(grid_2d)
    m = len(grid_2d[0])

#set start and end points in grid
for i in range(n):
    for j in range(m):
        char = grid_2d[i][j]
        if char == "S":
            start = i, j
        if char == "E":
            end = i, j

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

        #check neighbour isn't outside bounds of grid:
        if not (0 <= ii < n and 0 <= jj < m):  
            continue

        # Check to see if we can move to this spot or not:    
        if get_height(grid_2d[ii][jj]) <= get_height(grid_2d[i][j]) +1:
            # 'return' the checked co-ordidnate that can be moved to
            yield ii, jj

niceprint_grid(grid_2d)

# Dijkstra's algorithm
visited = [[False] * m for _ in range(n)]
heap = [(0, start[0], start[1])]

while True:
    steps, i, j = heappop(heap)

    if visited[i][j]:
        continue
    visited[i][j] = True

    if (i, j) == end:
        print(steps)
        break

    for ii, jj in get_neighbours(i, j):
        heappush(heap, (steps + 1, ii, jj))











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