import time
import numpy as np

BOARD_SIZE_X = 5
BOARD_SIZE_Y = 5
START_X = 0
START_Y = 0
TOTAL_STEPS = BOARD_SIZE_X * BOARD_SIZE_Y


def show_result(result):
    matrix = np.zeros(shape=(BOARD_SIZE_Y, BOARD_SIZE_X))
    for i in range(0, len(result)):
        matrix[result[i][1]][result[i][0]] = i + 1
    print(matrix)


def step_action(i, j, used_steps_list, best_list):
    used_steps_list.append((i, j))
    if len(best_list) < len(used_steps_list):
        best_list.clear()
        best_list.extend(used_steps_list)
        print("Best try so far {} steps in {:.5f} seconds".format(len(best_list), time.time() - start_time))
        if len(best_list) == TOTAL_STEPS:
            return True

    next_steps = [(i - 2, j - 1), (i - 2, j + 1), (i + 2, j - 1), (i + 2, j + 1),
                  (i - 1, j - 2), (i + 1, j - 2), (i - 1, j + 2), (i + 1, j + 2)]

    for ns in next_steps:
        if 0 <= ns[0] < BOARD_SIZE_X and 0 <= ns[1] < BOARD_SIZE_Y and ns not in used_steps_list:
            if step_action(ns[0], ns[1], used_steps_list, result):
                return True
    used_steps_list.pop()
    return False


print("Solving the horse problem using brute force\n")

start_time = time.time()
result = []
success = step_action(START_X, START_Y, [], result)
print("{}X{} ({},{}) {} Success in {:.5f} seconds\n".format(
    BOARD_SIZE_X, BOARD_SIZE_Y, START_X, START_Y, "Not" if not success else "Yay!", time.time() - start_time))

if success:
    show_result(result)


