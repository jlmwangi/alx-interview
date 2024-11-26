#!/usr/bin/python3

def island_perimeter(grid):
    """grid is a list of list of integers
    0 reps water and 1 reps land
    function should return perimeter of land described in grid
    """
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(rows):
        '''go throu each cell'''
        for j in range(cols):
            if grid[i][j] == 1:
                '''if we encounter a land cell, add 4'''
                count += 4

                if i < rows - 1 and grid[i + 1][j] == 1:
                    '''if a land ceell exists below current land cell'''
                    count -= 2
                if j < cols - 1 and grid[i][j + 1] == 1:
                    '''if land cell exists to right of current land cell'''
                    count -= 2

    return count
