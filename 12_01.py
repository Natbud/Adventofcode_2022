import string
import numpy as np



thefilepath = "12_01_Test_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()





alphabet = list(map(chr, range(97, 123)))
print(alphabet)

