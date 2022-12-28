import numpy as np

thefilepath = "08_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

def exit_strategy():       
    count = np.count_nonzero(np_visible_grid == 1)
    print("Total visible trees:,", count)
    

file_list_row_len = (len(file_list))
file_list_col_len = (len(file_list[0]))
np_grid = np.zeros((file_list_row_len,file_list_col_len))
np_visible_grid = np.zeros((file_list_row_len,file_list_col_len))


for r, row in enumerate(file_list):
    for d, digit in enumerate(row):
        np_grid[r][d] = digit

np_visibility_grid_left = np.zeros((file_list_row_len,file_list_col_len))
np_visibility_grid_right = np.zeros((file_list_row_len,file_list_col_len))
np_visibility_grid_bottom = np.zeros((file_list_row_len,file_list_col_len))
np_visibility_grid_top = np.zeros((file_list_row_len,file_list_col_len))

ltree_visibility = 0
rtree_visibility = 0
btree_visibility = 0
ttree_visibility = 0

print("\n",np_grid,"\n")

for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):

        ltree_visibility = 0

        #LEFT CHECK
        if d == 0:
                ltree_visibility = 0
                #print("left tree visibility for tree at pos:,",r,d," value:", np_grid[r][d], " is:", ltree_visibility )
                np_visibility_grid_left[r][d] = ltree_visibility
                continue
        for i in range(1,d+1):
            if np_grid[r][d-i] >= np_grid[r][d]:
                ltree_visibility += 1             
                break
            else:
                ltree_visibility += 1

        #print("left tree visibility for tree at pos:,",r,d," value:", np_grid[r][d], " is:", ltree_visibility )
        np_visibility_grid_left[r][d] = ltree_visibility


for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):

        rtree_visibility = 0

        #RIGHT CHECK
        if d == file_list_col_len-1:
                rtree_visibility = 0
                #print("right tree visibility for tree at pos:,",r,d," value:", np_grid[r][d], " is:", rtree_visibility )
                np_visibility_grid_right[r][d] = rtree_visibility
                continue
        for t in range(1,file_list_col_len - (d)):
            if np_grid[r][d+t] >= np_grid[r][d]:
                rtree_visibility += 1
                break
            else:
                rtree_visibility += 1

        #print("right tree visibility for tree at pos:,",r,d," value:", np_grid[r][d], " is:", rtree_visibility )
        np_visibility_grid_right[r][d] = rtree_visibility

                    

for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):

        btree_visibility = 0

        #BOTTOM
        if r == file_list_row_len-1:
                btree_visibility = 0
                #print("bottom tree visibility for tree at pos:,",r,d," value:", np_grid[r][d], " is:", btree_visibility )
                np_visibility_grid_bottom[r][d] = btree_visibility
                continue
        for b in range(1,file_list_row_len - (r)):
            if np_grid[r+b][d] >= np_grid[r][d]:
                btree_visibility += 1
                break
            else:
                btree_visibility += 1

        #print("bottom tree visibility for tree at pos:,",r,d," value:", np_grid[r][d], " is:", btree_visibility )
        np_visibility_grid_bottom[r][d] = btree_visibility       



for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):

        ttree_visibility = 0

        #TOP
        if r == 0:
                ttree_visibility = 0
                #print("top tree visibility for tree at pos:,",r,d," value:", np_grid[r][d], " is:", ttree_visibility )
                np_visibility_grid_top[r][d] = ttree_visibility
                continue
        for h in range(1,r+1):
            if np_grid[r-h][d] >= np_grid[r][d]:
                ttree_visibility += 1
                break
            else:
                ttree_visibility += 1

        #print("top tree visibility for tree at pos:,",r,d," value:", np_grid[r][d], " is:", ttree_visibility )
        np_visibility_grid_top[r][d] = ttree_visibility

# Mutliply all scores together for each tree to get it's scenic score.abs(
np_scenic_scores = np.zeros((file_list_row_len,file_list_col_len))
#print("scenic scores grid empty: ", np_scenic_scores)

for r, row in enumerate(np_scenic_scores):
    for d, digit in enumerate(row):

        score = np_visibility_grid_left[r][d] * np_visibility_grid_right[r][d] * np_visibility_grid_bottom[r][d] * np_visibility_grid_top[r][d]

        np_scenic_scores[r][d] = score

print("scenic_scores final grid: ", np_scenic_scores)
print("highest scenic score: ", int(np_scenic_scores.max()))











     
