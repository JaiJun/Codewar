"""
    Write a function to convert a name into initials.

    This kata strictly takes two words with one space in between them.

    The output should be two capital letters with a dot separating them.

    It should look like this:

    Sam Harris => S.H

    Patrick Feeney => P.F

    I think best solution:
        def abbrevName(name):
            first, last = name.upper().split(' ')
            return first[0] + '.' + last[0]

    https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
"""
def abbrev_name(name):
    Result = name.split(" ")

    return str.upper(Result[0][0] +"." + Result[1][0])

if __name__ == '__main__':
    input ="Sam Harris"
    abbrev_name(input)