"""
    What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
    For example:
        'abba' & 'baab' == true
        'abba' & 'bbaa' == true
        'abba' & 'abbba' == false
        'abba' & 'abca' == false
    Write a function that will find all the anagrams of a word from a list.
    You will be given two inputs a word and an array with words.
    You should return an array of all the anagrams or an empty array if there are none.
    For example:
        anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

        anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

        anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

"""
def anagrams(word, words):
    n1 = len(word)
    sortword = sorted(word)
    print(sortword)
    Result = []
    for i in range(len(words)):
        # print("Lenght  number",len(words[i]))
        # print("Now Compare word->", words[i])
        if n1 != len(words[i]):
            print("If lenght of both strings is not same, then they cannot be anagram.")
        else:
            print("Can anagram ->", sorted(words[i]))
            sortword2 = sorted(words[i])
            if (sortword == sortword2):
                print("This is same.")
                Result.append(words[i])
            else:
                print("Incompatible anagram.")
    print(Result)
    return Result



if __name__=='__main__':
    input ="racer"
    inpulist =['crazer', 'carer', 'racar', 'caers', 'racer']
    anagrams(input, inpulist)