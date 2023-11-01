#!/usr/bin/python3
"""Module containing program to solve the N queens problem"""
import sys


def backtrack(row, N, cols, pos, neg, board):
    """Function to backtrack"""
    if row == N:
        result = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    result.append([l, k])
        print(result)
        return

    for col in range(N):
        if col in cols or (row + col) in pos or (row - col) in neg:
            continue

        cols.add(col)
        pos.add(row + col)
        neg.add(row - col)
        board[row][col] = 1

        backtrack(row + 1, N, cols, pos, neg, board)

        cols.remove(col)
        pos.remove(row + col)
        neg.remove(row - col)
        board[row][col] = 0


def nqueens(N):
    """Returns every possible solution to the nqueens problem"""
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * N for i in range(N)]

    backtrack(0, N, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    N = sys.argv
    if len(N) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N_N = int(N[1])
        if N_N < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(N_N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
