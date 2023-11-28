#!/usr/bin/python3
"""The Island Perimeter module"""


def island_perimeter(grid):
    """Returns the perimeter of the island as per requirement specifications"""
    perimeter = 0

    if not isinstance(grid, list):
        return perimeter

    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 1:
                boundaries = (
                    i == 0 or grid[i - 1][j] == 0,
                    j == m - 1 or row[j + 1] == 0,
                    i == n - 1 or grid[i + 1][j] == 0,
                    j == 0 or row[j - 1] == 0,
                )
                perimeter += sum(boundaries)

    return perimeter
