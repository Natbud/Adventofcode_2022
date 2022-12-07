thefilepath = "04_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

found_lines = 0 

for line in file_list:   
  
    # This finds the lines with NO overlaps (the logic to do this was in my head clearly so I just did it this way)
    if int(line.split("-", 1)[0]) > int(line.split("-", 2)[2]) or int(line.split(",")[1].split("-", 2)[0]) > int(line.split("-", 1)[1].split(",")[0]):
        #print("There is no overlap:", line)
        found_lines += 1

#Now find the number of all the other lines which must have overlaps:
print("No of lines with overlaps:",len(file_list)-found_lines)    
