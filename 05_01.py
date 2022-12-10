thefilepath = "05_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    crate_list = [line.strip("\n") for line in file_list]
    crate_list = list(filter(None, crate_list))
    file_list = [line.strip() for line in file_list] #strips /n and whitespace

#print("stripped file_list", file_list)
#print("crate list:", crate_list)
stacks_quantity = 0

#find number of stacks:
for i, line in enumerate(file_list):
    #print("checking line:", line)
    if line[0] == '1':
        stacks_quantity = int(line[-1])
        #print("there are ", stacks_quantity, " stacks in this data")
        break

# Create correct no of stacks (just list objects):
stacks_dict = {}

for x in range (0,stacks_quantity):
    stacks_dict[str(x+1)] = []



#Add crate stacks to dictionary:
for line in (crate_list):
    if not line[1] == "1" and not line[0:4] == "move":
        #print("crate_list crates only:", line)
        
        
        chartoadd = 1
        left = 0
        right = 2
        for x in range (0,stacks_quantity):
            if not line[left:right] == "  ":
                stacks_dict[str(x+1)].append(line[chartoadd])
            chartoadd += 4
            left += 4
            right += 4

#print("Dict populated with crates:", stacks_dict)



#Now start moving crates:
number_to_move = 0

for line in (file_list):
    if not line == '':
        #print(line[0:4])
        if line[0:4] =="move":
            number_to_move = int(line.split(' ',5)[1])
            move_from = line.split(' ', 5)[3]
            move_to = line.split(' ', 5)[5]
            #print("how many", number_to_move, "from where:", move_from, "moved to:", move_to)

            for m in range(number_to_move):
                stacks_dict[move_to].insert(0, stacks_dict[move_from].pop(0))
                #print("stacks_dict update:", stacks_dict)
a="1"
#Report resulting top crates on each stack:



# Gets the first item in each 'value' from dict key : value pairs:
result = str([item[0] for item in stacks_dict.values()])


#Cleaning up the string remove nonsesne:               
result = result.strip('}{').replace('[', '').replace(']', '')   
result = result.replace(':','').replace('\'','').replace(', ','')
print("Result:", result)  

                


