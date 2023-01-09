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

#count all 'items' in input file
item_count = 0
for line in spacesplit_list:
    if line[0] == "Starting":
        for word in line:
            word = word.strip(',')
            if word.isdigit():
                item_count +=1

#print("file_list total item count:", item_count)
monkey_item_grid = np.full((int(len(paragraphs)),item_count), ".")

# THIS BIT NOT WORKING!! NEED TO STRIP WHITESPACE FROM FONT OF PARAGRAPH LINES
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
                    monkey_item_grid[p][add_count] = int(word)
                    add_count +=1

niceprint_grid(monkey_item_grid)






