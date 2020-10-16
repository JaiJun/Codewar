"""
    Summation
    Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

    For example:

    summation(2) -> 3
    1 + 2

    summation(8) -> 36
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

    I think best solution:
        def summation(num):
            return sum(range(1,num+1))

    https://www.codewars.com/kata/55d24f55d7dd296eb9000030
"""
def summation(num):
    number = 0
    for i in range(0, num+1):
        print(i)
        number +=i
    print(number)
    return number
if __name__ == '__main__':
    input = 100
    summation(input)