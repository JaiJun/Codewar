"""
    Task:

    In this kata you will be given a list consisting of unique elements except for one thing that appears twice.

    Your task is to output a list of everything inbetween both occurrences of this element in the list.

    I think best solution:
        def duplicate_sandwich(arr):
            start, end = [i for i, x in enumerate(arr) if arr.count(x) > 1]
            return arr[start+1:end]

    https://www.codewars.com/kata/5f8a15c06dbd530016be0c19
"""


def duplicate_sandwich(arr):
    print("Orignal>", arr)
    start = 0
    end = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                start = i
                end = j
    print(arr[start + 1:end])
    Result = arr[start + 1:end]

    return Result


if __name__ == '__main__':
    input = ['None', 'Hello', 'Example', 'hello', 'None', 'Extra']
    duplicate_sandwich(input)
