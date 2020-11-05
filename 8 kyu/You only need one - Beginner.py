"""
    You will be given an array a and a value x.

    All you need to do is check whether the provided array contains the value.

    Array can contain numbers or strings. X can be either.

    Return true if the array contains the value, false if not.

    I think best solution:
        def check(seq, elem):
            return elem in seq

    https://www.codewars.com/kata/57cc975ed542d3148f00015b
"""
def check(seq, elem):
    if elem in seq:
        print(True)
        return True
    else:
        print(False)
        return False

if __name__ == '__main__':
    seq = [66, 101]
    elem = 66
    check(seq, elem)