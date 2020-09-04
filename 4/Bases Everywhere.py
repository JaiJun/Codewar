"""
Uh oh, Someone at the office has dropped all these sequences on the floor and forgotten to label them with their correct bases.

We have to fix this before the boss gets back or we're all going to be fired!

This is what your years of coding have been leading up to, now is your time to shine!

Task
You will have to create a function which takes in a sequence of numbers in random order and you will have to return the correct base of those numbers.

Constraints
The sequence will always be 10 numbers long and we know that the base is going to be between 2 and 10 inclusive so no need to worry about any letters.
When sorted, the sequence is made up of consecutive numbers.

Examples
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']     -->  10
['1', '2', '3', '4', '5', '6', '10', '11', '12', '13']  -->   7
"""
import more_itertools as mit
def base_finder(seq):
    base =[]
    for i in range(len(seq)):
        seq[i] =int(seq[i])
    new=sorted(seq)
    print(new)
    # for j in range(len(new)):
    #     # print(new[j]%10)
    #     base.append(new[j]%10)
    # basenumber = max(base)+1
    # print(max(base)+1)
    # return basenumber
if __name__=='__main__':
    equence =[1000001111, 1000010000, 1000010001, 1000010010, 1000010011, 1000010100, 1000010101, 1000010110, 1000010111, 1000011000]

    base_finder(equence)
