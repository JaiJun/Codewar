"""
    Your task is to remove all consecutive duplicate words from string, leaving only first words entries.

    Example:

    Input:

    'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

    Output:

    'alpha beta gamma delta alpha beta gamma delta'


    I think best solution:
        def remove_consecutive_duplicates(s):
            x = y = ''
            z = 0
            for pal in s.split():
                z += 1
                if not x == pal:
                    y += pal
                    if len(s.split()) > z:
                        y += " "
                x = pal
            return y

    https://www.codewars.com/kata/5b39e91ee7a2c103300018b3
"""


def remove_consecutive_duplicates(s):
    splitstr = s.split(" ")
    newstr = []
    end = splitstr[-1]
    for i in range(len(splitstr) - 1):
        if splitstr[i] == splitstr[i + 1]:
            print("Same")
        else:
            newstr.append(splitstr[i])

    newstr.append(end)
    Result = ' '.join(newstr)

    return Result


if __name__ == '__main__':
    input = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
    remove_consecutive_duplicates(input)
