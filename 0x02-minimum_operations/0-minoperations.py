#!/usr/bin/env python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    if n <= 1:
        return 0

    # Initialize number of operations
    operations = 0

    # Initialize divisor
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations
