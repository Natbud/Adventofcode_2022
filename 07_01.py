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
    if "cd" in line[0:4]:
        # don't need to do this for file size one as these are added in loop later..
        dirs_children[line[5]]=[]
       
prev_line = []
curdir = []
curdir_filesizes = 0

for n, line in enumerate(file_list):
    if "ls" in line[0:5] and "cd" in prev_line[0:5]:
        #store current dir name and total file sizes before these are cleared....
        print("curdir_filesize total:", curdir_filesizes, " for curdir: ",curdir)
        if not curdir == []:
            dirs_file_sizes[curdir]=curdir_filesizes
        
        print("line no:", n, " start directory ", prev_line[5])
        curdir = prev_line[5]
        curdir_filesizes = 0
    else:
        #Check for filesize record:
        if line[0].isdigit():
            curdir_filesizes += int(line.split(" ")[0])
            #print("size: ", line.split(' ')[0], " added")
        
        #Check also for 'child' directories:
        if "dir" in line[0:4]:
            print("child dir found: ", line[4])
          
        prev_line = line

# need this to print out the final curdir_filesizes amount as will be no more iterations:
print("curdir_filesize total:", curdir_filesizes, " for curdir: ",curdir)
#Add this info to dictionary:
dirs_file_sizes[curdir]=curdir_filesizes
        
#File size dictionary is now populated with all dirs and total size of any files within them:
print("dirs_file_sizes dictionary: ", dirs_file_sizes)

#Children dirs dictionary has dir names in:
print("dirs_children dictionary: ", dirs_children)


#Now find each direcotry's child directories:

        