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
        # Check is on an edge and if so 'continue' / skip:
        if r == 0 or d == 0 or r == file_list_row_len-1 or d == file_list_col_len-1:
            continue
        else:
            #Then continue processing if not an edge digit:
            #Check if value is greater tha ll values on left of it THIS WAS TRICKY TO FIGURE OUT!:
            print("d is:", d, " checking starting")
            for i in range(1,d+1):
                #print("d minus i is:", d-i)
                if np_grid[r][d-i] >= np_grid[r][d]:
                    #SET NOT VISIBLE:
                    np_visible_grid[r][d] = 0
                    break
                else:
                    np_visible_grid[r][d] = 1

            
            #Now same for all values to the RIGHT



            




print("\nnp_visible_grid:\n", np_visible_grid)