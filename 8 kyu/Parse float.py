"""
    Write function parse_float which takes a string/list and returns a number or 'none'

    if conversion is not possible

    I think best solution:
        def parse_float(string):
            try:
                return float(string)
            except:
                return None

    https://www.codewars.com/kata/57a386117cb1f31890000039
"""


def parse_float(string):
    if isinstance(string, list):
        return None
    else:
        try:
            a = float(string)
        except (TypeError, ValueError):
            return None
        else:
            return a


if __name__ == '__main__':
    input = ['5', '8', '7', '.', '9', '7', '7']
    parse_float(input)