"""
    Task
    Given three integers a ,b ,c,

    return the largest number obtained after inserting the following operators and brackets: +, *, ()

    In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

    Consider an Example :
    With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:

    1 * (2 + 3) = 5
    1 * 2 * 3 = 6
    1 + 2 * 3 = 7
    (1 + 2) * 3 = 9
    So the maximum value that you can obtain is 9.

    I think best solution:
        def expression_matter(a, b, c):
            return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))

    https://www.codewars.com/kata/5ae62fcf252e66d44d00008e

"""
def expression_matter(a, b, c):
    Result =[]
    for i in range(1, 6):
        if i == 1:
            Result.append(a * (b + c))
        elif i ==2:
            Result.append(a * b * c)
        elif i ==3:
            Result.append(a + b * c)
        elif i ==4:
            Result.append((a + b) * c)
        elif i == 5:
            Result.append(a + b + c)
    return max(Result)

if __name__ == '__main__':
    a = 2
    b = 1
    c = 2
    expression_matter(a, b, c)