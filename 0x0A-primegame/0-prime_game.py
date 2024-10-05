#!/usr/bin/python3
"""
Function to define isWineer function, resolve the Prime Game problem
"""


def primes(n):
    """Function return prime numbers between 1 and n inclusive
       Args:
        n (int): indicates upper boundary of range.
        while lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Function to determine the winner of Prime Game
    Args:
        x (int): number of game rounds
        nums (int): indicates upper limit of range for each round
    Return:
        Name of winner or None if no winner is found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
