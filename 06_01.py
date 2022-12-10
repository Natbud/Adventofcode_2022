thefilepath = "06_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.read()
    
print("file_list:", file_list)

start=0
end=4
    
for i, char in enumerate(file_list):
    test4 = str(file_list[start:end])
    print("test4:", test4)
    if len(set(test4)) == len(test4):
        print("there are no duplicates")
        print("Position of marker:", i+4)
        break
    else:
        print("there are duplicates")
        
        
    
    start+=1
    end+=1



