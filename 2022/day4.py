
# PART 1
# ans = []
# with open("day4_input.txt", "r") as file:
    
#     count = 0
#     #24-27,28-97
#     for line in file:
#         line = line.strip()
#         line = line.split(",")
#         first, second = line[0].split("-"), line[1].split("-")
#         first_start = int(first[0])
#         first_end = int(first[1])
#         second_start = int(second[0])
#         second_end = int(second[1])

#         # print(first_start, first_end, second_start, second_end)

        
#         if (first_start <= second_start) and (first_end >= second_end):
#             count += 1
#             print("A", first_start, first_end, second_start, second_end)
#         elif (second_start <= first_start) and (second_end >= first_end):
#             count += 1
#             print("B",first_start, first_end, second_start, second_end)

# print(count)


# PART 2
ans = []
with open("day4_input.txt", "r") as file:
    
    count = 0
    #24-27,28-97
    for line in file:
        line = line.strip().split(",")
        first, second = line[0].split("-"), line[1].split("-")
        first_start, first_end = int(first[0]), int(first[1])
        second_start, second_end = int(second[0]), int(second[1])

        if (first_end < second_start) or (first_start > second_end): continue
        else: count += 1

print(count) # 792
