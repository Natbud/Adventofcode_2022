import numpy as np

thefilepath = "09_01_Test_Data_Nath.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

print(file_list)

x_head = 0
y_head = 0
x_tail = 0
y_tail = 0

tail_coordinates = []

change = 1

for m, move in enumerate(file_list):
    distance = int(move.split(' ')[1])

    print("distance: ",distance)

    for c in range(1,distance+1):
        #check if overlapping before any moves happen:
        if x_head == x_tail and y_head == y_tail:
            change = 0
        
        #Move head
        if move[0] == "R":
            x_head +=1
        if move[0] == "L":
            x_head -=1
        if move[0] == "U":
            y_head +=1
        if move[0] == "D":
            y_head -=1    
        
        #check if overlapping again after head has moved:
        if x_head == x_tail and y_head == y_tail:
            change = 0
        
        # Now Move Tail:
        if move[0] == "R":
            x_tail +=change
        if move[0] == "L":
            x_tail -=change
        if move[0] == "U":
            y_tail +=change
        if move[0] == "D":
            y_tail -=change  

        tail_coordinates.append([x_tail,y_tail])
        change = 1

#Remove duplicates from co-ordinates list:
res = []
for i in tail_coordinates:
    if i not in res:
        res.append(i)

print("tail_coordinates: ", tail_coordinates)
print("tail_co-or dedup: ", res)
exit()