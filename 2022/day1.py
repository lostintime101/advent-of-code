
# Part 1

totals, curr = [], 0

with open("day1_input.txt", "r") as file:
    
    for line in file:
        line = line.strip()
        
        if line:
            curr += int(line)
        else:
            totals.append(curr)
            curr = 0

print(max(totals))

# Part 2

print(sum(sorted(totals)[-3::]))