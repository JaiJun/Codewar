"""
    Following on from Part 1, part 2 looks at some more complicated array contents.

    So let's try filling an array with...

    ...square numbers
    The numbers from 1 to n*n

    const squares = n => ???
    squares(5) // [1, 4, 9, 16, 25]
    ...a range of numbers
    A range of numbers starting from start and increasing by step

    const range = (n, start, step) => ???
    range(6, 3, 2) // [3, 5, 7, 9, 11, 13]
    ...random numbers
    A bunch of random integers between min and max

    const random = (n, min, max) => ???
    random(4, 5, 10) // [5, 9, 10, 7]
    ...prime numbers
    All primes starting from 2 (obviously)...

    const primes = n => ???
    primes(6) // [2, 3, 5, 7, 11, 13]

    I think best solution:
        from itertools import accumulate
        from gmpy2 import next_prime
        from random import sample

        def squares(n):
            return [x**2 for x in range(1, n+1)]

        def num_range(n, start, step):
            return list(range(start, start+n*step, step))

        def rand_range(n, mn, mx):
            return sample(range(mn, mx+1), n)

        def primes(n):
            return list(accumulate(range(2, n+2), func=lambda p,_:next_prime(p)))

    https://www.codewars.com/kata/571e9af407363dbf5700067c/python
"""


import random
def squares(n):
    Result=[]
    for i in range(1, n+1):
        # print(i*i)
        Result.append(i*i)
    print("Squares>", Result)
    return Result

def num_range(n, start, step):
    Result = []
    for i in range(n):
        Result.append(start)
        start+=step

    print("Num_range>", Result)
    return Result

def rand_range(n, min, max):
    Result = []
    for i in range(0, n):
        value =random.randint(min, max)
        print(value)
        Result.append(value)
    print(Result)
    return Result


def primes(n):
    Result = []
    for num in range(2, 1000):
        prime =True
        for i in range(2, num):
            if (num % i ==0):
                prime =False
        if prime:
            Result.append(num)
    print(len(Result),Result [:n])
    return Result

if __name__ == '__main__':
    squaresnumber = 5

    start = 3
    step = 2
    num_n = 10

    min = 5
    max = 10
    random_n =4

    primes_n = 26

    squares(squaresnumber)
    num_range(num_n, start, max)
    rand_range(random_n, min, max)
    primes(primes_n)