"""
    In this Kata, you will remove the left-most duplicates from a list of integers and return the result.

    # Remove the 3's at indices 0 and 3
    # followed by removing a 4 at index 1
    solve([3, 4, 4, 3, 6, 3]) # => [4, 6, 3]

    I think best solution:
        def solve(arr):
            re = []
            for i in arr[::-1]:
                if i not in re:
                    re.append(i)
            return re[::-1]
"""

def solve(arr):
    remove = list(set(arr))
    print(remove)
    duplicates = []
    print(arr)
    for k in range(len(remove)):
        print("K>", remove[k])
        for i, j in enumerate(arr):
            if j == remove[k]:
                duplicates.append(i)
                print(duplicates)
        if len(duplicates) > 1:
            for n in range(0, len(duplicates) - 1):
                arr[duplicates[n]] = ""
            duplicates = []
        else:
            duplicates = []
    while '' in arr:
        arr.remove('')
    print(arr)
    return arr
if __name__ == '__main__':
    input = [3, 4, 4, 3, 6, 3]
    solve(input)
