
# PART 1
# cycle, value = 0, 1
# checkpoints = [220, 180, 140, 100, 60, 20]
# checkpoint_vals = []

# with open("day10_input.txt", "r") as file:
    
#     """ SAMPLE INPUT
#     addx 15
#     addx -11
#     noop  
#     """

#     for line in file:
        
#         line = line.strip()

#         if line == "noop":
#             cycle += 1
#             if checkpoints and cycle == checkpoints[-1]:
#                 checkpoint_vals.append(value * checkpoints[-1])
#                 checkpoints.pop()
#         else:
#             line = int(line.split(" ")[-1])
#             cycle += 1

#             if checkpoints and cycle == checkpoints[-1]:
#                 checkpoint_vals.append(value * checkpoints[-1])
#                 checkpoints.pop()

#             cycle += 1

#             if checkpoints and cycle == checkpoints[-1]:
#                 checkpoint_vals.append(value * checkpoints[-1])
#                 checkpoints.pop()           
        
#             value += line
        
#         print(f"Cycle: {cycle}, Value: {value}")


# print(checkpoint_vals, sum(checkpoint_vals))

# PART 2
cycle, value = 0, 1
checkpoints = [240, 200, 160, 120, 80, 40]
checkpoint_vals = []

with open("day10_input.txt", "r") as file:
    
    """ SAMPLE INPUT
    addx 15
    addx -11
    noop  
    """
    curr = ""
    values = []
    for line in file:
        
        line = line.strip()

        if line == "noop":
            
            if cycle % 40 in [value, value-1, value+1]: curr += "#"
            else: curr += "."
            cycle += 1

            if checkpoints and cycle == checkpoints[-1]:
                print(curr)
                curr = ""
                checkpoint_vals.append(value * checkpoints[-1])
                checkpoints.pop()
        else:
            line = int(line.split(" ")[-1])
            
            if cycle % 40 in [value, value-1, value+1]: curr += "#"
            else: curr += "."
            cycle += 1
            
            if checkpoints and cycle == checkpoints[-1]:
                print(curr)
                curr = ""
                checkpoint_vals.append(value * checkpoints[-1])
                checkpoints.pop()

            
            if cycle % 40 in [value, value-1, value+1]: curr += "#"
            else: curr += "."
            cycle += 1

            if checkpoints and cycle == checkpoints[-1]:
                print(curr)
                curr = ""
                checkpoint_vals.append(value * checkpoints[-1])
                checkpoints.pop()           
        
            value += line
            values.append(value)
        
        # print(f"Cycle: {cycle}, Value: {value}")

# print(values)  
# print(checkpoint_vals, sum(checkpoint_vals))