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
"""
def solve(a,b):
    if "*" in a:
        print("a>", a)
        print("b>", b)
        replasestr = ""
        for i in range(len(b)):

            # print(a.replace('*', replasestr))
            print(b[i:])

    else:
        if len(a) == len(b):
            print("Not Contain * >", True)
            return True
        else:
            print("Not Contain * >", False)
            return False



    pass

if __name__ == '__main__':
    a = "aa*"
    b = "aaa"
    solve(a,b)