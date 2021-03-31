"""
    Write a function, persistence,

    that takes in a positive parameter num and returns its multiplicative persistence,

    which is the number of times you must multiply the digits in num until you reach a single digit

    I think best solution:
        import operator
        def persistence(n):
            i = 0
            while n>=10:
                n=reduce(operator.mul,[int(x) for x in str(n)],1)
                i+=1
            return i
"""


def persistence(n):
    number = list(str(n))
    length = len(number)
    count = 0
    while length > 1:
        total = 1
        for i in number:
            total = total * int(i)
        print(total)
        length = len(list(str(total)))
        number = list(str(total))
        count+=1
    return count



if __name__ == '__main__':
    number = 999
    persistence(number)
