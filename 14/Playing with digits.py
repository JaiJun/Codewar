"""
    ome numbers have funny properties. For example:

    89 --> 8¹ + 9² = 89 * 1

    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

    46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

    Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

    we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
    In other words:

    Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

    If it is the case we will return k, if not return -1.

    Note: n and p will always be given as strictly positive integers.

    https://www.codewars.com/kata/5552101f47fc5178b1000050
    
"""

def dig_pow(n, p):
    Result=0
    length =len(str(n))
    print(length)
    for i in str(n):
        print(int(i)**p)
        Result +=int(i)**p
        p+=1
    #判斷是否整除
    if Result % n ==0:
        print(Result/n)
        return int(Result/n)
    else:
        print(Result / n)
        return -1

if __name__=='__main__':
    input = 92
    Result=dig_pow(input,1)
    print(Result)