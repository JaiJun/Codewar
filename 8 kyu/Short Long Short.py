"""
    Given 2 strings, a and b, return a string of the form short+long+short,

    with the shorter string on the outside and the longer string on the inside.

    The strings will not be the same length, but they may be empty ( length 0 ).

    I think best solution:
        def solution(a, b):
            return a+b+a if len(a)<len(b) else b+a+b

    https://www.codewars.com/kata/50654ddff44f800200000007
"""


def solution(a, b):
    if len(a) > len(b):
        Result = b + a + b
    else:
        Result = a + b + a
    print(Result)
    return Result


if __name__ == '__main__':
    a = "45"
    b = "1"
    solution(a,b)

