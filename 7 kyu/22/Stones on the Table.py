"""
    There are some stones on Bob's table in a row, and each of them can be red, green or blue,
    indicated by the characters R, G, and B.

    Help Bob find the minimum number of stones he needs to remove from the table so that the stones in each pair of adjacent stones have different colours.

    I think best solution:
        def solution(stones):
            st=[1 for i in range(1,len(s)) if s[i-1]==s[i]]
            return sum(st)

    https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a/python


    Reference:
        https://liuxveyang.github.io/posts/cf266-a.-stones-on-the-table/
"""


def solution(stones):
    count = 0
    print(list(stones))
    for i in range(0, len(stones)):
       print(stones[i])
       if i == len(stones)-1:
            print("Full")
       elif stones[i] == stones[i+1]:
            count+=1
    print(count)
    return count

if __name__ == '__main__':
    input = "RGGRGBBRGRR"
    solution(input)