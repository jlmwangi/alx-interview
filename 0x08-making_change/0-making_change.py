#!/usr/bin/python3
'''determine fewest no of coins needed to meet a given amount'''


def makeChange(coins, total):
    """return fewest coins needed to make total"""
    count = 0
    if total <= 0:
        return 0

    # sort coins in descending order to use larger coins first
    coins.sort(reverse=True)

    for coin in coins:
        #  use as many coins of this denomination as possible
        if total >= coin:
            count += total // coin  # count no of coins of this type
            total %= coin  # remaining total after using the coins

        # if total becomes 0, no more coins needed
        if total == 0:
            return count

    # return -1 if we exit loop and total still not equal to zero
    return -1
