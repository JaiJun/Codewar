"""
    Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

    Your task is to make 'Past' function which returns time converted to milliseconds.

    Example:
        past(0, 1, 1) == 61000
        Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59

    I think best solution:
        def past(h, m, s):
            return (3600*h + 60*m + s) * 1000

    https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
"""


def past(h, m, s):
    print(h, m, s)
    R_h = h * 3600
    R_m = m * 60
    R_s = s
    Result = (R_h + R_m + R_s) * 1000
    print(Result)
    return Result


if __name__ == '__main__':
    h = 0
    m = 1
    s = 1
    past(h, m, s)
