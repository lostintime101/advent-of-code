# Part 1

# Ops: A for Rock, B for Paper, and C for Scissors
# Us: X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

mappings = {
    "A X": 4, # 1 + 3 
    "A Y": 8, # 2 + 6
    "A Z": 3, # 3 + 0
    "B X": 1, # 1 + 0
    "B Y": 5, # 2 + 3
    "B Z": 9, # 3 + 6
    "C X": 7, # 1 + 6
    "C Y": 2, # 2 + 0
    "C Z": 6, # 3 + 3
}

total = 0

with open("day2_input.txt", "r") as file:
    
    for line in file:
        
        total += mappings[line.strip()]

print(total)


# Part 2
# Ops: A for Rock, B for Paper, and C for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

mappings = {
    "A X": 3, # 0 + 3
    "A Y": 4, # 3 + 1
    "A Z": 8, # 6 + 2
    "B X": 1, # 0 + 1
    "B Y": 5, # 3 + 2
    "B Z": 9, # 6 + 3
    "C X": 2, # 0 + 2
    "C Y": 6, # 3 + 3
    "C Z": 7, # 6 + 1
}

total = 0

with open("day2_input.txt", "r") as file:
    
    for line in file:
        
        total += mappings[line.strip()]

print(total)