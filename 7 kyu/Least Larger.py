"""
    Task:

    Given an array of numbers and an index, return the index of the least number larger

    than the element at the given index, or -1 if there is no such index ( or, where applicable,

    Nothing or a similarly empty value ).

    Notes:

    Multiple correct answers may be possible. In this case, return any one of them.

    The given index will be inside the given array.

    The given array will, therefore, never be empty.

    I think best solution:
        def least_larger(a, i):
            b = [x for x in a if x>a[i]]
            return a.index(min(b)) if b else -1

    https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4
"""


def least_larger(a, i):
    compare = []
    print(a[i])
    for element in a:
        if a[i] < element:
            compare.append(element)
    compare = sorted(compare)
    if len(compare) > 0:
        location = a.index(compare[0])
        print(location)
        return location
    else:
        print("-1")
        return -1


if __name__ == '__main__':
    input = [4, 1, 3, 5, 6]
    location = 4
    least_larger(input, location)
