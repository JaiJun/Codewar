"""
    I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements.

    I'll appreciate for your help.

    P.S. Each array includes only integer numbers.

    Output is a number too.

    https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
"""
def array_plus_array(arr1,arr2):
    Result = sum(arr1) +sum(arr2)
    return Result

if __name__ == '__main__':
    number_1 = [1, 2, 3]
    number_2 = [4, 5, 6]

    array_plus_array(number_1, number_2)