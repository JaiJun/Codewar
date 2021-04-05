"""
    The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

    max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # should be 6: [4, -1, 2, 1]

    Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.

    If the list is made up of only negative numbers, return 0 instead.

    Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

    I think best solution:
        def maxSequence(arr):
            max,curr=0,0
            for x in arr:
                curr+=x
                if curr<0:curr=0
                if curr>max:max=curr
            return max
"""


def max_sequence(arr):
    length = len(arr)
    if length == 0: return 0
    res = arr[0]
    now = arr[0]
    for i in range(1, length):
        if now > 0:
            now += arr[i]
        else:
            now = arr[i]

        if now > res:
            res = now
    if res < 0:
        return 0
    else:
        return res

if __name__ == '__main__':
    # input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    input = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
    max_sequence(input)

