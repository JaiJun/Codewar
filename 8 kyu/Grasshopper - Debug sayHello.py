"""
    Debugging sayHello function

    The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

    Example output:

    Hello, Mr. Spock

    I think best solution:
        def say_hello(name):
            return f"Hello, {name}"

    https://www.codewars.com/kata/5625618b1fe21ab49f00001f
"""


def say_hello(name):
    return "Hello, " + name


if __name__ == '__main__':
    input = 'Mr. Spock'
    say_hello(input)
