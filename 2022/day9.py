# sample input
# R 1
# D 1
# U 1
# R 2
# L 2
# U 2
# D 1
# L 2
# R 1

# PART 1

# def tail_reaction(H, T):

#     x_diff = T[0] - H[0]
#     y_diff = T[1] - H[1]

#     if x_diff > 1: 
#         T[0] -= 1
#         T[1] = H[1]
#     elif x_diff < -1: 
#         T[0] += 1
#         T[1] = H[1]

#     if y_diff > 1: 
#         T[1] -= 1
#         T[0] = H[0]
#     elif y_diff < -1: 
#         T[1] += 1
#         T[0] = H[0]


# with open("day9_input.txt", "r") as file:
    
#     H, T = [0,0], [0,0]
#     seen = set()
#     seen.add(tuple(T))
#     # print(seen)
#     # print(H,T)
    
#     for line in file:
#         line = line.split(" ")
#         direction, steps = line[0], int(line[1])

#         if direction == "L":
#             for step in range(steps):
#                 H[0] -= 1
#                 tail_reaction(H, T)
#                 seen.add(tuple(T))
#                 # print(H,T)
#             continue
        
#         if direction == "R":
#             for step in range(steps):
#                 H[0] += 1
#                 tail_reaction(H, T)
#                 seen.add(tuple(T))
#                 # print(H,T)
#             continue

#         if direction == "U":
#             for step in range(steps):
#                 H[1] += 1
#                 tail_reaction(H, T)
#                 seen.add(tuple(T))
#                 # print(H,T)
#             continue

#         if direction == "D":
#             for step in range(steps):
#                 H[1] -= 1
#                 tail_reaction(H, T)
#                 seen.add(tuple(T))
#                 # print(H,T)
#             continue

# 4586 your answer is too low
# 4587 your answer is too low
# print(len(seen))

# PART 2


def tail_reaction(early, late):

    x_diff = late[0] - early[0]
    y_diff = late[1] - early[1]

    if [x_diff, y_diff] == [2,0]: late[0] -= 1  
    elif [x_diff, y_diff] == [-2,0]: late[0] += 1
    elif [x_diff, y_diff] == [0,2]: late[1] -= 1
    elif [x_diff, y_diff] == [0,-2]: late[1] += 1
    elif [x_diff, y_diff] in [[1,2], [2,2], [2,1]]:
        late[0] -= 1
        late[1] -= 1
    elif [x_diff, y_diff] in [[-1,-2], [-2,-2], [-2,-1]]:
        late[0] += 1
        late[1] += 1
    elif [x_diff, y_diff] in [[1,-2], [2,-2], [2,-1]]:
        late[0] -= 1
        late[1] += 1
    elif [x_diff, y_diff] in [[-1,2], [-2,2], [-2,1]]:
        late[0] += 1
        late[1] -= 1
    
    return late


with open("day9_input.txt", "r") as file:
    
    H, T1, T2, T3, T4, T5, T6, T7, T8, T9  = [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]
    seen = set()
    seen.add(tuple(T9))
    
    for line in file:
        line = line.split(" ")
        direction, steps = line[0], int(line[1])

        if direction == "L":
            for step in range(steps):
                H[0] -= 1
                T1 = tail_reaction(H, T1)
                T2 = tail_reaction(T1, T2)
                T3 = tail_reaction(T2, T3)
                T4 = tail_reaction(T3, T4)
                T5 = tail_reaction(T4, T5)
                T6 = tail_reaction(T5, T6)
                T7 = tail_reaction(T6, T7)
                T8 = tail_reaction(T7, T8)
                T9 = tail_reaction(T8, T9)
                seen.add(tuple(T9))
                # print(H, T1, T2, T3, T4, T5, T6, T7, T8, T9)
            continue
        
        if direction == "R":
            for step in range(steps):
                H[0] += 1
                T1 = tail_reaction(H[::], T1[::])
                T2 = tail_reaction(T1[::], T2[::])
                T3 = tail_reaction(T2[::], T3[::])
                T4 = tail_reaction(T3[::], T4[::])
                T5 = tail_reaction(T4[::], T5[::])
                T6 = tail_reaction(T5[::], T6[::])
                T7 = tail_reaction(T6[::], T7[::])
                T8 = tail_reaction(T7[::], T8[::])
                T9 = tail_reaction(T8[::], T9[::])
                seen.add(tuple(T9))
                # print(H, T1, T2, T3, T4, T5, T6, T7, T8, T9)
            continue

        if direction == "U":
            for step in range(steps):
                H[1] += 1
                T1 = tail_reaction(H[::], T1[::])
                T2 = tail_reaction(T1[::], T2[::])
                T3 = tail_reaction(T2[::], T3[::])
                T4 = tail_reaction(T3[::], T4[::])
                T5 = tail_reaction(T4[::], T5[::])
                T6 = tail_reaction(T5[::], T6[::])
                T7 = tail_reaction(T6[::], T7[::])
                T8 = tail_reaction(T7[::], T8[::])
                T9 = tail_reaction(T8[::], T9[::])
                seen.add(tuple(T9))
                # print(H, T1, T2, T3, T4, T5, T6, T7, T8, T9)
            continue

        if direction == "D":
            for step in range(steps):
                H[1] -= 1
                T1 = tail_reaction(H[::], T1[::])
                T2 = tail_reaction(T1[::], T2[::])
                T3 = tail_reaction(T2[::], T3[::])
                T4 = tail_reaction(T3[::], T4[::])
                T5 = tail_reaction(T4[::], T5[::])
                T6 = tail_reaction(T5[::], T6[::])
                T7 = tail_reaction(T6[::], T7[::])
                T8 = tail_reaction(T7[::], T8[::])
                T9 = tail_reaction(T8[::], T9[::])
                seen.add(tuple(T9))
                # print(H, T1, T2, T3, T4, T5, T6, T7, T8, T9)
            continue

print(len(seen))