#!/usr/bin/python3
'''determine fewest no of coins needed to meet a given amount'''


def makeChange(coins, total):
    """return fewest coins needed to make total"""
    count = 0
    if total <= 0:
        return 0
    for coin in coins:
        #  base case where a value of a coin is equal to the total
        if coin == total:
            count += 1
            return count
        # if not go through each coin, looking for one whose value is greter than the rest and subtract it from total
        elif coin < total:
            total = total - coin
            count += 1
        else:
            return -1
    return count

