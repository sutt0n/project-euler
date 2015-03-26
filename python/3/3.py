"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

factors, d, n = [], 2, 600851475143

while n > 2:
    while n % d == 0:
        factors.append(d)
        n /= d

    d += 1

print max(factors)