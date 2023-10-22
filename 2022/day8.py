
# Sample input
# 202002313322443443333413205214140320025450316364504141264123114304203303114001123204003420102030300

# PART 1

# with open("day8_input.txt", "r") as file:
#     grid = []
#     for line in file:
#         line = line.strip()
#         row = []
#         for char in line:
#             row.append(int(char))
#         grid.append(row)

# ROWS, COLS = len(grid), len(grid[0])

# ans = [[0 for col in range(COLS)] for row in range(ROWS)]

# print(len(ans) == len(grid), len(ans[0]) == len(grid[0]))

# for row in range(ROWS):
#     row_max = -1
#     for col in range(COLS):
#         if grid[row][col] > row_max:
#             ans[row][col] = 1
#             row_max = grid[row][col]

# curr = 0
# for row in ans:
#     curr += sum(row)
# print(curr)

# for row in range(ROWS):
#     row_max = -1
#     for col in range(COLS-1, -1, -1):
#         if grid[row][col] > row_max:
#             ans[row][col] = 1
#             row_max = grid[row][col]

# curr = 0
# for row in ans:
#     curr += sum(row)
# print(curr)

# for col in range(COLS):
#     col_max = -1
#     for row in range(ROWS):
#         if grid[row][col] > col_max:
#             ans[row][col] = 1
#             col_max = grid[row][col]

# curr = 0
# for row in ans:
#     curr += sum(row)
# print(curr)


# for col in range(COLS):
#     col_max = -1
#     for row in range(ROWS-1, -1, -1):
#         if grid[row][col] > col_max:
#             ans[row][col] = 1
#             col_max = grid[row][col]

# curr = 0
# for row in ans:
#     curr += sum(row)
# print(curr)


# PART 2

with open("day8_input.txt", "r") as file:
    grid = []
    for line in file:
        line = line.strip()
        row = []
        for char in line:
            row.append(int(char))
        grid.append(row)

ROWS, COLS = len(grid), len(grid[0])
ans = 0

for row in range(ROWS):
    for col in range(COLS):

        curr = grid[row][col]
        left, right, up, down = 0, 0, 0, 0

        # deal with grid edges
        if not col or not row: continue
        if col == COLS-1 or row == ROWS-1: continue

        for l in range(col-1, -1, -1):
            left += 1
            if grid[row][l] >= curr: break
        
        for r in range(col+1, COLS, 1):
            right += 1
            if grid[row][r] >= curr: break

        for u in range(row-1, -1, -1):
            up += 1
            if grid[u][col] >= curr: break
        
        for d in range(row+1, ROWS, 1):
            down += 1
            if grid[d][col] >= curr: break

        ans = max(ans, left*right*up*down)

print(ans) 




        

