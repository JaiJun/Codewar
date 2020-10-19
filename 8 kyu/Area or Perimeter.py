"""
    You are given the length and width of a 4-sided polygon.

    The polygon can either be a rectangle or a square.

    If it is a square, return its area. If it is a rectangle, return its perimeter.

    I think best solution:
        def area_or_perimeter(l, w):
            return l * w if l == w else (l + w) * 2

    https://www.codewars.com/kata/5ab6538b379d20ad880000ab
"""


def area_or_perimeter(l, w):
    # return your answer
    if l == w:
        return l * w
    else:
        return l * 2 + w * 2


if __name__ == '__main__':
    length = 6
    width = 10
    area_or_perimeter(length, width)
