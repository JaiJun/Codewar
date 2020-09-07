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