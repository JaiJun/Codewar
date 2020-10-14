"""
    It's the academic year's end, fateful moment of your school report.

    The averages must be calculated.

    All the students come to you and entreat you to calculate their average for them.

    Easy ! You just need to write a script.

    Return the average of the given array rounded down to its nearest integer.

    The array will never be empty.

    I think best solution:
        def get_average(marks):
            return sum(marks) // len(marks)

    https://www.codewars.com/kata/59ca8246d751df55cc00014c

"""


def get_average(marks):
    average = int(sum(marks) / len(marks))
    print(average)
    return average


if __name__ == '__main__':
    input = [1, 5, 87, 45, 8, 8]
    get_average(input)
