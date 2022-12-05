thefilepath = "02_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]   #strips out the /n character from each line

shape_score=0
outcome_score=0
round_score=0
cumulative_score=0

for line in file_list:
    # Get my score for shape played:
    if line[2]=="X":
        shape_score=1
    if line[2]=="Y":
        shape_score=2
    if line[2]=="Z":
        shape_score=3

    # Now find if I draw:
    if line == "A X" or line == "B Y" or line == "C Z":
        outcome_score=3
    # And if I lose:
    if line == "A Z" or line == "B X" or line == "C Y":
        outcome_score=0
    # And if I win:
    if line == "C X" or line == "A Y" or line == "B Z":
        outcome_score=6
    
    round_score = shape_score + outcome_score

    cumulative_score += round_score

print ("Final Cumulative Score For All Rounds:", cumulative_score)
