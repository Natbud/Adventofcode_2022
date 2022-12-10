thefilepath = "06_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.read()
    
print("file_list:", file_list)

start=0
end=14
    
for i, char in enumerate(file_list):
    test14 = str(file_list[start:end])
    print("test14:", test14)
    if len(set(test14)) == len(test14):
        print("there are no duplicates")
        print("Position of marker:", i+14)
        break
    else:
        print("there are duplicates")
        
        
    
    start+=1
    end+=1



