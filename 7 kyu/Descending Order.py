"""
    Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

    Examples:
        Input: 42145 Output: 54421

        Input: 145263 Output: 654321

        Input: 123456789 Output: 987654321

    I think best solution:
        def Descending_Order(num):
            return int("".join(sorted(str(num), reverse=True)))

    https://www.codewars.com/kata/5467e4d82edf8bbf40000155

"""


def descending_order(num):
    n_number = []
    s_number = []
    for ele in str(num):
        n_number.append(int(ele))
    for s in sorted(n_number, reverse=True):
        s_number.append(str(s))
    Result = int(''.join(s_number))
    print(Result)
    return Result

    # Bust a move right here


if __name__ == '__main__':
    input = 123456789
    descending_order(input)
