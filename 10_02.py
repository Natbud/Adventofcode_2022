import numpy as np
import tabulate as tab

thefilepath = "10_01_Test_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n
    file_list = [line.split(' ') for line in file_list] #split at space character

#print(file_list)

global_cycle = 0
register_value_x = 1
crt_grid = np.full((6, 40), ".")
crt_pos = 0  # NEED TO NOT USE THIS FOR PRINTING - NEED ANOTHER VALUE THAT RESETS TO ZERO EACH LINE
print_row = 0

def niceprint_grid ():
    print (tab.tabulate(crt_grid))

def exit_drawgrid():
    niceprint_grid()
    exit()

    
for a in file_list:

    if crt_pos <40:
        print_row = 0
    if crt_pos > 39 and crt_pos < 80:
        print_row = 1
    if crt_pos > 79 and crt_pos < 120:
        print_row = 2
    if crt_pos > 119 and crt_pos < 160:
        print_row = 3        
    if crt_pos > 159 and crt_pos < 200:
        print_row = 4
    if crt_pos > 199 and crt_pos < 240:
        print_row = 5

    global_cycle +=1

    #DRAW A PIXEL ON CRT:
    crt_grid[print_row][crt_pos] = "#"

    #END OF CYCLE COMMAND EXECUTION:
    if a[0] == "noop":
        crt_pos +=1
        continue
    if a[0] == "addx":
        global_cycle +=1 #additional cycle added for addx which takes 2 cycles to complete
        crt_pos +=1 # NEEDS TO HAPPEN BEFORE DRAWING HAPPENS.

        #DRAW A PIXEL ON CRT     
        crt_grid[print_row][crt_pos] = "#"

        #End of Cycle Commands:
        register_value_x += int(a[1])

    if crt_pos == 47:
        exit_drawgrid()
        


niceprint_grid()
#print("total number of cycles in data: ", global_cycle)






#SPARE BAD CODE:

"""

    if print_row == 0:
        p = 0
        q = 39
    if print_row == 1:
        p = 40
        q = 79
    if print_row == 2:
        p = 80
        q = 119
    if print_row == 3:
        p = 120
        q = 159
    if print_row == 4:
        p = 160
        q = 199
    if print_row == 5:
        p = 200
        q = 239 

"""