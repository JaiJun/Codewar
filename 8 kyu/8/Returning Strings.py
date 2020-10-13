"""
    Make a function that will return a greeting statement that uses an input; your program should return,

    "Hello, <name> how are you doing today?".

    SQL: return results in a column named greeting

    [Make sure you type the exact thing I wrote or the program may not execute properly]

    I think best solution:
        def greet(name):
            return "Hello, {} how are you doing today?".format(name)

    https://www.codewars.com/kata/55a70521798b14d4750000a4
"""
def greet(name):
    #Good Luck (like you need it)
    return "Hello, " + name +" how are you doing today?"

if __name__ == '__main__':
    input = "Ryan"
    greet(input)
