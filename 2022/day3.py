# PART 1
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# print(ord("a")) #97 -> 1     -96
# print(ord("A")) #65 -> 27    -38

ans = []
with open("day3_input.txt", "r") as file:
    
    for line in file:
        line = line.strip()

        half = len(line) // 2

        first_half = line[:half]
        second_half = line[half:]
        
        ans.append([ord(l) for l in first_half if l in second_half][0])

for i in range(len(ans)):
    if ans[i] > 96: 
        ans[i] -= 96
    else: ans[i] -= 38

print(sum(ans))


# PART 2

ans = []
curr = []
count = 0

with open("day3_input.txt", "r") as file:

    for line in file:
        line = line.strip()

        curr.append(line)
        count += 1

        if count == 3:
            ans.append([ord(l) for l in curr[0] if (l in curr[1]) and (l in curr[2])][0])

            curr = []
            count = 0

for i in range(len(ans)):
    if ans[i] > 96: 
        ans[i] -= 96
    else: ans[i] -= 38

print(sum(ans))

