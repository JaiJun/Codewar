"""
    Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

    Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

    Examples
     123 ->  321
    -456 -> -654
    1000 ->    1

     I think best solution:
        def reverseNumber(n):
        if n >= 0:
            return int(str(n)[::-1])
        else:
            return int(str(n).strip('-')[::-1])*-1
"""


def reverse_number(n):
    rev_number = 0
    if n < 0:
        n = n * -1
        while (n > 0):
            remainder = n % 10
            rev_number = (rev_number * 10) + remainder
            n = n // 10
        return (rev_number * -1)
    else:
        while (n > 0):
            remainder = n % 10
            rev_number = (rev_number * 10) + remainder
            n = n // 10
        return rev_number

    print("The reverse number is : {}".format(rev_number))


if __name__ == '__main__':
    input = 321
    reverse_number(input)
