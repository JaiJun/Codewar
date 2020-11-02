"""
    In this Kata you are expected to find the coefficients of quadratic equation of the given two roots (x1 and x2).

    Equation will be the form of ax^2 + bx + c = 0

    Return type is a Vector (tuple in Rust, Array in Ruby) containing coefficients of the equations in the order (a, b, c).

    Since there are infinitely many solutions to this problem, we fix a = 1.

    Remember, the roots can be written like (x-x1) * (x-x2) = 0

    I think best solution:
        def quadratic(x1, x2):
            return (1,-x1-x2,x1*x2)

    https://www.codewars.com/kata/5d59576768ba810001f1f8d6
"""


def quadratic(x1, x2):
    x = 1
    # (x - x1) * (x - x2)
    num_1 = x * x
    num_2 = -(x1 + x2)
    num_3 = x1 * x2
    Result = (num_1, num_2, num_3)
    return Result


if __name__ == '__main__':
    x1 = 4
    x2 = 9
    quadratic(x1, x2)
