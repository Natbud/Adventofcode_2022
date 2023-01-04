import numpy as np

thefilepath = "09_01_Test_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

#print(file_list)

x_head = 0
y_head = 0
x_tail = 0
y_tail = 0

tail_coordinates = []

change = 1


for m, move in enumerate(file_list):
    distance = int(move.split(' ')[1])

    #print("distance: ",distance)

    for c in range(1,distance+1):
        change = 1
        
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
        
        #ADJACENT AND DIAGONAL MOVE CHECKS:

        #check if head is adjacent to tail in N S E W directions:
        if (x_head == x_tail and y_head == y_tail+1) or (x_head == x_tail+1 and y_head == y_tail) or (x_head == x_tail and y_head == y_tail-1) or (x_head == x_tail-1 and y_head == y_tail):
            change = 0


        #check if head is diagonally adjacent to tail:
        if (x_head == x_tail+1 and y_head == y_tail+1) or (x_head == x_tail-1 and y_head == y_tail+1) or (x_head == x_tail-1 and y_head == y_tail-1) or (x_head == x_tail+1 and y_head == y_tail-1):
            change = 0
        
        
        #Now intercept requirement for a diagonal tail move:
        #TOP RIGHT DIAGONAL TAIL MOVE:
        if (x_head == x_tail+1 and y_head == y_tail+2) or (x_head == x_tail+2 and y_head == y_tail+1):
            x_tail +=1
            y_tail +=1

            tail_coordinates.append([x_tail,y_tail])
            continue
        
        #TOP LEFT DIAGONAL TAIL MOVE:
        if (x_head == x_tail-1 and y_head == y_tail+2) or (x_head == x_tail-2 and y_head == y_tail+1):
            x_tail -=1
            y_tail +=1

            tail_coordinates.append([x_tail,y_tail])
            continue
        
        #BOTTOM LEFT DIAGONAL TAIL MOVE:
        if (x_head == x_tail-2 and y_head == y_tail-1) or (x_head == x_tail-1 and y_head == y_tail-2):
            x_tail -=1
            y_tail -=1

            tail_coordinates.append([x_tail,y_tail])
            continue

        #BOTTOM RIGHT DIAGONAL TAIL MOVE:
        if (x_head == x_tail+1 and y_head == y_tail-2) or (x_head == x_tail+2 and y_head == y_tail-1):
            x_tail +=1
            y_tail -=1

            tail_coordinates.append([x_tail,y_tail])
            continue

        # STRAIGHT MOVES OF TAIL:
        if move[0] == "R":
            x_tail +=change
        if move[0] == "L":
            x_tail -=change
        if move[0] == "U":
            y_tail +=change
        if move[0] == "D":
            y_tail -=change  

        tail_coordinates.append([x_tail,y_tail])
        

def tail_report():
    #Remove duplicates from co-ordinates list:
    res = []
    for i in tail_coordinates:
        if i not in res:
            res.append(i)

    #print("tail_coordinates: ", tail_coordinates)
    #print("tail_co-or dedup: ", res)
    #print("number of co-ordinates visited by tail: ", len(res))
    print("number of co-ordinates visited by first knot: ", len(res))

tail_report()

#PART 2:

def knot_report():
    #Remove duplicates from co-ordinates list:
    res = []
    for i in knot_coordinates:
        if i not in res:
            res.append(i)

    #print("tail_coordinates: ", tail_coordinates)
    #print("tail_co-or dedup: ", res)
    #print("number of co-ordinates visited by tail: ", len(res))
    print("number of co-ordinates visited by knot: ", x, " equals: ", len(res))
    print("knot: ", x, "knot_coordinates contains: ", knot_coordinates)


# might need to do an initial 'overlap' check here before first 'move'

#reset x and y values:
x_head = 0
y_head = 0
x_tail = 0
y_tail = 0


knot_coordinates = []

change = 1

for x in range(2,10):

    for p, prev_coord in enumerate(tail_coordinates):
        change = 1

        #OVERLAP CHECK (before head has moved):
        if x_head == x_tail and y_head == y_tail:
                change = 0
        
        #HEAD MOVE:
        x_head = prev_coord[0]
        y_head = prev_coord[1]


        #OVERLAP CHECK (after head has moved):
        if x_head == x_tail and y_head == y_tail:
                change = 0
        
        #ADJACENT AND DIAGONAL MOVE CHECKS:

        #check if head is adjacent to tail in N S E W directions:
        if (x_head == x_tail and y_head == y_tail+1) or (x_head == x_tail+1 and y_head == y_tail) or (x_head == x_tail and y_head == y_tail-1) or (x_head == x_tail-1 and y_head == y_tail):
            change = 0


        #check if head is diagonally adjacent to tail:
        if (x_head == x_tail+1 and y_head == y_tail+1) or (x_head == x_tail-1 and y_head == y_tail+1) or (x_head == x_tail-1 and y_head == y_tail-1) or (x_head == x_tail+1 and y_head == y_tail-1):
            change = 0
        
        
        #Now intercept requirement for a diagonal tail move:
        #TOP RIGHT DIAGONAL TAIL MOVE:
        if (x_head == x_tail+1 and y_head == y_tail+2) or (x_head == x_tail+2 and y_head == y_tail+1):
            x_tail +=1
            y_tail +=1

            knot_coordinates.append([x_tail,y_tail])
            continue
        
        #TOP LEFT DIAGONAL TAIL MOVE:
        if (x_head == x_tail-1 and y_head == y_tail+2) or (x_head == x_tail-2 and y_head == y_tail+1):
            x_tail -=1
            y_tail +=1

            knot_coordinates.append([x_tail,y_tail])
            continue
        
        #BOTTOM LEFT DIAGONAL TAIL MOVE:
        if (x_head == x_tail-2 and y_head == y_tail-1) or (x_head == x_tail-1 and y_head == y_tail-2):
            x_tail -=1
            y_tail -=1

            knot_coordinates.append([x_tail,y_tail])
            continue

        #BOTTOM RIGHT DIAGONAL TAIL MOVE:
        if (x_head == x_tail+1 and y_head == y_tail-2) or (x_head == x_tail+2 and y_head == y_tail-1):
            x_tail +=1
            y_tail -=1

            knot_coordinates.append([x_tail,y_tail])
            continue

        #NOW ADD STRAIGHT MOVES FOR TAIL:
        #NORTH:
        if (x_head == x_tail and y_head == y_tail+2):
            y_tail +=change

        #EAST:
        if (x_head == x_tail+2 and y_head == y_tail):
            x_tail +=change
        
        #SOUTH:
        if (x_head == x_tail and y_head == y_tail-2):
            y_tail -=change 
            
        #WEST:
        if (x_head == x_tail-2 and y_head == y_tail):
            x_tail -=change

        knot_coordinates.append([x_tail,y_tail])

    knot_report()

    tail_coordinates = knot_coordinates
    
    knot_coordinates = []

    #reset x and y values:
    x_head = 0
    y_head = 0
    x_tail = 0
    y_tail = 0



