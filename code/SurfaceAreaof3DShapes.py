#Heavily borrowed from Lee256 https://leetcode.com/problems/surface-area-of-3d-shapes/discuss/163414/C%2B%2BJava1-line-Python-Minus-Hidden-Area

def surfaceArea(grid):
    n, res = len(grid), 0
    for i in range(n):
        for j in range(n):
            if grid[i][j]: res += 4 * grid[i][j] + 2
            if i: res -= min(grid[i - 1][j], grid[i][j]) * 2
            if j: res -= min(grid[i][j], grid[i][j - 1]) * 2
    return res

if __name__ == '__main__':
    grid = [[1, 2], [3, 4]]

    surfaceArea(grid)
