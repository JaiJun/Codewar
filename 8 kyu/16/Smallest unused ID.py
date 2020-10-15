"""
    Hey awesome programmer!

    You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

    Therefore you need a method, which returns the smallest unused ID for your next new data item...

    Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to find or remove them!

    Go on and code some pure awesomeness!

    I think best solution:
        def next_id(arr):
            t = 0
            while t in arr:
                t +=1
            return t

    https://www.codewars.com/kata/55eea63119278d571d00006a
"""
def next_id(arr):
    sortarr=sorted(arr)
    length = len(sortarr)
    compare= []
    unusednumber= []
    for i in range(0, length+1):
        compare.append(i)
    print(">",compare)
    for j in range(length+1):
        if compare[j] not in arr:
            unusednumber.append(compare[j])
        else:
            print("Include number")
    return unusednumber[0]



if __name__ == '__main__':
    input = []
    next_id(input)
