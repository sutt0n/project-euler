# coding=utf-8
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
a, b, found, palindromes = 100, 999, False, []

while a <= 999:

    b = 999

    while b >= 100:
        _str = str(a * b)
        _rev = str(a * b)[::-1]

        if _str == _rev:
            palindromes.append(a * b)

        b -= 1

    a += 1

#print palindromes
print max(palindromes)