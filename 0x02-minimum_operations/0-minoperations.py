#!/usr/bin/python3
'''calculate min number of operations'''


def minOperations(n):
    '''fewest number of operations to result in n H characters in file
    given copy All and paste functionalities only'''
    if (n <= 0):
        return 0
    if (n == 1):
        return 0  # no operations needed

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1

    return operations
