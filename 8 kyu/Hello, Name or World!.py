"""
    Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

    Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

    Examples:

    hello "john"   => "Hello, John!"
    hello "aliCE"  => "Hello, Alice!"
    hello          => "Hello, World!" # name not given
    hello ''       => "Hello, World!" # name is an empty String

    I think best solution:
        def hello(name=''):
        #The title() method returns a string where the first character in every word is upper case.
        #Like a header, or a title.
        return f"Hello, {name.title() or 'World'}!"

    https://www.codewars.com/kata/57e3f79c9cb119374600046b
"""
def hello(name=None):
    Fistword = "Hello,"
    Result = ""
    if name == "" or name ==None:
        return "Hello, World!"
    else:
        Capitalize_name = name.capitalize()
        Result = Fistword + " " + Capitalize_name + "!"
        print(Result)
        return Result


if __name__ == '__main__':
    input ="aliCE"
    hello(input)