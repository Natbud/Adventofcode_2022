import numpy as np
import tabulate as tab


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
monkey_item_grid = np.full((int(len(paragraphs)),item_count), "  ")

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
        
        #now get Test divisor:
        if line[0] == "Test:":
            divisible = line[len(line) -1]
            divisibles.append(divisible)
        
        # get if true throw:
        if line[0] == "If true:":
            true_throw = line[len(line) -1]
            true_throws.append(true_throw)

        # get if false throw:
        if line[0] == "If false:":
            false_throw = line[len(line) -1]
            false_throws.append(false_throw)          


#Display collected data so far:
print("operators: ", operators)
print("divisibles: ", divisibles)
print("true throws: ", true_throws)
print("false throws: ", false_throws)
niceprint_grid(monkey_item_grid)


#Now start main procedure:
#for monkey, items in enumerate(monkey_item_grid):