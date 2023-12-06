#!/usr/bin/python3
"""The Prime Game module"""


def isWinner(x, nums):
    """Determines the winner of a prime game session"""
    if x < 1 or not nums:
        return None

    Maria, Ben = 0, 0

    def sieve(n):
        """Return list of prime numbers"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for num in range(2, int(n**0.5) + 1):
            if is_prime[num]:
                for multiple in range(num * num, n + 1, num):
                    is_prime[multiple] = False

        return is_prime

    for round_limit in nums[:x]:
        primes = sieve(round_limit)
        primes_count = sum(1 for prime in primes if prime)
        Ben += primes_count % 2 == 0
        Maria += primes_count % 2 == 1

    if Maria == Ben:
        return None
    return 'Maria' if Maria > Ben else 'Ben'
