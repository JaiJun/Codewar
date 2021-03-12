"""
    Your job is to write a function, which takes three integers a, b, and c as arguments,
    and returns True if exactly two of of the three integers are positive numbers, and False - otherwise.


    I think best soluction:
        def two_are_positive(a, b, c):
            list = [a,b,c]
            x = 0
            for i in list:
                if i > 0:
                    x += 1
            return x == 2

"""


def two_are_positive(a, b, c):
    print("Now number>", a, b, c)
    answer = 0
    number = (a, b, c)
    for i in number:
        if i > 0:
            print("++")
            answer += 1
    if answer >= 2:
        print("All number include two positive!")
        return True
    else:
        print("All number include negative!")
        return False


if __name__ == '__main__':
    two_are_positive(-4, 6, 0)
