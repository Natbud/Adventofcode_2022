import numpy as np

thefilepath = "08_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

def exit_strategy():
        
    count = np.count_nonzero(np_visible_grid == 1)

    print("Total visible trees:,", count)

    exit ()

file_list_row_len = (len(file_list))
file_list_col_len = (len(file_list[0]))
np_grid = np.zeros((file_list_row_len,file_list_col_len))
np_visible_grid = np.zeros((file_list_row_len,file_list_col_len))

for r, row in enumerate(file_list):
    for d, digit in enumerate(row):
        np_grid[r][d] = digit

for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):   
        if r == 0 or d == 0 or r == file_list_row_len-1 or d == file_list_col_len-1:
            np_visible_grid[r][d] = 1     # IS VISIBLE!

for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):

        if r == 0 or d == 0 or r == file_list_row_len-1 or d == file_list_col_len-1:
            continue
        else:

            for i in range(1,d+1):

                last_tree = len(range(1,d+1))
                if np_grid[r][d-i] >= np_grid[r][d]:
                    np_visible_grid[r][d] = 2

                    for t in range(1,file_list_col_len - (d)):
                        last_tree = len(range(0,file_list_col_len - (d+1))) 
                        if np_grid[r][d+t] >= np_grid[r][d]:
                            np_visible_grid[r][d] = 2
                            for b in range(1,file_list_row_len - (r)):
                                last_tree = len(range(0,file_list_row_len - (r+1)))
                                if np_grid[r+b][d] >= np_grid[r][d]:
                                    np_visible_grid[r][d] = 2
                                    for h in range(1,r+1): 
                                        last_tree = len(range(0,r))
                                        if np_grid[r-h][d] >= np_grid[r][d]:
                                            np_visible_grid[r][d] = 2
                                            break                 
                                        else:
                                            if h == last_tree:
                                                np_visible_grid[r][d] = 1
                                                break
                                            else:
                                                np_visible_grid[r][d] = 1
                                                continue    
                                    break  
                                else:
                                    if b == last_tree: 
                                        np_visible_grid[r][d] = 1
                                        break
                                    else:
                                        np_visible_grid[r][d] = 1
                                        continue
                            break  
                        else:
                            if t == last_tree:
                                np_visible_grid[r][d] = 1
                                break
                            else:
                                np_visible_grid[r][d] = 1
                                continue
                    break  
                else:
                    if i == last_tree:
                        np_visible_grid[r][d] = 1
                        break
                    else:
                        np_visible_grid[r][d] = 1
                        continue
            continue      
exit_strategy()