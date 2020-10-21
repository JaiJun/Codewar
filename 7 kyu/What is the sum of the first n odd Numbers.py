"""
    Sum of n first numbers
        In this kata you will require to sum the first n odd numbers.

        example1:

        n = 0
        0
        example2:

        n = 3
        1+3+5

        Reference:
            https://byjus.com/maths/sum-of-odd-numbers/

    https://www.codewars.com/kata/5f8fee47d2ec88001a338410
"""


def SumOfOddNums(n):
    print(n * n)
    return n * n


if __name__ == '__main__':
    length = 1
    SumOfOddNums(length)
