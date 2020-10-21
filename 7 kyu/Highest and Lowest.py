"""
    In this little assignment you are given a string of space separated numbers,

    and have to return the highest and lowest number.

    Example:

    high_and_low("1 2 3 4 5")  # return "5 1"
    high_and_low("1 2 -3 4 5") # return "5 -3"
    high_and_low("1 9 3 4 -5") # return "9 -5"
    Notes:

    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first.

    I think best solution:
        def high_and_low(numbers):
            nn = [int(s) for s in numbers.split(" ")]
            return "%i %i" % (max(nn),min(nn))

    https://www.codewars.com/kata/554b4ac871d6813a03000035
"""


def high_and_low(numbers):
    Result = []
    for i in numbers.split():
        Result.append(int(i))
    Result = sorted(Result)

    return str(Result[-1]) + " " + str(Result[0])

if __name__ == '__main__':
    input = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
    high_and_low(input)
