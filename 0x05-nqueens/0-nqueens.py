#!/usr/bin/python3
'''N queens puzzle'''


import sys


def is_safe(board, row, col):
    '''check if its safe to place a queen on board[row][col]'''
    for i in range(col):  # checks current row, no queens placed horizontally
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        '''chevk upper-left diagonal'''
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        '''check lower left diagonal'''
        if board[i][j] == 1:
            return False

    return True


def backtrack_nqueens(board, col, result):
    '''solve nqueens using backtracking by trying
        to place queens one by one in columns'''
    if col >= len(board):  # if all queens are placed append sol
        result.append([i.index(1) for i in board])
        return True

    res = False  # track valid placement for current column

    for i in range(len(board)):  # throu rows of curr col
        if is_safe(board, i, col):  # check if safe to place queen at i, col
            board[i][col] = 1
            res = backtrack_nqueens(board, col + 1, result)
            board[i][col] = 0  # Backtrack

    return res


def solve_nqueens(n):
    '''initialize the board and call backtrack to solve the problem'''
    board = [[0 for _ in range(n)] for _ in range(n)]
    result = []
    backtrack_nqueens(board, 0, result)
    return result


def nqueens():
    '''caals the solver, parses args'''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if (n < 4):
        print("N must be atleast 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


if __name__ == "__main__":
    nqueens()
