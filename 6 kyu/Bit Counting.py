"""
    Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

    You can guarantee that input is non-negative.

    Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

    I think best solution:
        def countBits(n):
            return bin(n).count("1")
"""


def count_bits(n):
    count = 0
    # binary method
    bin_number = "{0:b}".format(n)
    for i in bin_number:
        if i == "1":
            count += 1
    return count


if __name__ == '__main__':
    number = 4
    count_bits(number)
