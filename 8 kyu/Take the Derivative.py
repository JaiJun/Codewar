"""
    This function takes two numbers as parameters, the first number being the coefficient, and the second number being the exponent.

    Your function should multiply the two numbers, and then subtract 1 from the exponent.

    Then, it has to print out an expression (like 28x^7).

    "^1" should not be truncated when exponent = 2.

    I think best solution:
        def derive(coefficient, exponent):
            return f'{coefficient * exponent}x^{exponent - 1}'

    https://www.codewars.com/kata/5963c18ecb97be020b0000a2
"""


def derive(coefficient, exponent):
    # your code here
    Result = str(coefficient * exponent) + "x^" + str(exponent - 1)
    return Result


if __name__ == '__main__':
    a = 7
    b = 8
    derive(a, b)
