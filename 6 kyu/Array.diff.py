"""
    Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

    It should remove all values from list a, which are present in list b.

    array_diff([1,2],[1]) == [2]
    If a value is present in b, all of its occurrences must be removed from the other:

    array_diff([1,2,2,2,3],[2]) == [1,3]

    I think best solution:
        def array_diff(a, b):
            return [x for x in a if x not in b]
"""


def array_diff(a, b):

    if len(a) == 0 or len(b) == 0:
        return a
    else:
        for remove_n in b:
            #remove_n假設還有重複存在於a List內繼續刪除
            while remove_n in a:
                a.remove(remove_n)
        return a



if __name__ == '__main__':
    # arr = [1,2]
    # delete = [1]

    # arr = [1, 2, 3]
    # delete = [1, 2]
    arr = [1,2,2]
    delete = [2]
    array_diff(arr, delete)
