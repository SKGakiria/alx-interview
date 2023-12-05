#!/usr/bin/python3
"""The Prime Game module"""


def primes(n):
    """Return list of prime numbers"""
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    prime_nums = []

    for num in range(2, int(n**0.5) + 1):
        if prime[num]:
            prime_nums.append(num)
            for i in range(num * num, n + 1, num):
                prime[i] = False

    for num in range(int(n**0.5) + 1, n + 1):
        if prime[num]:
            prime_nums.append(num)

    return prime_nums


def isWinner(x, nums):
    """Determines the winner of a prime game session"""
    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria = Ben = 0
    for n in nums:
        prime_nums = primes(n)
        if len(prime_nums) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
