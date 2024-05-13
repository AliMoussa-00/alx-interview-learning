#!/usr/bin/python3
'''N queens Backtracking'''


from typing import List


def check_vertically(board: List[List[int]], i: int, n: int):
    '''check the row 'i' of the board'''

    # y: iterate the columns
    for y in range(n):
        if board[i][y] != 1:
            board[i][y] = 0


def check_horizontally(board: List[List[int]], j: int, n: int):
    '''check the column 'j' of the board'''

    # x: iterate the rows
    for x in range(n):
        if board[x][j] != 1:
            board[x][j] = 0


def check_diagonally(board: List[List[int]], i: int, j: int, n: int):
    '''check diagonally downward and upward the board from indexes "i" and "j"'''

    dr_i = dl_i = ur_i = ul_i = i
    dr_j = dl_j = ur_j = ul_j = j

    # check downward right
    while dr_i < n and dr_j < n:
        if board[dr_i][dr_j] != 1:
            board[dr_i][dr_j] = 0
        dr_i += 1
        dr_j += 1

    # check downward left
    while dl_i < n and dl_j >= 0:
        if board[dl_i][dl_j] != 1:
            board[dl_i][dl_j] = 0
        dl_i += 1
        dl_j -= 1

    # check upward left
    while ul_i >= 0 and ul_j >= 0:
        if board[ul_i][ul_j] != 1:
            board[ul_i][ul_j] = 0
        ul_i -= 1
        ul_j -= 1

    # check upward right
    while ur_i >= 0 and ur_j < n:
        if board[ur_i][ur_j] != 1:
            board[ur_i][ur_j] = 0
        ur_i -= 1
        ur_j += 1


def main():
    '''main function'''

    n = 4
    board = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
    ]

    print(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                board[i][j] = 1
                check_horizontally(board, j, n)
                check_vertically(board, i, n)
                check_diagonally(board, i, j, n)

    print(board)


if __name__ == '__main__':
    main()
