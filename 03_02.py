# THIS ONE BUGGY - SOMETIMES GIVES CORRECT ANSWER SOMETIMES FINDS SAME CHARACTER TWICE...
thefilepath = "03_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

# same = set()
type_found = []
priorities_total = 0
#print(file_list)
priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=0
y=1
z=2

while True:
    try:

        for a in file_list[x]:
            for b in file_list[y]:
                for c in file_list[z]:
                    if a == b == c:
                        # print("same character found:", c)
                        type_found.append(c)    
                        type_found = list(min(type_found)) # Chris' hacky remove duplicates....nice!
                        print("type_found:", type_found)          
                                                                       
        for i, char in enumerate(priorities):
            if char == type_found[0]:
                #print("char", char, "found....number:", i + 1)
                priorities_total += (i+1)    

                # print(list(same)[0])

        #clear out / adjust variables for next run
        type_found = []

        x += 3
        y += 3
        z += 3

    except IndexError:

        break

# Simply converting the set back into a standard list:
#for r in same:
#    type_found.append(r)

#print("type_found variable:", type_found)


          
print("final priorities total:", priorities_total)
