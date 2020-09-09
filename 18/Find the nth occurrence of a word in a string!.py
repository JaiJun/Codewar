"""
    You are required to implement a function find_nth_occurrence that returns the index of the nth occurrence of a substring within a string (considering that those substring could overlap each others).
    If there are less than n occurrences of the substring, return -1.

    Example:
        string = "This is an example. Return the nth occurrence of example in this example string."
        find_nth_occurrence("example", string, 1) == 11
        find_nth_occurrence("example", string, 2) == 49
        find_nth_occurrence("example", string, 3) == 65
        find_nth_occurrence("example", string, 4) == -1

    Multiple occurrences of a substring are allowed to overlap, e.g.

        find_nth_occurrence("TestTest", "TestTestTestTest", 1) == 0
        find_nth_occurrence("TestTest", "TestTestTestTest", 2) == 4
        find_nth_occurrence("TestTest", "TestTestTestTest", 3) == 8
        find_nth_occurrence("TestTest", "TestTestTestTest", 4) == -1

    key Fuction : str.find() or import re
    I think best solution:
        def find_nth_occurrence(substring, string, occurrence=1):
            idx = -1
            for i in range(occurrence):
                print(i)
                idx = string.find(substring, idx + 1)
                print(idx)
                if idx == -1: return -1
            return idx

    https://www.codewars.com/kata/5b1d1812b6989d61bd00004f/solutions/python
"""
def find_nth_occurrence(substring, string, occurrence=1):
    index = 0
    count = 0
    Frequency = []
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        else:
            print("{} found at {}".format(substring, index))
            Frequency.append(index)
            index += 1
            count += 1
    print(count)
    print(Frequency)
    if len(Frequency) >= occurrence:
        Result = Frequency[occurrence - 1]
    else:
        Result = -1
    return Result
if __name__=='__main__':
    input = "This is an example. Return the nth occurrence of example in this example string."
    print(find_nth_occurrence("example", input,3))
