import numpy as np

thefilepath = "10_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n
    file_list = [line.split(' ') for line in file_list] #split at space character

#print(file_list)

global_cycle = 0
register_value_x = 1
signal_strength = 0
interesting_strengths = []

def interesting_check():
    if ((global_cycle-20) % 40) == 0 and not ((global_cycle-20) % 40) > 220:
        signal_strength = global_cycle * register_value_x
        #print("DURING global_cycle: ", global_cycle, " register_value_x: ", register_value_x, " signal strength: ", signal_strength)
        interesting_strengths.append(signal_strength)


for a in file_list:
    global_cycle +=1

    #DURING CYCLE CHECKS:
    interesting_check()

    #END OF CYCLE COMMAND EXECUTION:
    if a[0] == "noop":
        continue
    if a[0] == "addx":
        global_cycle +=1 #additional cycle added for addx which takes 2 cycles to complete
        
        #ANOTHER DURING CYCLE CHECK REQUIRED HERE:
        interesting_check()

        register_value_x += int(a[1])

#print("total number of cycles in data: ", global_cycle)
#print("Interesting Strengths: ", interesting_strengths)
print("Signal Strengths Sum: ", np.sum(interesting_strengths))





