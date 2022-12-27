import numpy as np

thefilepath = "08_01_Test_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

    #print(file_list)


def exit_strategy():
        
    count = np.count_nonzero(np_visible_grid == 1)

    #print("Total visible trees:,", count)

    #print("\nnp_visible_grid:\n", np_visible_grid)

    #print("\nnp_grid:\n", np_grid)

    exit ()


# Get the size of file_list to help with creating numpy array of same size.
# rows:
file_list_row_len = (len(file_list))
#print("file_list rows:", file_list_row_len)
# columns:
file_list_col_len = (len(file_list[0]))
#print("file_list cols:", file_list_col_len)

# Create a numpy array (for original given grid values) of same size as file_list and add all zeroes:
np_grid = np.zeros((file_list_row_len,file_list_col_len))

# Also create a numpy array for storing visible identifier (as a '1')
np_visible_grid = np.zeros((file_list_row_len,file_list_col_len))

# read in all the values from file_list into np_grid array
for r, row in enumerate(file_list):
    for d, digit in enumerate(row):
        np_grid[r][d] = digit

#print("np_grid:\n", np_grid)

for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):
        ##print(digit)
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
            
            

            #print("d is:", d, " checking FROM LEFT")
            for i in range(1,d+1):
                #print("total number of checks is:", d)
                #print("LEFT CHECK: i is:",i)

                
                #Identify the last tree in the row:
                last_tree = len(range(1,d+1))
                #print("LEFT CHECK LAST TREE IS: ", last_tree)
                #print("current value of np_grid[r][d]:", np_grid[r][d])
                #print("current value of np_grid[r][d-i]:", np_grid[r][d-i])

                if np_grid[r][d-i] >= np_grid[r][d]:
                    #SET NOT VISIBLE:
                    #print("np_visible_grid location: ", r, d, " marked 2") 
                    np_visible_grid[r][d] = 2
                    
                    #If marked as INVISIBLE Then continue with further checks:
                    #print("d is:", d, " checking FROM RIGHT") #THIS IS NOT WORKING WHEN d = 3  is jumping straight to final continue..
                    for t in range(1,file_list_col_len - (d)):
                        #print("total number of checks is: [file_list_col_len - (d+1)]:", (file_list_col_len - (d+1)))
                        #print("RIGHT CHECK t equals:", t)

                        #Identify the last tree in the row:
                        last_tree = len(range(0,file_list_col_len - (d+1))) # returning one too few...range needs to start at 0 not 1 
                        #print("RIGHT CHECK LAST TREE IS: ", last_tree)
                        #print("current value of np_grid[r][d]:", np_grid[r][d])
                        #print("current value of np_grid[r][d+t]:", np_grid[r][d+t])
                        if np_grid[r][d+t] >= np_grid[r][d]:
                            #SET NOT VISIBLE:
                            np_visible_grid[r][d] = 2
                            #print("np_visible_grid location: ", r, d, " marked 2")
                            

                            #If marked as INVISIBLE Then continue with BOTTOM checks:
                            #print("d is:", d, " checking FROM BOTTOM")
                            for b in range(1,file_list_row_len - (r)):
                                #print("total number of checks is [file_list_row_len - (r+1)]:", (file_list_row_len - (r+1)))
                                #print("crrent check number (b):", b)

                                #Identify the last tree in the row:
                                last_tree = len(range(0,file_list_row_len - (r+1))) # reduced this one to zero
                                #print("BOTTOM CHECK LAST TREE IS: ", last_tree)
                                #print("current value of np_grid[r][d]:", np_grid[r][d])
                                #print("current value of np_grid[r+b][d]:", np_grid[r+b][d])

                                if np_grid[r+b][d] >= np_grid[r][d]:
                                    #SET NOT VISIBLE:
                                    np_visible_grid[r][d] = 2
                                    #print("np_visible_grid location: ", r, d, " marked 2")
                                    #break  - remove this break if adding another check here.....
                                    
                                    # #If marked as INVISIBLE Then continue with TOP checks:
                                    #print("d is:", d, " checking FROM TOP")
                                    for h in range(1,r+1): # added +r to r to make last check happen....
                                        #print("total number of checks (r) is:", (r))
                                        #print("current check number (h):", h)

                                        #Identify the last tree in the row:
                                        last_tree = len(range(0,r))
                                        #print("TOP CHECK LAST TREE IS: ", last_tree)
                                        #print("current value of np_grid[r][d]:", np_grid[r][d])
                                        #print("current value of np_grid[r-h][d]:", np_grid[r-h][d])

                                        if np_grid[r-h][d] >= np_grid[r][d]:
                                            #SET NOT VISIBLE:
                                            np_visible_grid[r][d] = 2
                                            #print("np_visible_grid location: ", r, d, " marked 2")
                                            break  #no more checks to do so leave this break in......
                               
                                        else:
                                            #TOP CHECK mark as 1 and BREAK/CONTINUE to next 'd'
                                            if h == last_tree:
                                                np_visible_grid[r][d] = 1
                                                #print("np_visible_grid location: ", r, d, " marked 1 - last check done break and continue with next d") 
                                                break
                                            else:
                                                #print("np_visible_grid location: ", r, d, " marked 1 - not last check yet - continue with next check")
                                                np_visible_grid[r][d] = 1
                                                continue

                                    #TOP CHECK needs a 2nd 'break' at the same indent level as the RIGHT CHECK 'break' which then
                                    # sends to the Continue which instigates the next d.        
                                    break  

                                else:
                                    #BOTTOM CHECK mark as 1 and BREAK/CONTINUE to next 'd'
                                    if b == last_tree: 
                                        np_visible_grid[r][d] = 1
                                        #print("np_visible_grid location: ", r, d, " marked 1 - last check done break and continue with next d")
                                        break
                                    else:
                                        #print("np_visible_grid location: ", r, d, " marked 1 - not last check yet - continue with next tree check")
                                        np_visible_grid[r][d] = 1
                                        continue

                            #BOTTOM CHECK needs a 2nd 'break' at the same indent level as the RIGHT CHECK 'break' which then
                            # sends to the Continue which instigates the next d.        
                            break  

                        else:
                            #RIGHT CHECK - Check if last tree in row then Mark as 1 and BREAK (go to next 'd')    
                            if t == last_tree:
                                np_visible_grid[r][d] = 1
                                #print("RC np_visible_grid location: ", r, d, " marked 1 - last check done break and continue with next d") 
                                break
                            else:
                                #print("RC np_visible_grid location: ", r, d, " marked 1 - not last check yet - continue with next tree check")
                                np_visible_grid[r][d] = 1
                                continue
                    #RIGHT CHECK needs a 2nd 'break' at the same indent level as the 1st LEFT CHECK 'break' which then
                    # sends to the Continue which instigates the next d.        
                    break  

                
                else:
                    #LEFT CHECK - Check if last tree in row then Mark as 1 and BREAK (go to next 'd')
                    if i == last_tree:
                        np_visible_grid[r][d] = 1
                        #print("np_visible_grid location: ", r, d, " marked 1 - last check done break and continue with next d") 
                        break
                    else:
                        #print("np_visible_grid location: ", r, d, " marked 1 - not last check yet - continue with next tree check")
                        np_visible_grid[r][d] = 1
                        continue

                        

                
            #LEFT CHECK Continue with next 'd'
            #print("final continue reached - going to next 'd'....")
            continue
            
exit_strategy()