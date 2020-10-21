"""
    Create a function that checks if a number n is divisible by two numbers x AND y.

    All inputs are positive, non-zero digits.

    I think best solution:
        def is_divisible(n,x,y):
            return n % x == 0 and n % y == 0

    https://www.codewars.com/kata/5545f109004975ea66000086
"""


def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        print("True")
        return True
    else:
        print("False")

        return False


if __name__ == '__main__':
    n = 3
    x = 1
    y = 3
    is_divisible(n, x, y)
