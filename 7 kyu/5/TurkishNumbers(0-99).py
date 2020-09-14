"""
Your Task
Complete the function to convert an integer into a string of the Turkish name.

input will always be an integer 0-99;
output should always be lower case.
Background
Forming the Turkish names for the numbers 0-99 is very straightforward:

units (0-9) and tens (10, 20, 30, etc.) each have their own unique name;
all other numbers are simply [tens] + [unit], like twenty one in English.
Unlike English, Turkish does not have "teen"-suffixed numbers;
e.g. 13 would be directly translated as "ten three" rather than "thirteen" in English.

Turkish names of units and tens are as follows:

0 = sıfır
1 = bir
2 = iki
3 = üç
4 = dört
5 = beş
6 = altı
7 = yedi
8 = sekiz
9 = dokuz

10 = on
20 = yirmi
30 = otuz
40 = kırk
50 = elli
60 = altmış
70 = yetmiş
80 = seksen
90 = doksan

Online I think best Solution
def get_turkish_number(num):
    if num < 10 or num%10 == 0:
        return turk_dict[num]
    else:
        return f"{turk_dict[(num//10)*10]} {turk_dict[num%10]}"
"""
import math
def get_turkish_number(num):
    res =[]
    numberline={
        0:"sıfır",
        1:"bir",
        2:"iki",
        3:"üç",
        4:"dört",
        5:"beş",
        6:"altı",
        7:"yedi",
        8:"sekiz",
        9:"dokuz",
        10:"on",
        20:"yirmi",
        30:"otuz",
        40:"kırk",
        50:"elli",
        60:"altmış",
        70:"yetmiş",
        80:"seksen",
        90:"doksan",

    }
    x_ten_digit = num % 100 //10  # 十位
    x_one_digit = num % 10
    print(x_ten_digit, x_one_digit)
    if x_ten_digit !=0 and x_one_digit==0:
        Combinenumber = str(numberline[x_ten_digit*10])
    elif x_ten_digit ==0:
        Combinenumber = str(numberline[x_one_digit])

    else:
        Combinenumber = str(numberline[x_ten_digit * 10] + " " + numberline[x_one_digit])
    print(Combinenumber)
    return Combinenumber
if __name__=='__main__':
    number = 99
    get_turkish_number(number)