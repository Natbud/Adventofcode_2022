thefilepath = "04_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

print(file_list)

found_lines = 0 

for line in file_list:
    
    
    if line.split("-", 1)[0] <= line.split(",")[1].split("-", 2)[0] and line.split("-", 1)[1].split(",")[0] >= line.split("-", 2)[2]:
        print("Left digits fully contain right digits:", line)
        found_lines += 1
    if line.split("-", 1)[0] >= line.split(",")[1].split("-", 2)[0] and line.split("-", 1)[1].split(",")[0] <= line.split("-", 2)[2]:
        print("Right digits fully contain Left digits:", line)
        found_lines += 1  

# Remove duplicates and print foundlines:    
print("total encapsulations found:", found_lines)

# NOT WORKING VALUE IS TOO HIGH!!!  

    #TESTING THE LINE SPLITS (WORKS FOR MULTIPLE DIGIT NUMBERS):
    #print("first digits:",line.split("-", 1)[0])
    #print("second digits:", line.split("-", 1)[1].split(",")[0])
    #print("third digits:", line.split(",")[1].split("-", 2)[0])
    #print("fourth digits:", line.split("-", 2)[2])