"""
    Friday 13th or Black Friday is considered as unlucky day.

    Calculate how many unlucky days are in the given year.

    Find the number of Friday 13th in the given year.

    Input: Year as an integer.

    Output: Number of Black Fridays in the year as an integer.

    Examples:

    unluckyDays(2015) == 3
    unluckyDays(1986) == 1

    I think best solution:
        from datetime import date

        def unlucky_days(year):
            return sum(date(year, m, 13).weekday() == 4 for m in range(1, 13))

    https://www.codewars.com/kata/56eb0be52caf798c630013c0
"""
from datetime import date, timedelta


def unlucky_days(year):
    d1 = date(year, 1, 1)
    d2 = date(year, 12, 31)
    delta = d2 - d1
    count = 0
    for i in range(delta.days + 1):
        nowdate = d1 + timedelta(days=i)

        if nowdate.day == 13 and nowdate.weekday() == 4:
            print(nowdate)
            count += 1
    return count


if __name__ == '__main__':
    input = 2015
    unlucky_days(input)
