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

print (tab.tabulate(crt_grid))


for a in file_list:
    global_cycle +=1

    #DRAW A PIXEL ON CRT:


    #END OF CYCLE COMMAND EXECUTION:
    if a[0] == "noop":
        continue
    if a[0] == "addx":
        global_cycle +=1 #additional cycle added for addx which takes 2 cycles to complete
        
        #DRAW A PIXEL ON CRT        

        register_value_x += int(a[1])



#print("total number of cycles in data: ", global_cycle)






