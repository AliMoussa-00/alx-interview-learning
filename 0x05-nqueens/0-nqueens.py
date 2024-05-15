#!/usr/bin/python3
'''N queens Backtracking'''


import sys
from typing import List


def mark_vertically(board: List[List[int]], i: int, mark: int, set, n: int):
    '''Mark positions attacked by the queen in the row'''

    # y: iterate the columns
    if set:
        for y in range(n):
            if board[i][y] == -1:
                board[i][y] = mark
    else:
        for y in range(n):
            if board[i][y] == mark:
                board[i][y] = -1


def mark_horizontally(board: List[List[int]], j: int, mark, set, n: int):
    '''Mark positions attacked by the queen in the column'''

    # x: iterate the rows
    if set:
        for x in range(n):
            if board[x][j] == -1:
                board[x][j] = mark
    else:
        for x in range(n):
            if board[x][j] == mark:
                board[x][j] = -1


def mark_diagonally(
        board: List[List[int]], i: int, j: int, mark, set, n: int):
    '''
    Mark positions attacked by the queen, diagonally
    '''

    dr_i = dl_i = ur_i = ul_i = i
    dr_j = dl_j = ur_j = ul_j = j

    # mark downward right
    while dr_i < n and dr_j < n:
        if set:
            if board[dr_i][dr_j] == -1:
                board[dr_i][dr_j] = mark
        else:
            if board[dr_i][dr_j] == mark:
                board[dr_i][dr_j] = -1

        dr_i += 1
        dr_j += 1

    # mark downward left
    while dl_i < n and dl_j >= 0:
        if set:
            if board[dl_i][dl_j] == -1:
                board[dl_i][dl_j] = mark
        else:
            if board[dl_i][dl_j] == mark:
                board[dl_i][dl_j] = -1
        dl_i += 1
        dl_j -= 1

    # mark upward left
    while ul_i >= 0 and ul_j >= 0:
        if set:
            if board[ul_i][ul_j] == -1:
                board[ul_i][ul_j] = mark
        else:
            if board[ul_i][ul_j] == mark:
                board[ul_i][ul_j] = -1
        ul_i -= 1
        ul_j -= 1

    # mark upward right
    while ur_i >= 0 and ur_j < n:
        if set:
            if board[ur_i][ur_j] == -1:
                board[ur_i][ur_j] = mark
        else:
            if board[ur_i][ur_j] == mark:
                board[ur_i][ur_j] = -1
        ur_i -= 1
        ur_j += 1


def mark_attacked_positions(
        board, queen_i, queen_j, mark, set, n):
    '''Mark positions attacked by the queen placed at (i, j)'''
    mark_horizontally(board, queen_j, mark, set, n)
    mark_vertically(board, queen_i, mark, set, n)
    mark_diagonally(board, queen_i, queen_j, mark, set, n)


def get_available_positions(board, row, n):
    '''Get available positions for queen placement in a row'''

    choices = []
    if row < n:
        for j in range(n):
            if board[row][j] == -1:
                choices.append((row, j))

    return choices


def n_queens(board, n, choices, queens, solutions):
    '''
    recursive function to get all the placements
    of the queens in the board using:
    Backtracking algorithm
    '''

    if len(queens) == n:
        solutions.append(queens[:])  # Append a valid queens positioning
        return

    for c in choices:
        i, j = c

        board[i][j] = j
        queens.append([i, j])
        mark_attacked_positions(board, i, j, j, True, n)
        next_line_choices = get_available_positions(board, i + 1, n)

        n_queens(board, n, next_line_choices, queens, solutions)
        mark_attacked_positions(board, i, j, j, False, n)
        queens.pop()

    return


def main():
    '''main function'''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)

        board = [[-1] * n for _ in range(n)]

        choices = get_available_positions(board, 0, n)
        solutions = []

        n_queens(board, n, choices, [], solutions)

        for solution in solutions:
            print(solution)

    except ValueError:
        print("N must be a number")
        sys.exit(1)


if __name__ == '__main__':
    main()
