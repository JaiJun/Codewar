"""
    Math hasn't always been your best subject, and these programming symbols always trip you up!

    I mean, does ** mean *"Times, Times"* or *"To the power of"*?

    Luckily, you can create the function expression_out() to write out the expressions for you!

    The operators you'll need to use are:

    { '+':   'Plus ',
      '-':   'Minus ',
      '*':   'Times ',
      '/':   'Divided By ',
      '**':  'To The Power Of ',
      '=':   'Equals ',
      '!=':  'Does Not Equal ' }
    These values will be stored in the preloaded dictionary OPERATORS just as shown above.

    But keep in mind: INVALID operators will also be tested, to which you should return "That's not an operator!"

    And all of the numbers will be 1 to10! Isn't that nice!

    Here's a few examples to clarify:

    expression_out("4 ** 9") == "Four To The Power Of Nine"
    expression_out("10 - 5") == "Ten Minus Five"
    expression_out("2 = 2")  == "Two Equals Two"

    I think best solution:
        def expression_out(exp):
            try:
                l[int(exp.split()[0])] + " " + operators[exp.split()[1]] + l[int(exp.split()[2])]
                print(l)
                return l
            except KeyError:
                print("That's not an operator!")
                return "That's not an operator!"

    https://www.codewars.com/kata/57e2afb6e108c01da000026e/python
"""


operators = {'+': 'Plus',
             '-': 'Minus',
             '*': 'Times',
             '/': 'Divided By',
             '**': 'To The Power Of',
             '=': 'Equals',
             '!=': 'Does Not Equal'}
digits = {'0': 'Zero',
          '1': 'One',
          '2': 'Two',
          '3': 'Three',
          '4': 'Four',
          '5': 'Five',
          '6': 'Six',
          '7': 'Seven',
          '8': 'Eight',
          '9': 'Nine',
          '10': 'Ten'}
check = []
l = ['0','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']




# def expression_out(exp):
#     arr = exp.split()
#     print(arr)
#     for value in arr:
#         if value in operators:
#             print("Operators")
#             check.append("Operators")
#         elif value in digits:
#             print("Digits")
#             check.append("Digits")
#         else:
#             Meg = "That's not an operator!-1"
#             print(Meg)
#             return Meg
#
#     print(check)
#     if "Operators" in check:
#         print("True")
#         for i in range(len(arr)):
#             if arr[i] in operators:
#                 print(arr[i])
#                 arr[i] = operators[arr[i]]
#
#             elif arr[i] in digits:
#                 print(arr[i])
#                 arr[i] = digits[arr[i]]
#         Result = ' '.join(arr)
#         print(Result)
#         return Result
#     else:
#         Meg = "That's not an operator!-2"
#         print(Meg)
#         return Meg
#


if __name__ == '__main__':
    input="6 1 6"
    expression_out(input)