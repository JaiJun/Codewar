"""
    Your task is to sort a given string. Each word in the string will contain a single number.

    This number is the position the word should have in the result.

    Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

    If the input string is empty, return an empty string.

    The words in the input String will only contain valid consecutive numbers.

    I think best solution:

        def order(sentence):
        return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

    https://www.codewars.com/kata/55c45be3b2079eccff00010f/python
"""


def order(sentence):
    Result = []
    TOT = []
    for s in sentence.split():
        # print(s)
        for i in range(len(s)):
            if s[i].isdigit():
                location = int(s[i])
                Result.append('{}: {}'.format(location, s))
    Result = sorted(Result)
    Result = " ".join(Result).split(" ")
    for j in range(1, len(Result), 2):
        print(Result[j])
        TOT.append(Result[j])
    print(TOT)
    return " ".join(TOT)

if __name__ == '__main__':
    input = "4of Fo1r pe70ople g3ood th5e the2"
    binary = order(input)
