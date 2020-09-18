"""
    Create a function that takes any sentence and redistributes the spaces (and adds additional spaces if needed) so that each word starts with a vowel.
    The letters should all be in the same order but every vowel in the sentence should be the start of a new word.
    The first word in the new sentence may start without a vowel.
    It should return a string in all lowercase with no punctuation (only alphanumeric characters).

    EXAMPLES:
         'It is beautiful weather today!' becomes 'it isb e a ut if ulw e ath ert od ay'

         'Coding is great' becomes 'c od ing isgr e at'

         'my number is 0208-533-2325' becomes 'myn umb er is02085332325'

    Key word-isalnum()、lstrip()、f-string

    I think best solution:

        def vowel_start(st):
            rst = ''
            for e in st:
                if not e.isalnum():
                    continue
                e = e.lower()
                if e in 'aeiou':
                    rst += f' {e}'
                else:
                    rst += e
            return rst.lstrip()

"""
import re
def vowel_start(st):
    Result = []
    index = []
    st =re.sub('[^A-Za-z0-9]+', '', st).lower()
    print(st)
    for ele in range(0, len(st)):
        if st[ele] in "aeiou":
            index.append(ele)
            print(st[ele], ele)

    i =0
    for j in range(0, len(index), 1):
        print("Now>", (i, index[j]))
        if i==0 and index[j] ==0:
            print("None!")
        else:
            Result.append(st[i:index[j]])
            i = index[j]
            print(i)
    Result.append(st[i:])
    print(Result)
    Dividestr = " ".join(Result)
    return Dividestr

if __name__ == '__main__':
    input="oranges, apples, melon, pineapple"
    vowel_start(input)