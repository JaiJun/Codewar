def generate_hashtag(s=None):
    if s == None or s=="":
        return False
    elif len(s) > 140:
        print("The final word is longer than 140 chars")
        return False
    else:
        CobineWord = []
        for word in s.strip().split():
            word = word.capitalize()
            print(word)
            CobineWord.append(word)
        Result = "#" + "".join(CobineWord)
        print(Result)
        return Result


if __name__ == '__main__':
    input = "codewars  is  nice"
    generate_hashtag(input)
