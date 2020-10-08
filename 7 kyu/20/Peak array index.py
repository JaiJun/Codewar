def peak(arr):
    length = len(arr)
    reverse = arr[::-1]
    Count=0
    ori_value, rev_value = 0, 0
    reversearray =[]
    original =[]

    for i in range(0, length//2):
        reversearray.append(reverse[i])
        original.append(arr[i])
    reversearray = sorted(reversearray)
    original =sorted(original)
    for i in range(len(original)):
        ori_value+=original[i]
        rev_value+=reversearray[i]
        if ori_value == rev_value:
            Count+=1
            print(ori_value, rev_value)

    if Count == 0:
        print("Nothing")
        return -1
    else:
        print(Count)
        return Count

if __name__ == '__main__':

    input = [9, 3, 2, 1, 2, 4, 3, 4, 5, 2, 1, 7, 8, 9, 1, 5, 7, 8, 5, 2, 2, 7, 1, 3, 7, 2, 6, 2, 2, 1, 1, 4, 2, 9, 2, 4, 6, 6, 5, 7, 4, 7, 5, 8, 5, 6, 6, 1, 1, 8, 5, 8, 8, 1, 9, 3, 2, 1, 2, 4, 3, 4, 5, 2, 1, 7, 8, 9, 1, 5, 7, 8, 5, 2, 2, 7, 1, 3, 7, 2, 6, 2, 2, 1, 1, 4, 2, 9, 2, 4, 6, 6, 5, 7, 4, 7, 5, 8, 5, 6, 6, 1, 1, 8, 5, 8, 8]

    peak(input)