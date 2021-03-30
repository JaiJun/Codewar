"""
    This time no story, no theory.
    The examples below show you how to write function accum:

    Examples:

    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"

    I think best solution:
        def accum(s):
            return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
"""


def accum(s):
    # your code
    legnth = len(s)
    print(legnth)
    finish = []
    for i in range(legnth):
        m = (s[i] * (i + 1)).capitalize()
        finish.append(m)
    Res = '-'.join(finish)

    return Res


if __name__ == '__main__':
    name = "abcd"
    accum(name)
