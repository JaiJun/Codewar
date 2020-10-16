"""
    In this Kata, you will be given a string that has lowercase letters and numbers.

    Your task is to compare the number groupings and return the largest number.

    For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.

    Good luck!

    I think best solution:
        #\d+ > 匹配1個或更多連續的數字
        a=re.findall("(\d+)", s)
        Result = max(map(int, a))
        print(Result)

    https://www.codewars.com/kata/59dd2c38f703c4ae5e000014/python
"""

import re


def solve(s):

    arr = re.split('[A-Za-z]', s)
    print(re.split('[A-Za-z]', s))
    while '' in arr:
        arr.remove('')
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    print(max(arr))
    return max(arr)


if __name__ == '__main__':
    input="gh12cdy695m1"
    solve(input)