import time
import numpy as np

BOARD_SIZE_X = 8
BOARD_SIZE_Y = 8
TOTAL_STEPS = BOARD_SIZE_X * BOARD_SIZE_Y


class Board:
    def __init__(self, size_i, size_j):
        self.used_square_count = 0
        self.total_squares = size_j * size_i
        self.matrix = np.full((size_j + 4, size_i + 4), self.total_squares + 1)
        for j in range(2, 2 + size_j):
            for i in range(2, 2 + size_i):
                self.matrix[j][i] = 0

    def add_step(self, i, j):
        self.used_square_count += 1
        self.matrix[j + 2][i + 2] = self.used_square_count

    def is_unused_square(self, i, j):
        return self.matrix[j + 2][i + 2] == 0

    def get_matrix(self):
        return self.matrix[2:2 + BOARD_SIZE_Y, 2:2 + BOARD_SIZE_X]

    def are_there_unused_squares(self):
        return self.used_square_count < self.total_squares


def solve(size_i, size_j, start_i, start_j):
    start_time = time.time()
    board = Board(size_i, size_j)
    move_list = [(- 2, - 1), (- 2, + 1), (+ 2, - 1), (+ 2, + 1), (- 1, - 2), (+ 1, - 2), (- 1, + 2), (+ 1, + 2)]
    i = start_i
    j = start_j
    board.add_step(i, j)

    while board.are_there_unused_squares():
        best_next_square = (-1, -1)
        best_next_square_moves = 10000
        for move in move_list:
            next_square_i = i + move[0]
            next_square_j = j + move[1]
            if board.is_unused_square(next_square_i, next_square_j):
                possible_moves_count = 0
                for second_move in move_list:
                    if board.is_unused_square(next_square_i + second_move[0], next_square_j + second_move[1]):
                        possible_moves_count += 1
                if possible_moves_count < best_next_square_moves:
                    best_next_square_moves = possible_moves_count
                    best_next_square = (next_square_i, next_square_j)
        if best_next_square == (-1, -1):
            print("{}X{} ({},{}) Not Success in {:.5f} seconds".format(
                size_i, size_j, start_i, start_j, time.time() - start_time))
            return False, []
        i = best_next_square[0]
        j = best_next_square[1]
        board.add_step(i, j)

    print("{}X{} ({},{}) Yay! Success in {:.5f} seconds".format(
        size_i, size_j, start_i, start_j, time.time() - start_time))

    return True, board.get_matrix()


print("Solving the knight's tour problem using Warnsdorff's algorithm\n")
for start_i in range(0, BOARD_SIZE_X):
    for start_j in range(0, BOARD_SIZE_Y):
        success, matrix = solve(BOARD_SIZE_X, BOARD_SIZE_Y, start_i, start_j)
        if success:
            print(matrix)


