"""
    Complete the square sum function so that it squares each number passed into it and then sums the results together.

    For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9

    I think best solution:
        def square_sum(numbers):
            return sum(x ** 2 for x in numbers)

    https://www.codewars.com/kata/515e271a311df0350d00000f
"""

def square_sum(numbers):
    Result=0
    for ele in numbers:
        Result+= ele *ele
    return Result
    #your code here
if __name__ == '__main__':
    input = [0, 3, 4, 5]
    square_sum(input)