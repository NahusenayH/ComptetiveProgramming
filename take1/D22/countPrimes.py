import math
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [1] * n
        for i in range(2,math.ceil(math.sqrt(n))):
            if primes[i]:
                for k in range(i * i, n, i):
                    primes[k] = 0

        return sum(primes[2:])