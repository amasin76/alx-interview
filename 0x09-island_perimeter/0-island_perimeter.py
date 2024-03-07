#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    This function calculates the perimeter of the island in the grid.

    Args:
        grid: A list of lists of integers representing the grid.
            0 represents water, 1 represents land.

    Returns:
        The perimeter of the island in the grid.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check for neighbors that are water (part of the perimeter)
                perimeter += 4  # Assume all sides are water initially
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Not water on top
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Not water on left

    return perimeter
