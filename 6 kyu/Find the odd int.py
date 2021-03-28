"""
    Description:

    Given an array of integers, find the one that appears an odd number of times.
    There will always be only one integer that appears an odd number of times.

    I think best solution:
        def find_it(seq):
            for i in seq:
                if seq.count(i)%2!=0:
                    return i
"""


def find_it(seq):
    n = list(dict.fromkeys(seq))
    for i in n:
        if seq.count(i) % 2 == 0:
            pass
        else:
            m = seq.count(i)
            number = i
            print("Now number>", i)
    return number


if __name__ == '__main__':
    number = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
    find_it(number)
