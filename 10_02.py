import numpy as np
import tabulate as tab
import os

thefilepath = "10_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n
    file_list = [line.split(' ') for line in file_list] #split at space character

#print(file_list)

global_cycle = 0
register_value_x = 1
crt_grid = np.full((6, 40), ".")
crt_pos = 0  # NEED TO NOT USE THIS FOR PRINTING - NEED ANOTHER VALUE THAT RESETS TO ZERO EACH LINE
print_pos = 0
print_row = 0
noop_no = 0
sprite_pos = 1

def niceprint_grid ():
    print (tab.tabulate(crt_grid))

def exit_drawgrid():
    niceprint_grid()
    exit()

def draw_pixel_hash():
    #DRAW A PIXEL ON CRT:
    crt_grid[print_row][print_pos] = "#"
    #os.system('cls')
    #niceprint_grid()

def draw_pixel_dot():
    #DRAW A PIXEL ON CRT:
    crt_grid[print_row][print_pos] = " "
    #os.system('cls')
    #niceprint_grid()

def newline_check():
    global print_row
    if print_pos == 40 or print_pos == 80 or print_pos == 120 or print_pos == 160 or print_pos == 200:
        print_row +=1

def printpos_reset():
    global crt_pos
    global print_pos
    if crt_pos == 40 or crt_pos == 80 or crt_pos == 120 or crt_pos == 160 or crt_pos == 200 or crt_pos == 240:
        print_pos = 0

    
for a in file_list:

    #OMIT ADVANCING PRINTPOS FIRST TIME ONLY
    if crt_pos > 0:
        print_pos +=1
        crt_pos +=1 

    global_cycle +=1

    newline_check()

    printpos_reset()

    if print_pos == sprite_pos or print_pos == sprite_pos-1 or print_pos == sprite_pos+1:
        draw_pixel_hash()
    else:
        draw_pixel_dot()


    #NOOP OR ADDX:
    if a[0] == "noop":
        continue
    if a[0] == "addx":
        #ADVANCE CYCLE:
        global_cycle +=1
        crt_pos +=1 
        print_pos +=1

        newline_check()

        printpos_reset()

        if print_pos == sprite_pos or print_pos == sprite_pos-1 or print_pos == sprite_pos+1:
            draw_pixel_hash()
        else:
            draw_pixel_dot()

        #UPDATE REGISTER:
        register_value_x += int(a[1])
        sprite_pos = register_value_x

niceprint_grid()
print("total number of cycles in data: ", global_cycle)