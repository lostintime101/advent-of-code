from collections import defaultdict

dirs = defaultdict(int)
stack = ["home"]

def end_count(c):
    
    for level in stack:
        dirs[level] += c
    

with open("day7_input.txt", "r") as file:

    counting = False
    count = 0
    
    for line in file:

        line = line.strip()
 
        if line == "$ ls":
            counting = True
            continue

        if line == "$ cd /":
            if counting: end_count(count)
            stack = ["home"]
            counting = False
            count = 0
            continue

        if line == "$ cd ..":
            if counting: end_count(count)
            stack.pop()
            counting = False
            count = 0
            continue

        if line[:4] == "$ cd":
            if counting: 
                end_count(count)
            stack.append(stack[-1]+"/"+line[5:])
            counting = False
            count = 0
            continue

        if line[0] == "d":
            continue
        
        if counting:
            line = line.split(" ")
            size = int(line[0])
            count += size


# print(dirs)

# total = 0
# for k,v in dirs.items():
#     if v < 100_000:
#         total += v

# print(total)


        
# free up enough space to run the update
# PART 2

print(dirs)

space_needed = dirs['home'] - 40_000_000
print(space_needed)
# space_needed = 532950
print(min(weight for weight in dirs.values() if weight >= space_needed))


# print("space_needed", space_needed)

# chosen = float("inf")
# for k,v in dirs.items():
#     if v > space_needed:
#         chosen = min(chosen, v)

# # 386_246 too low
# print(chosen)
# print(chosen - space_needed)




