"""
    The rgb function is incomplete.

    Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.

    Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

    Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

    The following are examples of expected output values:
        rgb(255, 255, 255) # returns FFFFFF
        rgb(255, 255, 300) # returns FFFFFF
        rgb(0,0,0) # returns 000000
        rgb(148, 0, 211) # returns 9400D3


    I think best solution:
        def rgb(r, g, b):
            round = lambda x: min(255, max(x, 0))
            return ("{:02X}" * 3).format(round(r), round(g), round(b))
"""


def rgb(r, g, b):
    # your code here :)
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    hex = '#%02x%02x%02x' % (r, g, b)
    Result = hex[1:].upper()
    return Result


if __name__ == '__main__':
    r = -20
    g = 275
    b = 125

    rgb(r, g, b)
