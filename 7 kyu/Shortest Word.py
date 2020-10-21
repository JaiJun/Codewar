"""
    Simple, given a string of words, return the length of the shortest word(s).

    String will never be empty and you do not need to account for different data types.

    I think best solution:
        def find_short(s):
            return min(len(x) for x in s.split())

    https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
"""


def find_short(s):
    Result = []
    for i in s.split(' '):
        Result.append(len(i))
    print(min(Result))

    return min(Result)


if __name__ == '__main__':
    input = "bitcoin take over the world maybe who knows perhaps"
    find_short(input)
