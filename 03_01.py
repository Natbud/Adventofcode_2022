thefilepath = "03_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

#Function to get first half and second half of a string and compare them, outputting any similar characters.
def half_string(string):
    length_string = len(string)
    first_length = round(length_string / 2)
    first_half = string[0:first_length]
    second_half = string[first_length:]
    same = set()  # using a set to remove duplicates later.
    
    #this bit compares all characters in first half with all characters in second half:
    for a in first_half:
        for b in second_half:

            if a == b:
                same.add(b)          

    return(same)

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print(len(priorities))

priorities_total = 0

#This calls the function:   
for line in file_list:
        #print(half_string(line))
        type_found = (half_string(line))
        print(list(type_found)[0])
        for i, char in enumerate(priorities):
            #print("char:",char)
            if char == (list(type_found)[0]):   # This is how to get the basic elements out of a set
                print("char", char, "found....number:", i + 1)
                priorities_total += (i+1)

print("final priorities total:", priorities_total)


        