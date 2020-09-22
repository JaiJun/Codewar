"""
    pairs([1,2,5,8,-4,-3,7,6,5]) = 3
    The pairs are selected as follows [(1,2),(5,8),(-4,-3),(7,6),5]
    --the first pair is (1,2) and the numbers in the pair are consecutive; Count = 1
    --the second pair is (5,8) and are not consecutive
    --the third pair is (-4,-3), consecutive. Count = 2
    --the fourth pair is (7,6), also consecutive. Count = 3.
    --the last digit has no pair, so we ignore.

    I think best solution:
        def pairs(ar):
            count = 0
            for i in range(0, len(ar), 2):
                try:
                    a, b = ar[i], ar[i+1]
                except IndexError:
                    return count

                if abs(a-b) == 1:
                    count +=1

            return count

    https://www.codewars.com/kata/5a3e1319b6486ac96f000049/python
"""


def pairs(ar):
    length = len(ar)
    n = 2
    Count = 0
    print("List Length>", length, (length + n - 1))
    for i in range((length + n - 1) // n):
        # print(ar[i *n: (i+1)*n])
        final = ar[i * n: (i + 1) * n]
        sorted_List = sorted(final)
        range_list = list(range(min(final), max(final) + 1))
        if len(final) > 1:
            if sorted_List == range_list:
                print(sorted_List, range_list)
                Count += 1
            else:
                print("SubList has no consecutive numbers.")
        else:
            print("SubList has no two numbers.")
    print(Count)
    return Count


if __name__ == '__main__':
    input = [1, 2, 5, 8, -4, -3, 7, 6, 5]
    pairs(input)
