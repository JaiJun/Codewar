"""
    Given an array of ones and zeroes, convert the equivalent binary value to an integer.

    Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
"""
def binary_array_to_number(arr):
    Result =""
    for i in arr:
        Result+=str(i)
    print(int(Result))
    for j in range(16):
        number = int(bin(j).replace('0b', ''))
        # print(number)
        if int(Result)== number:
            print(j)
            return j





if __name__ == '__main__':
    input = [0,0,0,1]
    binary_array_to_number(input)