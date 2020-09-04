"""
    Trolls are attacking your comment section!

    A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

    Your task is to write a function that takes a string and return a new string with all vowels removed.

    For example:

    the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

    Note: for this kata y isn't considered a vowel.

    What is English vowels-> a、e、i、o、u

"""
def disemvowel(string):
    delword =["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    replaceword = ""
    detectword = list(string)
    combineword = []
    for i in range(len(detectword)):
        print(detectword[i])
        for j in range(len(delword)):
            if detectword[i] == delword[j]:
                detectword[i] =replaceword
                print("Replace!")
            else:
                print("Nothing Replace")
        combineword.append(detectword[i])
    Result = "".join(combineword)
    print(Result)
    return Result

if __name__=='__main__':
    input = "This website is for losers LOL!"
    disemvowel(input)