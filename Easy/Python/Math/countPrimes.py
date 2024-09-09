# Given an integer n, return the number of prime numbers that are strictly less than n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 106



class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        # Step 1: Create a boolean list is_prime[] of size n and initialize all as True
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # We know 0 and 1 are not prime numbers
        
        # Step 2: Use the Sieve of Eratosthenes algorithm
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as False (i.e., non-prime)
                for multiple in range(i * i, n, i):
                    is_prime[multiple] = False
        
        # Step 3: Count the number of primes by summing the True values in is_prime[]
        return sum(is_prime)