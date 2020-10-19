"""
    A person's Life Path Number is calculated by adding each individual number in that person's date of birth, untill it is reduced to a single digit number.

    For example, Albert Einstein's birthday is March 14, 1879.

    The calculation of his Life Path Number would look like this:

    I think best solution:
        def life_path_number(birthdate):
            n = "".join(i for i in birthdate if i.isdigit())
            while len(str(n)) > 1:
                n = sum(i for i in map(int, str(n)))
            return n

    https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0
"""


def life_path_number(birthdate):
    number = birthdate.replace('-', '')
    print(number)
    while len(number) > 1:
        n = 0
        for i in range(len(number)):
            n += int(number[i])
        number = str(n)
    print(n)
    return n


if __name__ == '__main__':
    input = "1971-06-28"
    life_path_number(input)
