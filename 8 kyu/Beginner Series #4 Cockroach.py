"""
    The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

    For example:

    cockroach_speed(1.08) == 30

    I think best solution:
        def cockroach_speed(s):
            cm_per_km = 100000
            sec_per_hour = 3600
            return int(s * cm_per_km / sec_per_hour)

    https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6
"""


def cockroach_speed(s):
    cm_per_second = s * (10 ** 5) // 3600
    print(cm_per_second)
    return cm_per_second


if __name__ == '__main__':
    input = 3.5546207219389316
    cockroach_speed(input)
