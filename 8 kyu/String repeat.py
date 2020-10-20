"""
    Write a function called repeat_str which repeats the given string src exactly count times.

    repeatStr(6, "I") // "IIIIII"
    repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"


    https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
"""


def repeat_str(repeat, string):
    Result = string * repeat
    print(string * repeat)
    return Result


if __name__ == '__main__':
    repeat = 4
    input = "a"
    repeat_str(repeat, input)
