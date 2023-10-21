
# # PART 1
# with open("day6_input.txt", "r") as file:
    
#     # rgffbnnqvqhhmtmzzmmpmllcg...
#     for line in file:
#         line = line.strip()

#         for i in range(len(line)):
            
#             curr = line[i:i+4]
#             if len(set(curr)) == len(curr):
#                 print(curr, i+4)
#                 break

# PART 2
with open("day6_input.txt", "r") as file:
    
    # rgffbnnqvqhhmtmzzmmpmllcg...
    for line in file:
        line = line.strip()

        for i in range(len(line)):
            
            curr = line[i:i+14]
            if len(set(curr)) == len(curr):
                print(curr, i+14)
                break
