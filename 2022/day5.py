
#     [G]         [P]         [M]    
#     [V]     [M] [W] [S]     [Q]    
#     [N]     [N] [G] [H]     [T] [F]
#     [J]     [W] [V] [Q] [W] [F] [P]
# [C] [H]     [T] [T] [G] [B] [Z] [B]
# [S] [W] [S] [L] [F] [B] [P] [C] [H]
# [G] [M] [Q] [S] [Z] [T] [J] [D] [S]
# [B] [T] [M] [B] [J] [C] [T] [G] [N]
#  1   2   3   4   5   6   7   8   9 

stacks = {
1:["B", "G", "S", "C"],
2:["T", "M", "W", "H", "J", "N", "V", "G"],
3:["M", "Q", "S"],
4:["B", "S", "L", "T", "W", "N", "M"],
5:["J", "Z", "F", "T", "V", "G", "W", "P"],
6:["C", "T", "B", "G", "Q", "H", "S"],
7:["T", "J", "P", "B", "W"],
8:["G", "D", "C", "Z", "F", "T", "Q", "M"],
9:["N", "S", "H", "B", "P", "F"]
}

# PART1
# with open("day5_input.txt", "r") as file:
# # move 3 from 8 to 5
#     for line in file:
#         line = line.strip().split(" ")
#         count, fr, to = int(line[1]), int(line[3]), int(line[5])
#         print(count, fr, to)

#         while count:
#             stacks[to].append(stacks[fr].pop())
#             count -= 1

# ans = ""
# for stack in stacks.values():
#     ans += stack[-1]

# print(ans)


# PART2

with open("day5_input.txt", "r") as file:
    
    # move 3 from 8 to 5
    for line in file:
        line = line.strip().split(" ")
        count, fr, to = int(line[1]), int(line[3]), int(line[5])
        print(count, fr, to)

        count *= -1
        stacks[to].extend(stacks[fr][count:])
        stacks[fr] = stacks[fr][:count]

ans = ""
for stack in stacks.values():
    ans += stack[-1]

print(ans)