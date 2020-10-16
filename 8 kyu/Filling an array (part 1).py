"""
    Description:
    We want an array, but not just any old array, an array with contents!

    Write a function that produces an array with the numbers 0 to N-1 in it.

    For example, the following code will result in an array containing the numbers 0 to 4:

    arr(5) // => [0,1,2,3,4]

    I think best solution:
        def arr(n=0):
            return list(range(n))

    https://www.codewars.com/kata/571d42206414b103dc0006a1/solutions/python
"""


def arr(n=None):
    Result = []
    if n == None or n==0:
        return []
    else:
        for i in range(0, n, 1):
            Result.append(i)
        print(Result)
        return Result
if __name__ == '__main__':
    input =5
    arr(input)