"""
    Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".

    tripleX("abraxxxas") → true
    tripleX("xoxotrololololololoxxx") → false
    tripleX("softX kitty, warm kitty, xxxxx") → true
    tripleX("softx kitty, warm kitty, xxxxx") → false
    Note :

    capital X's do not count as an occurrence of "x".
    if there are no "x"'s then return false

    I think best solution:
        def triple_x(s):
            try:
                return True if s.index("x")==s.index("xxx") else False
            except: return False

    https://www.codewars.com/kata/568dc69683322417eb00002c
"""


def triple_x(s):
    if 'x' not in s or s == "":
        return False
    else:
        Result = s.split('x', 1)[1]
        print(Result[:2])
        if Result[:2] == "xx":
            print(True)
            return True
        else:
            print(False)
            return False


if __name__ == '__main__':
    input = "abraxxxas"
    triple_x(input)
