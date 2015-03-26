"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

n, i, _sum = 1000, 0, 0

while i < n:
    if i % 3 == 0:
        _sum += i
    elif i % 5 == 0:
        _sum += i

    i += 1

# sum of the integers divisible by 3 and 5 less than n
print _sum