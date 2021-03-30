"""
    Check to see if a string has the same amount of 'x's and 'o's.

    The method must return a boolean and be case insensitive.

    The string can contain any char.

    Examples input/output:

        XO("ooxx") => true
        XO("xooxx") => false
        XO("ooxXm") => true
        XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
        XO("zzoo") => false

        I think best solution:
            def xo(s):
                s = s.lower()
                return s.count('x') == s.count('o')
"""


def xo(s):
    s = s.lower()
    n = 0
    m = 0
    ele = list(s)
    for i in ele:
        if i == "o":
            n += 1
        elif i == "x":
            m += 1
    print(n, m)
    if n == m:
        return True
    else:
        return False


if __name__ == '__main__':
    n = "xxxoo"
    xo(n)
