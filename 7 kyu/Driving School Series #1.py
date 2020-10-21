"""
    Every month, a random number of students take the driving test at Fast & Furious (F&F) Driving School.

    To pass the test, a student cannot accumulate more than 18 demerit points.

    At the end of the month, F&F wants to calculate the average demerit points accumulated by ONLY the students who have passed, rounded to the nearest integer.

    Write a function which would allow them to do so.

    If no students passed the test that month, return 'No pass scores registered.'.


    I think best solution:
        def passed(lst):
            a = list(filter(lambda x: x<=18, lst))
            return 'No pass scores registered.' if a == [] else round(sum(a)/len(a))

    https://www.codewars.com/kata/58999425006ee3f97c00011f
"""


def passed(lst):
    print(lst)
    average = []
    for i in lst:
        if i <= 18:
            average.append(i)
        else:
            print("More than 18")
    if average == []:
        print("No pass scores registered.")
        return "No pass scores registered."
    else:
        value = round(sum(average) / len(average))
        print(value)
        return value


if __name__ == '__main__':
    input = [10, 10, 10, 18, 20, 20]
    passed(input)
