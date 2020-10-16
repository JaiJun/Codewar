"""
    Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

    Write a function which takes a list of strings and returns each line prepended by the correct number.

    The numbering starts at 1. The format is n: string. Notice the colon and space in between.

    Examples:

    number([]) # => []
    number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]


    Online solutions:
    Use enumerate function
    def number(lines):
        result = ['%d: %s' % v for v in enumerate(lines, 1)]
        print(result)
    return result
"""

def number(lines):
    strnumber =[]
    print(len(lines))
    for i in range(len(lines)):
        strinfro = str(i+1) +': '+str(lines[i])
        strnumber.append(strinfro)
    print(strnumber)

    return result


if __name__=='__main__':
    input = ["a", "b", "c"]
    number(input)