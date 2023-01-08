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

int_count = 0
for line in spacesplit_list:
    for word in line:
        if word.isdigit():
            int_count +=1

print("file_list digit count:", int_count)



monkey_item_grid = np.full((100,int(len(paragraphs))), "[]")

niceprint_grid(monkey_item_grid)


#monkey_item_grid = np.



