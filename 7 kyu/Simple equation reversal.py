"""
Given a mathematical equation that has *,+,-,/, reverse it as follows:

    solve("100*b/y") = "y/b*100"
    solve("a+b-c/d*30") = "30*d/c-b+a"

More examples in test cases.
"""
import re
def solve(eq):
    Newstr=""
    print("The original str : " +eq)
    for i in eq:
        Newstr = eq.replace("+",",+,")
        Newstr = Newstr.replace("-", ",-,")
        Newstr = Newstr.replace("*", ",*,")
        Newstr = Newstr.replace("/", ",/,")
        print(Newstr)
    listvalue=Newstr.split(",")
    listvalue.reverse()
    separator=""
    Result =separator.join(listvalue)
    print(Result)
    return Result
if __name__=='__main__':
    value ="a+b-c/d*30"
    solve(value)