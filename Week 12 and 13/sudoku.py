
import turtle
import time
import random

import numpy
import numpy as np
import copy


def draw_grid(tortoise: turtle) -> None:

    tortoise.hideturtle()
    tortoise.speed(0)
    direction = 1
    tortoise.penup()
    tortoise.goto(-N * W / 2, -N * W / 2)
    tortoise.pendown()

    tortoise.pensize(5)
    for i in range(4):
        tortoise.forward(N * W)
        tortoise.left(90)

    for i in range(N):
        if i in range(0, 10, 3):
            tortoise.pensize(3)
        else:
            tortoise.pensize(1)

        tortoise.forward(N * W)
        tortoise.left(90 * direction)
        tortoise.forward(W)
        tortoise.left(90 * direction)
        direction = -1 * direction

    direction = 1

    for i in range(N):
        if i in range(2, 10, 3):
            tortoise.pensize(3)
        else:
            tortoise.pensize(1)

        tortoise.forward(W)
        tortoise.left(90 * direction)
        tortoise.forward(N * W)
        direction = -1 * direction
        tortoise.left(90 * direction)


def goto_xy(tortoise: turtle, x: int, y: int):

    tortoise.penup()
    tortoise.setposition(-(N / 2 - (x + 0.5)) * W, (N / 2 - (y + 1.8 * ratio / 10)) * W)


def write_number(tortoise: turtle, num: int, x: int, y: int, color: str = 'black') -> None:

    goto_xy(tortoise, x, y)
    tortoise.color(color)
    if num:
        tortoise.write(num, move=False, align='center', font=("Verdana", 4 * ratio, "normal"))


def check_rc(grid: numpy, rc: int, orientation: str = 'r') -> set:

    possible_values = set(range(1, 10))
    if orientation == 'r':
        available_choices = possible_values - set(grid.tolist()[rc])

    elif orientation == 'c':
        columns = list(zip(*grid.tolist()))
        available_choices = possible_values - set(columns[rc])

    else:
        available_choices = set()

    return available_choices


def check_square(grid, square_index):

    c = (square_index % 3) * 3
    r = (square_index // 3) * 3
    square = grid[r: r + 3, c: c + 3]
    possible_values = set(range(1, 10))
    available_choices = possible_values - set(sum(square.tolist(), []))
    return available_choices


def initialise(tortoise):

    rows, cols = (N, N)
    # grid = [[0] * cols] * rows
    grid = np.zeros((rows, cols), dtype=int)
    tortoise.clear()
    return grid


def calculate_grid(tortoise):

    grid = initialise(tortoise)
    rc = 0

    while rc - 81:
        row = rc // 9
        col = rc % 9

        si = col // 3 if row < 3 else 3 + col // 3 if row < 6 else 6 + col // 3 if row < 9 else None

        available_square_options = check_square(grid, si)
        available_row_options = check_rc(grid, row, orientation='r')
        available_column_options = check_rc(grid, col, orientation='c')

        if not grid[row, col]:
            candidates = available_square_options.intersection(
                available_row_options).intersection(available_column_options)

            if candidates:
                grid[row, col] = random.choice(list(candidates))
                write_number(tortoise, grid[row, col], col, row)
                rc += 1
            else:
                rc = 0
                grid = initialise(tortoise)

    return grid


def solve_grid(grid, tortoise, color='green'):

    rc = 0
    temp_grid = copy.deepcopy(grid)

    while rc - 81:
        row = rc // 9
        col = rc % 9
        rc += 1

        si = col // 3 if row < 3 else 3 + col // 3 if row < 6 else 6 + col // 3 if row < 9 else None

        available_square_options = check_square(temp_grid, si)
        available_row_options = check_rc(temp_grid, row, orientation='r')
        available_column_options = check_rc(temp_grid, col, orientation='c')

        if not temp_grid[row, col]:
            candidates = available_square_options.intersection(
                available_row_options).intersection(available_column_options)

            if candidates:
                temp_grid[row, col] = random.choice(list(candidates))
                write_number(tortoise, temp_grid[row, col], col, row, color=color)
            else:
                rc = 0
                tortoise.clear()
                temp_grid = copy.deepcopy(grid)

    return temp_grid


def remove_numbers(grid, tortoise, difficulty='medium'):

    difficulty_settings = (30, 'easy'), (40, 'medium'), (50, 'hard')
    attempts = next(idx for idx, val in difficulty_settings if val == difficulty)

    temp_grid = copy.deepcopy(grid)
    while attempts:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if not temp_grid[row, col]:
            continue
        else:
            temp_grid[row, col] = 0
            attempts -= 1

    tortoise.clear()
    rc = 0
    while rc - 81:
        row = rc // 9
        col = rc % 9
        write_number(tortoise, temp_grid[row, col], col, row, color='black')
        rc += 1

    return temp_grid


if __name__ == '__main__':

    N = 9
    W = 40

    ratio = W // 8

    turtle.tracer(0)
    t1 = turtle.Turtle()
    draw_grid(t1)

    time.sleep(4)

    t2 = turtle.Turtle()
    full_grid = calculate_grid(t2)
    #
    time.sleep(4)

    puzzle = remove_numbers(full_grid, t2)

    time.sleep(4)

    t3 = turtle.Turtle()
    solved_grid = solve_grid(puzzle, t3, color='green')

    time.sleep(2)

    print(solved_grid == full_grid)

    turtle.done()

