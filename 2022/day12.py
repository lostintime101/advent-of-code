from typing import List
from functools import cache
import sys

sys.setrecursionlimit(10000000)

# # PART 1
# # a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.
# # current position (S), evelation 'a' and the location that should get the best signal (E) evelation 'z'
# # next square at most one higher than the elevation of your current square


# with open("day12_input.txt", "r") as file:
    
#     """ SAMPLE INPUT
#     abcccaaaaaccaaaaaaccccaaaaaaccccccaacccaaaaaacccccccccaaaaaacccaaaaaaaaaaaaaaacaaccacccccccccccaaaaaaccccccccccaaaaaacccccccccccccccccccccccccccccccccccccccccaaaaa
#     abccccccaaccaaaaaaccaaaaaaaaccccccaaacaaaacaaacccccccaaaaaaaaccaaaaaaaaaaaaaaacaaaaacccccccccccccaaccccccccccccaaaaaaccccccccccccccccccccccccccccacccccccccccaaaaaa
#     """
#     grid = []
#     for line in file:
#         line = line.strip()
#         grid.append([char for char in line])

# for line in grid: print(line)

# COLS = len(grid[0])
# ROWS = len(grid)
# directions = [(0,-1), (0,1), (-1,0), (1,0)]

# # Find Start & Find End
# for row in range(ROWS):
#     for col in range(COLS):
#         if grid[row][col] == "S":
#             start = (row, col)
#             grid[row][col] = "a"
#         if grid[row][col] == "E":
#             end = (row, col)
#             grid[row][col] = "z"

# ans = []
# seen = [[float("inf")]* COLS for row in range(ROWS)]
# # print(seen)

# @cache
# def dfs(curr: tuple, steps: int) -> None :
    
#     r,c = curr[0],curr[1]
#     if seen[r][c] <= steps: return
#     seen[r][c] = steps

#     if(r,c) == end:
#         ans.append(steps)
#         return

#     for direction in directions:
#         new_r = r + direction[0]
#         new_c = c + direction[1]

#         if (new_r > -1) and (new_r < ROWS) and (new_c > -1) and (new_c < COLS):

#             if ord(grid[new_r][new_c]) > ord(grid[r][c]) + 1: continue
            
#             dfs((new_r, new_c), steps +1)

# dfs(start, 0)
# print(min(ans))


# PART 2

with open("day12_input.txt", "r") as file:
    
    """ SAMPLE INPUT
    abcccaaaaaccaaaaaaccccaaaaaaccccccaacccaaaaaacccccccccaaaaaacccaaaaaaaaaaaaaaacaaccacccccccccccaaaaaaccccccccccaaaaaacccccccccccccccccccccccccccccccccccccccccaaaaa
    abccccccaaccaaaaaaccaaaaaaaaccccccaaacaaaacaaacccccccaaaaaaaaccaaaaaaaaaaaaaaacaaaaacccccccccccccaaccccccccccccaaaaaaccccccccccccccccccccccccccccacccccccccccaaaaaa
    """
    grid = []
    for line in file:
        line = line.strip()
        grid.append([char for char in line])

# for line in grid: print(line)

COLS = len(grid[0])
ROWS = len(grid)
directions = [(0,-1), (0,1), (-1,0), (1,0)]

starts = []
# Find Start & Find End
for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] in ["S", "a"] :
            starts.append((row, col))
            grid[row][col] = "a"
        if grid[row][col] == "E":
            end = (row, col)
            grid[row][col] = "z"
# print("starts: ", starts)

answers = []

# MOVING THIS LINE INSIDE THE LOOP SLOWS THE WHOLE THING DOWN HORRENDOUSLY
# WE ONLY NEED TO CONSIDER NEW PATHS THAT ARE FASTER THAN OLD 
seen = [[float("inf")]* COLS for row in range(ROWS)]

for start in starts:

    ans = []    
    # THE CACHING MESSED THINGS UP, WOULDN'T RUN PROPERLY
    def dfs(curr: tuple, steps: int) -> None :
        
        r,c = curr[0],curr[1]
        if seen[r][c] <= steps: return
        seen[r][c] = steps

        if(r,c) == end:
            ans.append(steps)
            return

        for direction in directions:
            new_r = r + direction[0]
            new_c = c + direction[1]

            if (new_r > -1) and (new_r < ROWS) and (new_c > -1) and (new_c < COLS):

                if ord(grid[new_r][new_c]) > ord(grid[r][c]) + 1: continue
                
                dfs((new_r, new_c), steps +1)

    dfs(start, 0)
    if ans: 
        print(min(ans))
        answers.append(min(ans))

print(min(answers))
