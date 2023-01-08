import numpy as np
import tabulate as tab


thefilepath = "11_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    
with open(thefilepath) as f:
    paragraphs = f.read().split("\n\n")

def niceprint_grid (grid):
    print (tab.tabulate(grid))

spacesplit_list = [line.strip() for line in file_list] #strip /n
spacesplit_list = [line.split(' ') for line in spacesplit_list] #split at space character

item_count = 0
for line in spacesplit_list:
    if line[0] == "Starting":
        for word in line:
            word = word.strip(',')
            if word.isdigit():
                item_count +=1

print("file_list digit count:", item_count)

monkey_item_grid = np.full((int(len(paragraphs)),item_count), ".")

niceprint_grid(monkey_item_grid)


#monkey_item_grid = np.



