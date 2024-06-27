#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """Generates Pascal's Triangle up to the given number of rows."""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for cur_row in range(n):
        # define a row and fill first and last idx with 1
        new_row = [0] * (cur_row + 1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for col_index in range(1, cur_row):
            if col_index > 0 and col_index < len(new_row):
                left_value = pascal_triangle[cur_row - 1][col_index]
                upper_left_value = pascal_triangle[cur_row - 1][col_index - 1]
                new_row[col_index] = left_value + upper_left_value

        pascal_triangle[cur_row] = new_row

    return pascal_triangle