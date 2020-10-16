"""
    In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
    Example
    filter_list([1,2,'a','b']) == [1,2]
    filter_list([1,'a','b',0,15]) == [1,0,15]
    filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

"""
def filter_list(l):
    replacevalue =[]
    delstr =[]
    for i in range(len(l)):
        print(type(l[i]),l[i])
        if type(l[i]) == str:
            print("This is str")
            l[i] =replacevalue
        else:
            print("This is int")
            delstr.append(l[i])
    print(delstr)

    return delstr


if __name__=='__main__':
    input = [1,2,'a','b']
    filter_list(input)