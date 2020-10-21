"""
    Given a string of digits,

    you should replace any digit below 5 with '0' and any digit 5 and above with '1'.

    Return the resulting string.

    I think best solution:
        def fake_bin(x):
            return ''.join('0' if c < '5' else '1' for c in x)

    https://www.codewars.com/kata/57eae65a4321032ce000002d
"""
def fake_bin(x):
    Result =""
    for i in x:
        if int(i)>=5:
            Result+="1"
        else:
            Result+="0"
    print(Result)

    return Result


if __name__ == '__main__':
    input = "45385593107843568"
    fake_bin(input)