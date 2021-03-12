"""
    Write a function that takes a positive integer n, sums all the cubed values from 1 to n, and returns that sum.

    Assume that the input n will always be a positive integer.

    I think best solution:
        def sum_cubes(n):
            return sum(i**3 for i in range(0,n+1))
"""


def sum_cubes(n):
    sum = 0
    for i in range(n + 1):
        sum += i ** 3
    print("Total value:", sum)
    return int(sum)


if __name__ == '__main__':
    input = 3
    sum_cubes(input)
