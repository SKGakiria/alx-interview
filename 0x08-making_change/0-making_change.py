#!/usr/bin/python3
"""The Change making module"""


def makeChange(coins, total):
    """Determines fewest number of coins needed to meet a given amount"""
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coins_count = 0
    for c in coins:
        if total % c == 0:
            coins_count += total // c
            return coins_count
        if total - c >= 0:
            if int(total / c) > 1:
                coins_count += total // c
                total = total % c
            else:
                coins_count += 1
                total -= c
                if total == 0:
                    break
    if total > 0:
        return -1
    return coins_count
