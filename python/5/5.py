"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
List:
    Basically all primes between 1 and 20; any non-prime numbers
    would result in pointless calculations in time (and space, although
    space isn't necessarily a concern here).
"""

list = [7, 11, 13, 14, 16, 17, 18, 19, 20]

for x in xrange(20, 999999999, 20):
    if all(x % n == 0 for n in list):
        print x
        quit()