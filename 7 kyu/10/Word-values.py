"""
    Given a string "abc" and assuming that each letter in the string has a value equal to its position in the alphabet, our string will have a value of 1 + 2 + 3 = 6.
    This means that: a = 1, b = 2, c = 3 ....z = 26.

    You will be given a list of strings and your task will be to return the values of the strings as explained above multiplied by the position of that string in the list.
    For our purpose, position begins with 1

    nameValue ["abc","abc abc"] should return [6,24] because of [ 6 * 1, 12 * 2 ].
    Note how spaces are ignored.

    "abc" has a value of 6, while "abc abc" has a value of 12.
    Now, the value at position 1 is multiplied by 1 while the value at position 2 is multiplied by 2.

    Input will only contain lowercase characters and spaces.

    Good luck!

    I think best solution:
        def name_value(my_list):
          result = []
          for i in range(len(my_list)):
              subtotal = 0
              for c in my_list[i]:
                  if(c != ' '):
                      subtotal += ord(c) - ord('a') + 1
              result.append(subtotal*(i+1))
        return result

"""
import string


def name_value(my_list):
    alphabetvalue = 0
    Totalvalue = []
    alphabet = list(string.ascii_lowercase)
    compare = list(my_list[0])
    print(compare)
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            for k in range(len(alphabet)):
                if (my_list[i])[j] == alphabet[k]:
                    alphabetvalue = alphabetvalue + (k + 1)
                    print("This %d is value" % i, my_list[i], (my_list[i])[j], alphabet[k], alphabetvalue)
        Totalvalue.append(alphabetvalue * (i + 1))
        alphabetvalue = 0
    print(alphabetvalue)
    print(Totalvalue)
    return Totalvalue


if __name__ == '__main__':
    inpulist = ["codewars", "abc", "xyz"]
    # name_value(inpulist)
