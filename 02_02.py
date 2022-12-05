thefilepath = "02_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]   #strips out the /n character from each line

shape_score=0
outcome_score=0
round_score=0
cumulative_score=0

for line in file_list:
    # Outcome score dictated by 2nd value only:
    if line[2]=="X":
        outcome_score=0
        # Now find which shape is required for LOSING:
        if line[0]=="A": shape_score=3 # Rock  Scissors  = LOSE
        if line[0]=="B": shape_score=1 # Paper Rock  = LOSE
        if line[0]=="C": shape_score=2 # Scissors Paper = LOSE
    
    # Now find which shape is required for DRAWING:
    if line[2]=="Y":
        outcome_score=3
        if line[0]=="A": shape_score=1 # Rock Rock  = DRAW
        if line[0]=="B": shape_score=2 # Paper Paper  = DRAW
        if line[0]=="C": shape_score=3 # Scissors Scissors  = DRAW

    # Now find which shape is required for WINNING:
    if line[2]=="Z":
        outcome_score=6
        if line[0]=="A": shape_score=2 # Rock Paper = WIN
        if line[0]=="B": shape_score=3 # Paper Scissors = WIN
        if line[0]=="C": shape_score=1 # Scissors Rock = WIN  

    round_score = shape_score + outcome_score
    
    cumulative_score += round_score

print ("Final Cumulative Score For All Rounds:", cumulative_score)
