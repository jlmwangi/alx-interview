#!/usr/bin/python3

def island_perimeter(grid):
    """grid is a list of list of integers
    0 reps water and 1 reps land
    function should return perimeter of land described in grid
    """
    rows, cols = len(grid), len(grid[0])
    count = 0

    '''go through each cell'''
    for i in range(rows):
        for j in range(cols):
            '''if we encounter a land cell, add 4'''
            if grid[i][j] == 1:
                count += 4

                '''if a land cell exists below current land cell'''
                if i < rows - 1 and grid[i + 1][j] == 1:
                    count -= 2
                '''if a land cell exists to the right of curr land celi'''
                if j < cols - 1 and grid[i][j + 1] == 1:
                    count -= 2

    return count
