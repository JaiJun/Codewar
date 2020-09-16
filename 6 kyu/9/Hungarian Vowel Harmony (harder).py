"""
    Vowel Harmony Rules (simplified)
        Front vowels: e, é, i, í, ö, ő, ü, ű

        Back vowels: a, á, o, ó, u, ú

        Vowel pairs (short -> long): a -> á, e -> é, i -> í, o -> ó, u -> ú, ö -> ő, ü -> ű

        Digraphs: sz, zs, cs

        Word ends with a vowel
        Change the ending vowel from short to long form.
        Append the suffix:
        vel if the ending vowel is a front vowel
        val if the ending vowel is a back vowel
        Word ends with a consonant
        Step one
        Default case: Double the ending consonant and continue with step two.
        Special case: If the word ends with a digraph then double the first letter (e. g. sz -> ssz)
        Step two
        Append the suffix:

        el if the last vowel is a front vowel
        al if the last vowel is a back vowel
    Examples:
        instrumental("fa") == "fával"
        instrumental("teve") == "tevével"
        instrumental("betű") == "betűvel"
        instrumental("ablak") == "ablakkal"
        instrumental("szék") == "székkel"
        instrumental("otthon") == "otthonnal"
        instrumental("kar") == "karral"
        instrumental("rács") == "ráccsal"
        instrumental("kosz") == "kosszal"
    Preconditions:
        All strings are unicode strings.
        The tests don't contain:
        exceptional cases like kávé -> kávéval
        words ending with doubled consonants (e. g. tett)
        words ending with y
        words ending with u, i

    I think best solution:
        def instrumental(word):
            mod = {"e": "é", "i": "í", "ö": "ő", "ü": "ű", "a": "á", "o": "ó", "u": "ú"}
            for c in word[::-1]:
                if c in "aáoóuú":
                    suf = "val"
                    break
                elif c in "eéiíöőüű":
                    suf = "vel"
                    break
            # word ends with a vowel
            if c == word[-1]:
                return word[:-1] + mod.get(c, word[-1]) + suf
            if word[-2:] in ("sz", "zs", "cs"):
                word = word[:-1] + word[-2:]
            else:
                word += word[-1]
            print(word + suf[1:])
            return word + suf[1:]
    https://www.codewars.com/kata/57fe5b7108d102fede00137a/python
"""


def instrumental(word):
    Result =""
    reword = word[::-1]
    frontvowel = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]
    backvowel = ["a", "á", "o", "ó", "u", "ú"]
    for i in range(len(reword)):
        #One frontvowel or backvowel
        if i == 0 and (reword[i] in frontvowel):
            if reword[i] == "e":
                reword = reword.replace("e", "é", 1)
                Result = reword[::-1] + "vel"
                break
            elif reword[i] == "i":
                reword = reword.replace("i", "í", 1)
                Result = reword[::-1] + "vel"
                break
            Result = reword[::-1] + "vel"
            break
        elif i == 0 and (reword[i] in backvowel):
            if reword[i] == "a":
                reword = reword.replace("a", "á", 1)
                Result = reword[::-1] + "val"
                break
            elif reword[i] == "o":
                reword = reword.replace("o", "ó", 1)
                Result = reword[::-1] + "val"
                break
            elif reword[i] == "u":
                reword[i] = reword.replace("u", "ú", 1)
                Result = reword[::-1] + "val"
                break
            Result = reword[::-1] + "val"
            break
        elif i != 0 and reword[i] in frontvowel:
            if reword[0] == "z" and reword[1] =="s":
                word = reword[::-1]
                Result = word[:len(word) - 1] + word[-2] + word[-1] + "el"
                break
            elif reword[0] == "s" and reword[1] =="z":
                word = reword[::-1]
                Result = word[:len(word) - 1] + word[-2] + word[-1] + "el"
                break
            elif reword[0] == "s" and reword[1] =="c":
                word = reword[::-1]
                Result = word[:len(word) - 1] + word[-2] + word[-1] + "el"
                break
            else:
                Result = reword[::-1] + word[-1] + "el"
                break
        elif i != 0 and reword[i] in backvowel:
            if reword[0] == "z" and reword[1] == "s":
                word = reword[::-1]
                Result = word[:len(word)-1] + word[-2] + word[-1] +"al"
                break
            elif reword[0] == "s" and reword[1] == "z":
                word = reword[::-1]
                Result = word[:len(word) - 1] + word[-2] + word[-1] + "al"
                break
            elif reword[0] == "s" and reword[1] == "c":
                word = reword[::-1]
                Result = word[:len(word) - 1] + word[-2] + word[-1] + "al"
                break
            else:
                Result = reword[::-1] + word[-1] + "al"
                break
    print(Result)
    return Result

if __name__ == '__main__':
    input="rács"
    print(instrumental(input))