"""
    In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

    For example:

    dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].

    dup(["kelless","keenness"]) = ["keles","kenes"].

    Strings will be lowercase only, no spaces. See test cases for more examples.

    Good luck!

    I think best solution:
        from itertools import groupby
        def dup(arry):
            word =""
            Result=[]
            for i in arry:
                for c, grouper in groupby(i):
                    print(c)
                    word +=c
                    print(word)
                Result.append(word)
                word=""
            print(Result)
            return Result
            # return ["".join(c for c, grouper in groupby(i)) for i in arry]

    https://www.codewars.com/kata/59f08f89a5e129c543000069/python
"""
def dup(arry):
    Combineword=[]
    Result =[]
    for word in arry:
        j= 0
        char = list(word)
        print(char)
        for i in range(len(char)):
            print(i)
            if char[j] != char[i]:
                print(j,char[j], i,char[i])
                j+=1
                char[j] =char[i]

        j += 1
        char = char[:j]
        Combineword.append(char)
    for i in range (len(Combineword)):
        print(Combineword[i])
        CB = "".join(Combineword[i])
        Result.append(CB)
    print(Result)
    return Result
if __name__ == '__main__':
    input =["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]
    ouput =['codewars','picaniny','hubububo']
    print(dup(input))
