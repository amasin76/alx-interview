#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists of integers representing Pascal's
        triangle up to n rows. Returns an empty list if n <= 0.
    """
    triangle = []
    for i in range(n):
        # Start with a row of all zeros
        row = [0 for _ in range(i + 1)]
        # The first and last elements of each row are always 1
        row[0], row[-1] = 1, 1
        # Each interior element is the sum of the two elements above it
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
