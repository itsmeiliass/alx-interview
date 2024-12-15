#!/usr/bin/python3
"""
Prime Game Module: Defines function that determines the winner after a certain
number of rounds of playing the Prime Game.
"""


def isWinner(x, nums):
    """Determine the winner of each round of the Prime Game."""
    if not nums or x < 1:
        return None

    def sieve_of_eratosthenes(n):
        """Generate a list of prime numbers up to n using the Sieve of Eratosthenes."""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(n + 1) if sieve[i]]

    def count_primes_up_to(n):
        """Precompute the number of primes up to each number from 1 to n."""
        primes = sieve_of_eratosthenes(n)
        prime_count = [0] * (n + 1)
        count = 0
        for i in range(1, n + 1):
            if i in primes:
                count += 1
            prime_count[i] = count
        return prime_count

    max_n = max(nums)
    prime_count = count_primes_up_to(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:  # Maria wins if the count of primes is odd
            maria_wins += 1
        else:  # Ben wins if the count of primes is even
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
