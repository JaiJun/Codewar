import calendar
import datetime


# import time
def solve(a, b):
    # start = time.time()
    Result = []
    number = 1
    year_range = range(a, b + 1)
    for year in year_range:
        for month in range(1, 13):
            date = datetime.date(year, month, 1)
            if date.strftime("%A") == "Friday":
                month = date.strftime("%m")
                day = calendar.monthrange(year, int(month))[1]
                FirstDate = datetime.date(year, int(month), 1)
                LastDate = datetime.date(year, int(month), day)
                if FirstDate.strftime("%A") == "Friday" and LastDate.strftime("%A") == "Sunday":
                    print(FirstDate.strftime("%b"), LastDate.strftime("%a"))
                    Result.append(date.strftime("%b"))
    print((Result[0], Result[-1], len(Result)))
    return (Result[0], Result[-1], len(Result))


if __name__ == '__main__':
    a = 2016
    b = 2020
    print(solve(a, b))