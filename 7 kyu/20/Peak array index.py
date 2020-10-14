"""
    Given an array of ints, return the index such that the sum of the elements to the right of that index equals the sum of the elements to the left of that index.

    If there is no such index, return -1. If there is more than one such index, return the left-most index.

    For example:

    peak([1,2,3,5,3,2,1]) = 3, because the sum of the elements at indexes 0,1,2 == sum of elements at indexes 4,5,6. We don't sum index 3.
    peak([1,12,3,3,6,3,1]) = 2
    peak([10,20,30,40]) = -1

    Me Example:
        [1,12,3,3,6,3,1]
        Calculation Operating as follows:
            [] [12, 3, 3, 6, 3, 1] 0 28
            [1] [3, 3, 6, 3, 1] 1 16
            [1, 12] [3, 6, 3, 1] 13 13
            [1, 12, 3] [6, 3, 1] 16 10
            [1, 12, 3, 3] [3, 1] 19 4
            [1, 12, 3, 3, 6] [1] 25 1
            [1, 12, 3, 3, 6, 3] [] 28 0

    I think best solution:
        def peak(arr):
            for i, val in enumerate(arr):
                if sum(arr[:i]) == sum(arr[i+1:]):
                    return i
            return -1

    https://www.codewars.com/kata/5a61a846cadebf9738000076
"""


def peak(arr):
    indexnumber = 0
    for i in range(len(arr)):

        left = sum(arr[:i])
        right = sum(arr[i + 1:])
        print(arr[:i], arr[i + 1:], left, right)
        if left == right:
            # print(i)
            indexnumber = i
    if indexnumber > 0:
        return indexnumber
    else:
        return -1


if __name__ == '__main__':
    input = [1, 12, 3, 3, 6, 3, 1]
    peak(input)
