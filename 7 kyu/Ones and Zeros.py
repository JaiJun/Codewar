"""
    Given an array of ones and zeroes, convert the equivalent binary value to an integer.

    Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

    However, the arrays can have varying lengths, not just limited to 4.

    I think best solution:
        def binary_array_to_number(arr):
            return int("".join(map(str, arr)), 2)

    https://www.codewars.com/kata/578553c3a1b8d5c40300037c

    Reference:
        https://thecodingbot.com/convert-a-binary-numberbase-2-to-the-integerbase-10-in-python/
"""


def binary_array_to_number(arr):
    Result = ""
    for i in arr:
        Result += str(i)
    res = int(Result, 2)
    return res


if __name__ == '__main__':
    input = [1, 1, 1, 1]
    binary_array_to_number(input)
