"""
    You will be given two strings a and b consisting of lower case letters,
    but a will have at most one asterix character.

    The asterix (if any) can be replaced with an arbitrary sequence (possibly empty) of lowercase letters.

    No other character of string a can be replaced.

    If it is possible to replace the asterix in a to obtain string b, then string b matches the pattern.

    If the string matches, return true else false.

    For example:

    solve("code*s","codewars") = true, because we can replace the asterix(*) with "war" to match the second string.

    solve("codewar*s","codewars") = true, because we can replace the asterix(*) with "" to match the second string.

    solve("codewars","codewars") = true, because the strings already match.
    solve("a","b") = false

    Solution key> fnmatch

    I think best solution:
        from fnmatch import fnmatch
            def solve(a, b):
                print(fnmatch(b, a))
                return fnmatch(b, a)

    https://www.codewars.com/kata/5bc052f93f43de7054000188

"""


def solve(a, b):
    if "*" in a:
        print("a>", a)
        print("b>", b)
        element = a.split('*')
        left = len(element[0])
        right = len(element[1])
        print(b[:left], b[-right:])
        if len(a.replace('*', "")) > len(b):
            print("More >b", False)
            return False
        else:
            if element[0] == b[:left] and element[1] == b[-right:]:
                print("1-True")
                return True
            elif element[0] == "" and element[1] == b[-right:]:
                print("2-True")
                return True
            elif element[1] == "" and element[0] == b[:left]:
                print("3-True")
                return True
            else:
                print("4-False")
                return False

    else:
        if len(a) == len(b):
            print("Not Contain * >", True)
            return True
        else:
            print("Not Contain * >", False)
            return False


if __name__ == '__main__':
    a = "code*warrior"
    b = "codewars"
    solve(a, b)
