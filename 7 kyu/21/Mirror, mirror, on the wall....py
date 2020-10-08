"""
    Too long, didn't read
    You get a list of integers, and you have to write a function mirror that returns the 'mirrored' (or symmetric) version of this list,
    i.e. the middle element is the greatest, then the next greatest on both sides,
    the the next greatest, and so on...

    More info
    The list will always consist of integers in range < -1000, 1000 > and will vary in size between 0 and 10000.
    Your function should not mutate the input array, and this will be tested ( where applicable ).
    Notice that the returned list will always be of odd size,
    since there will always be a definitive middle element.

    I think best solution:
        def mirror(data: list) -> list:
        arr = sorted(data)
        return arr + arr[-2::-1]

    https://www.codewars.com/kata/5f55ecd770692e001484af7d
"""


def mirror(data: list) -> list:
    left_number = sorted(data, reverse=True)
    right_number =  sorted(data)

    print(left_number, right_number)

if __name__ == '__main__':
    input = ([-8, 42, 18, 0, -16])
    mirror(input)