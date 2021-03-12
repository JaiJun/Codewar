"""
    Write a function that reverses the bits in an integer.

    For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.

    I think best solution:
        def reverse_bits(n):
            return int(bin(n)[:1:-1],2)
"""


def reverse_bits(n):
    bin_number = bin(n)[2:]
    reverse_number = bin_number[::-1]
    return int(reverse_number, 2)


if __name__ == '__main__':
    number = 417
    reverse_bits(number)
