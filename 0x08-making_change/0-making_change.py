#!/usr/bin/python3
"""Change making"""


def makeChange(coins, total):
    # Initialize the dp table
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build the dp table
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
