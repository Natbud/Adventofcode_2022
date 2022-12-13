thefilepath = "07_01_Test_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n

print(file_list)

#Just find all dirs and their containing file sizes first - deal with tree later

#directories file sizes dictionary:
dirs_file_sizes = {}
#Also setup a directory's 'children' dictionary:
dirs_children = {}

for line in file_list:
    if "cd" in line[0:4] and not "cd ." in line[0:6] and not "cd .." in line [0:7]:
        # don't need to do this for file size one as these are added in loop later..
        dirs_children[line.split(" ",2)[2]]=[]

prev_line = []
curdir = []
curdir_filesizes = 0

for n, line in enumerate(file_list):
    if "ls" in line[0:5] and "cd" in prev_line[0:5]:
        #store current dir name and total file sizes before these are cleared....
        print("curdir_filesize total:", curdir_filesizes, " for curdir: ",curdir)
        if not curdir == []:
            dirs_file_sizes[curdir]=curdir_filesizes

        print("line no:", n, " start directory ", prev_line.split(" ",2)[2])
        curdir = prev_line.split(" ",2)[2]
        curdir_filesizes = 0
    else:
        #Check for filesize record:
        if line[0].isdigit():
            curdir_filesizes += int(line.split(" ")[0])
            #print("size: ", line.split(" ")[0], " added")

        #Check also for 'child' directories:
        if "dir" in line[0:4]:
            print("child dir found: ", line.split(" ")[1])
            dirs_children[curdir].append(line.split(" ")[1])

        prev_line = line

# need this to print out the final curdir_filesizes amount as will be no more iterations:
print("curdir_filesize total:", curdir_filesizes, " for curdir: ",curdir)
#Add this info to dictionary:
dirs_file_sizes[curdir]=curdir_filesizes


#### THIS NEXT BIT NEEDS RECURSION!!! ####

#total_rec_size = 0
#Children dirs dictionary has dir names in:
#print("dirs_children dictionary: ", dirs_children)

for dir, child_dirs in dirs_children.items():
    print(dir, child_dirs)



def folder_dig(dir, child_dirs, total_rec_size, count):

    print("range(len(child_dirs) is equal to: ", len(child_dirs))
#Base Case Exit Strategy (when there are no child dirs to check):
    if count > (int(len(child_dirs)-1)):
        count = 0
        return(total_rec_size)
        #print("Recursion Exited, child_dirs for dir:", dir, "is empty")


    else:
        print("count:", count)
        #parent_size = (dirs_file_sizes[dir])
        #print("parent:", dir, " size: ", parent_size)
        #total_rec_size += parent_size
        #this is how to get values out of a list in a dictionary:
        for x in range(len(child_dirs)):

            child_found = ([child_dirs].__getitem__(0)[x])
            #print("child found: ", child_found)
            child_size = (dirs_file_sizes[child_found])
            #print("child ", child_found, " size:", child_size)
            total_rec_size += child_size

            print("current total_rec_size: ", total_rec_size)
            newcount = count + 1

            print("inside recursion current value of child_dirs:", child_dirs)
            folder_dig(child_found, child_dirs, total_rec_size, newcount) # specifies new 'dir' as most recent child found.




for dir, child_dirs in dirs_children.items():
    print("checking child_dirs:", child_dirs)
    print("recursion returns:", folder_dig(dir, child_dirs, 0,0))

#print("dir: ", dir, " and immediate children: ", child_dirs, " have total size: ", total_rec_size)
