grid = [
    [10, 11, 12, 13, 14, 15],
    [20, 21, 22, 23, 24, 25],
    [30, 31, 32, 33, 34, 35],
    [40, 41]
]

print(grid[2][1])

for row in grid:
    for column in row:
        print(column)