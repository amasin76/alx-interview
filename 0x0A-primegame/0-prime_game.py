#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with x rounds"""
    if x < 1 or not nums:
        return None
    mariasWins, bensWins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, isPrime in enumerate(primes, 1):
        if i == 1 or not isPrime:
            continue
        for y in range(i + i, n + 1, i):
            primes[y - 1] = False
    for _, n in zip(range(x), nums):
        primesCount = len(list(filter(lambda x: x, primes[0: n])))
        bensWins += primesCount % 2 == 0
        mariasWins += primesCount % 2 == 1
    if mariasWins == bensWins:
        return None
    return 'Maria' if mariasWins > bensWins else 'Ben'
