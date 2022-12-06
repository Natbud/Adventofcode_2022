# THIS ONE BUGGY - SOMETIMES GIVES CORRECT ANSWER SOMETIMES FINDS SAME CHARACTER TWICE...
thefilepath = "03_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

same = set()
type_found = []

print(file_list)

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
                        same.add(c)          

        # print(list(same)[0])

        



        x += 3
        y += 3
        z += 3

    except IndexError:

        break

#print("type_found variable:",type_found)
for r in same:
    type_found.append(r)

print("type_found variable:", type_found)

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print(len(priorities))

priorities_total = 0

for i, char in enumerate(priorities):
    for j in type_found:
        if char == j: 
            print("char", char, "found....number:", i + 1)
            priorities_total += (i+1)
          
print("final priorities total:", priorities_total)
