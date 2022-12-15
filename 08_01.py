import numpy as np

thefilepath = "08_01_Test_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

    print(file_list)

# Get the size of file_list to help with creating numpy array of same size.
# rows:
file_list_row_len = (len(file_list))
print("file_list rows:", file_list_row_len)
# columns:
file_list_col_len = (len(file_list[0]))
print("file_list cols:", file_list_col_len)

# Create a numpy array (for original given grid values) of same size as file_list and add all zeroes:
np_grid = np.zeros((file_list_row_len,file_list_col_len))

# Also create a numpy array for storing visible identifier (as a '1')
np_visible_grid = np.zeros((file_list_row_len,file_list_col_len))

# read in all the values from file_list into np_grid array
for r, row in enumerate(file_list):
    for d, digit in enumerate(row):
        np_grid[r][d] = digit

print("np_grid:\n", np_grid)

for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):
        #print(digit)
        #check if digit is on the edges and therefore visible:        
        #         
        if r == 0 or d == 0 or r == file_list_row_len-1 or d == file_list_col_len-1:
            np_visible_grid[r][d] = 1     # IS VISIBLE!

for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):

        # Check if larger than rest of digits in every row / column on each of 4 sides.
        # Check isn't on an edge in order to process:
        if not r == 0 or d == 0 or r == file_list_row_len-1 or d == file_list_col_len-1:
            #Then continue processing:
            




print("\nnp_visible_grid:\n", np_visible_grid)