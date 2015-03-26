"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

a, b, _sum, limit = 1, 2, 0, 4000000

while a < limit:
    if a % 2 == 0:
        _sum += a

    a, b = b, a + b

print _sum