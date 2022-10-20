
def gridChallenge(grid):
    sorted_grid = []
    for letters in grid:
        grid_list = list(letters)
        grid_list.sort()
        sorted_grid.append(grid_list)
    for i in range(0, len(grid[0])):
        for j in range(0, len(sorted_grid)-1):
            c1 = sorted_grid[j][i]
            c2 = sorted_grid[j+1][i]
            if c1 > c2:
                return "NO"
    return "YES"


grid = ["abc", "hjk", "mpq", "rtv"]
print(gridChallenge(grid))