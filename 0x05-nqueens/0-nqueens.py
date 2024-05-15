#!/usr/bin/python3
'''N queens Backtracking'''


from typing import List


def reset_board(board: List[List[int]], i, j,  n):
    '''reset the board by filling it with -1'''
    for i in range(n):
        for j in range(n):
            board[i][j] = -1


def check_vertically(board: List[List[int]], i: int, index: int, set, n: int):
    '''check the row 'i' of the board'''

    # y: iterate the columns
    if set == True:
        for y in range(n):
            if board[i][y] == -1:
                board[i][y] = index
    else:
        for y in range(n):
            if board[i][y] == index:
                board[i][y] = -1


def check_horizontally(board: List[List[int]], j: int, index, set, n: int):
    '''check the column 'j' of the board'''

    # x: iterate the rows
    if set == True:
        for x in range(n):
            if board[x][j] == -1:
                board[x][j] = index
    else:
        for x in range(n):
            if board[x][j] == index:
                board[x][j] = -1


def check_diagonally(board: List[List[int]], i: int, j: int, index, set, n: int):
    '''check diagonally downward and upward the board from indexes "i" and "j"'''

    dr_i = dl_i = ur_i = ul_i = i
    dr_j = dl_j = ur_j = ul_j = j

    # check downward right
    while dr_i < n and dr_j < n:
        if set == True:
            if board[dr_i][dr_j] == -1:
                board[dr_i][dr_j] = index
        else:
            if board[dr_i][dr_j] == index:
                board[dr_i][dr_j] = -1

        dr_i += 1
        dr_j += 1

    # check downward left
    while dl_i < n and dl_j >= 0:
        if set == True:
            if board[dl_i][dl_j] == -1:
                board[dl_i][dl_j] = index
        else:
            if board[dl_i][dl_j] == index:
                board[dl_i][dl_j] = -1
        dl_i += 1
        dl_j -= 1

    # check upward left
    while ul_i >= 0 and ul_j >= 0:
        if set == True:
            if board[ul_i][ul_j] == -1:
                board[ul_i][ul_j] = index
        else:
            if board[ul_i][ul_j] == index:
                board[ul_i][ul_j] = -1
        ul_i -= 1
        ul_j -= 1

    # check upward right
    while ur_i >= 0 and ur_j < n:
        if set == True:
            if board[ur_i][ur_j] == -1:
                board[ur_i][ur_j] = index
        else:
            if board[ur_i][ur_j] == index:
                board[ur_i][ur_j] = -1
        ur_i -= 1
        ur_j += 1


def check_from_pos(board, queen_i, queen_j, index, set, n):
    '''check all the possible routes of a queen at position'''
    check_horizontally(board, queen_j, index, set, n)
    check_vertically(board, queen_i, index, set, n)
    check_diagonally(board, queen_i, queen_j, index, set, n)


def get_choices(board, row, n):
    '''get the valid choices in a row'''

    choices = []
    if row < n:
        for j in range(n):
            if board[row][j] == -1:
                choices.append((row, j))

    return choices


def n_queens(board: List[List[int]], n: int, choices: List, solution: List, solutions: List[List[int]]):

    if len(solution) == n:
        solutions.append(solution)
        print(solution)
        return

    for c in choices:
        i, j = c

        board[i][j] = j
        solution.append((i, j))
        check_from_pos(board, i, j, j, True, n)
        next_line_choices = get_choices(board, i + 1, n)
        # print(f'c = {c} next_line_choices = {next_line_choices} board = {board}')
        n_queens(board, n, next_line_choices, solution, solutions)
        check_from_pos(board, i, j, j, False, n)
        solution.pop()

    return


def main():
    '''main function'''

    n = 8
    board = [[-1] * n for _ in range(n)]

    choices = get_choices(board, 0, n)

    n_queens(board, n, choices, [], [])


if __name__ == '__main__':
    main()
