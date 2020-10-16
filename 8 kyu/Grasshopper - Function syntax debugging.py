"""
    Grasshopper - Function syntax debugging

    A student was working on a function and made some syntax mistakes while coding.

    Help them find their mistakes and fix them.

    I think best solution:
        def main(verb, noun):
            return verb + noun

    https://www.codewars.com/kata/56dae9dc54c0acd29d00109a
"""


def main(verb, noun):
    print(verb + noun)
    return verb + noun


if __name__ == '__main__':
    input_1 = 'take '
    input_2 = 'item'
    main(input_1, input_2)
