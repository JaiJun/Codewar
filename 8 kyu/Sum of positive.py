"""
    You get an array of numbers, return the sum of all of the positives ones.

    Example [1,-4,7,12] => 1 + 7 + 12 = 20

    Note: if there is nothing to sum, the sum is default to 0.

    I think best solution:
        def positive_sum(arr):
            return sum(x for x in arr if x > 0)

    https://www.codewars.com/kata/5715eaedb436cf5606000381
"""

def positive_sum(arr):
    new_nums = list(filter(lambda x: x > 0, arr))
    return sum(new_nums)



if __name__ == '__main__':
    input = [1,2,3,4,5]
    positive_sum(input)