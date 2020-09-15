"""
    Description:
        For a given string s find the character c (or C) with longest consecutive repetition and return:

        (c, l)
        where l (or L) is the length of the repetition.

        If there are two or more characters with the same l return the first in order of appearance.

        For empty string return:

        ('', 0)

    I think best solution:
        def longest_repetition(chars):
            max_char, max_count = '', 0
            char, count = '', 0
            for c in chars:
                if c != char:
                    count, char = 0, c
                count += 1
                if count > max_count:
                    max_char, max_count = char, count
            return max_char, max_count

    https://www.codewars.com/kata/586d6cefbcc21eed7a001155/python
"""

def longest_repetition(chars=None):
    n = len(chars)
    print(n)
    count = 0
    if chars == None or chars == "":
        print(" ", count)
        return ("", count)
    else:
        for i in range(n):
            # print(chars[i])
            repeatvalue = 1
            for j in range(i + 1, n):
                # print(chars[j])
                if chars[j] != chars[i]:
                    break
                repeatvalue += 1
            if repeatvalue > count:
                count = repeatvalue
                res = chars[i]
        print(res, count)
        return (res, count)

if __name__ == '__main__':
    input = "bbbaaabaaaa"
    print(longest_repetition(input))