import numpy as np
import tabulate as tab
import math


thefilepath = "11_01_Test_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    
with open(thefilepath) as f:
    paragraphs = f.read().split("\n\n")

def niceprint_grid (grid):
    print (tab.tabulate(grid))

spacesplit_list = [line.strip() for line in file_list] #strip /n
spacesplit_list = [line.split(' ') for line in spacesplit_list] #split at space character

operators = []
maths_signs = []
divisibles = []
true_throws = []
false_throws = []

#count all 'items' in input file
item_count = 0
for line in spacesplit_list:
    if line[0] == "Starting":
        for word in line:
            word = word.strip(',')
            if word.isdigit():
                item_count +=1

#print("file_list total item count:", item_count)
monkey_item_grid = np.full((int(len(paragraphs)),item_count), "  ", dtype='O')


#Add intial items to each monkey in grid
for p, paragraph in enumerate(paragraphs):
    spacesplit_paragraph = paragraph.split("\n")
    spacesplit_paragraph = [line.strip() for line in spacesplit_paragraph]
    spacesplit_paragraph = [line.split(' ') for line in spacesplit_paragraph]
    for line in spacesplit_paragraph:
        if line[0] == "Starting":
            add_count = 0
            for word in line:
                word = word.strip(',')
                if word.isdigit():
                    monkey_item_grid[p][add_count] = word
                    add_count +=1
        # now get 'operator' for current monkey/paragrraph:
        if line[0] == "Operation:":
            operator = line[len(line) -1]
            if operator.isdigit():
                #print("operation: ", operator, "for monkey: ", p)
                operators.append(operator)
            else:
                operators.append("old")

            maths_sign = line[len(line) -2]
            maths_signs.append(maths_sign)

        # now get the + or * modifier value from Operation line
        
        #now get Test divisor:
        if line[0] == "Test:":
            divisible = line[len(line) -1]
            divisibles.append(divisible)
        
        # get if true throw:
        if line[1] == "true:":
            true_throw = line[len(line) -1]
            true_throws.append(true_throw)

        # get if false throw:
        if line[1] == "false:":
            false_throw = line[len(line) -1]
            false_throws.append(false_throw)          


#Display collected data so far:
#print("operators: ", operators)
#print("divisibles: ", divisibles)
#print("true throws: ", true_throws)
#print("false throws: ", false_throws)
niceprint_grid(monkey_item_grid)




#Now start main procedure:
for monkey, items in enumerate(monkey_item_grid):
    temp_items = []
    for item in items:
        if not item == "  ":
            temp_items.append(item)
    print("temp items: ", temp_items)
    for temp_item in temp_items:
        #Find Destination Monkey for throw:
        #add clause for some that need addition not multiplication.
        if operators[monkey] == "old":
            if maths_signs[monkey] == "*":
                increased_worry = int(temp_item) * int(temp_item)
            else:
                increased_worry = int(temp_item) + int(temp_item)
        else:
            if maths_signs[monkey] == "*":
                increased_worry = int(temp_item) * int(operators[monkey])
            else:
                increased_worry = int(temp_item) + int(operators[monkey])

        div3_worry = math.floor(increased_worry/3)
        divided_test = div3_worry/int(divisibles[monkey])
        if divided_test == int(divided_test):
            destination_monkey = int(true_throws[monkey])
        else:
            destination_monkey = int(false_throws[monkey])
        print("\n\ndestination monkey: ",destination_monkey)
        
        #Throw the monkey:
        #Remove from current monkey:
        monkey_item_grid[monkey][0] = "  "
        monkey_item_grid[monkey] = np.roll(monkey_item_grid[monkey], -1)
        #Add to destination monkey:
        for d, dest_item in enumerate(monkey_item_grid[destination_monkey]):
            if dest_item == "  ":
                monkey_item_grid[destination_monkey][d] = div3_worry
                print("div3_worry value:", div3_worry)
                print("value at new destination: ", monkey_item_grid[destination_monkey][d])
                break
        
niceprint_grid(monkey_item_grid)

        