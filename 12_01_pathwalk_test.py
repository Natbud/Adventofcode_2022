import string
import numpy as np
import tabulate as tab

thefilepath = "12_01_pathwalk_test.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list] #strip /n
    file_list = [line.split(' ') for line in file_list] #split at space  NOT NEED THIS IN MAIN PROGRAM!!

alphabet = list(map(chr, range(97, 123)))
grid_2d = [line for line in file_list]

#print("file_list: ", file_list)
#print("grid_2d: ", grid_2d)

#FUNCTIONS:

def niceprint_grid (grid):
    print (tab.tabulate(grid))

#MAIN CODE (Backtracking approach FROM https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/ ):
# THIS WORKS

# code
class Solution:
     
    def __init__(self):
        self.mapping = {}
     
    def printAllPaths(self, M, m, n):
        if not self.mapping.get((m,n)):
            if m == 1 and n == 1:
                return [M[m-1][n-1]]
            else:
                res = []
                if n > 1:
                    a = self.printAllPaths(M, m, n-1)
                    for i in a:
                        if not isinstance(i, list):
                            i = [i]
                        res.append(i+[M[m-1][n-1]])
                if m > 1:
                    b = self.printAllPaths(M, m-1, n)
                    for i in b:
                        if not isinstance(i, list):
                            i = [i]
                        res.append(i+[M[m-1][n-1]])
            self.mapping[(m,n)] = res
        return self.mapping.get((m,n))
 
M = file_list
m, n = len(M), len(M[0])
a = Solution()
res = a.printAllPaths(M, m, n)
for i in res:
    print(i)




