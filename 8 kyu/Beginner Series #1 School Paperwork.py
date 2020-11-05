"""
    Your classmates asked you to copy some paperwork for them.

    You know that there are 'n' classmates and the paperwork has 'm' pages.

    Your task is to calculate how many blank pages do you need.

    Example:
    paperwork(5, 5) == 25
    Note: if n < 0 or m < 0 return 0!


    I think best solution:
        def paperwork(n, m):
            return n * m if n > 0 and m > 0 else 0

    https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd
"""
def paperwork(n, m):
    print(n,m)
    if n or m < 0:

        return 0
    else:
        return n*m


if __name__ == '__main__':
    n = 5
    m = 5
    paperwork(n, m)