"""
    Vowel harmony is a phenomenon in some languages.
    It means that "A vowel or vowels in a word are changed to sound the same (thus "in harmony.")" (wikipedia).
    This kata is based on vowel harmony in Hungarian.

    Task:
    Your goal is to create a function dative() (Dative() in C#) which returns the valid form of a valid Hungarian word w in dative case
    i. e. append the correct suffix nek or nak to the word w based on vowel harmony rules.

    Vowel Harmony Rules (simplified)
    When the last vowel in the word is

    a front vowel (e, é, i, í, ö, ő, ü, ű) the suffix is -nek
    a back vowel (a, á, o, ó, u, ú) the suffix is -nak

    I think best solution:
        def dative(word):
            for c in word[::-1]:
                if c in u'eéiíöőüű':
                    return word+'nek'
                elif c in u'aáoóuú':
                    return word+'nak'
    https://www.codewars.com/kata/57fd696e26b06857eb0011e7/python
"""
def dative(word):
    Resutl =""
    frontvowel = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]
    backvowel =["a", "á", "o", "ó", "u", "ú"]
    print(word)
    for i in word:
        for front in frontvowel:
            if i == front:
                Result = word+"nek"
                break
        for back in backvowel:
            if i == back:
                Result = word + "nak"
                break
    print(Result)
    return Result

if __name__ == '__main__':
    input = "rokkant"
    print(dative(input))