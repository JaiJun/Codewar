"""
    Impliment the reverse function, which takes in input n and reverses it.

    For instance, reverse(123) should return 321.

    You should do this without converting the inputted number into a string.


    I think best solution:
        def reverse(n):
            m = 0
            while n > 0:
                n, m = n // 10, m * 10 + n % 10
            return m

    https://www.codewars.com/kata/58069e4cf3c13ef3a6000168
"""


def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    reverse_number = 0
    while (n > 0):
        print("Now number>", n)
        remainder = n % 10
        test_num = (reverse_number * 10) + remainder
        n = n // 10

    print(reverse_number)
    return reverse_number

if __name__ == '__main__':
    input = 1234
    reverse(input)
