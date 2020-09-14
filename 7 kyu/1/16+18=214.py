"""
 Number one : 18
 Number two : 226
 ToTal Number : 2314
"""


from click._compat import raw_input
import math
def add(num1, num2):

    x_hundreds_digit = num1 % 1000 // 100#百位
    x_ten_digit = num1 % 100 // 10  # 十位
    x_one_digit = num1 % 10  # 個位
    print("%d, %d, %d digit", x_hundreds_digit, x_ten_digit, x_one_digit)
    print()

    print("===============================")
    y_hundreds_digit = num2 % 1000 // 100  # 百位
    y_ten_digit = num2 % 100 // 10  # 十位
    y_one_digit = num2 % 10  # 個位
    print("%d, %d, %d digit", y_hundreds_digit, y_ten_digit, y_one_digit)
    com_hundreds_digit =str(x_hundreds_digit+y_hundreds_digit)
    com_ten_digit = str(x_ten_digit+y_ten_digit)
    com_one_digit = str(x_one_digit+y_one_digit)

    combine = int(com_hundreds_digit+com_ten_digit+com_one_digit)
    print(format(combine))
    return combine

def checkdigit(num1,num2):
    num1_len = len(str(num1))
    num2_len = len(str(num2))
    if(num1_len>num2_len or num1_len==num2_len):
        resealt =""
        for i in range(int(num1_len+1),0,-1):
            # print(math.pow(10,i))
            # print(num1 %math.pow(10,i))
            num1_digit =(num1 %math.pow(10,i)) // math.pow(10,i-1)
            # print("Num1 %d Digit number: %d" % (i, num1_digit))
            num2_digit =(num2 %math.pow(10,i)) // math.pow(10,i-1)
            # print("Num2 %d Digit number: %d" % (i, num2_digit))
            com = str(int(num1_digit+num2_digit))
            resealt+=com
            chagevalue = int(resealt)
            print(chagevalue)
    else:
        resealt = ""
        for i in range(int(num2_len + 1), 0, -1):
            # print(math.pow(10,i))
            # print(num1 %math.pow(10,i))
            num1_digit = (num1 % math.pow(10, i)) // math.pow(10, i - 1)
            # print("Num1 %d Digit number: %d" % (i, num1_digit))
            num2_digit = (num2 % math.pow(10, i)) // math.pow(10, i - 1)
            # print("Num2 %d Digit number: %d" % (i, num2_digit))
            com = str(int(num1_digit + num2_digit))
            resealt += com
            chagevalue =int(resealt)
            print(chagevalue)
    return num2_len
if __name__=='__main__':
    x = int(raw_input("Input One a number:\n"))
    y = int(raw_input("Input Two a number:\n"))
    # answer=add(x,y)
    # print(int(answer))
    print(checkdigit(x,y))
    # print(len(str(list)))
