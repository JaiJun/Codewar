"""
    The marketing team is spending way too much time typing in hashtags.
    Let's help them with our own Hashtag Generator!

    Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.
    Examples
    " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
    "    Hello     World   "                  =>  "#HelloWorld"
    ""                                        =>  false

    I think best solution:
        def generate_hashtag(s):
            output = "#"

            for word in s.split():
                output += word.capitalize()

            return False if (len(s) == 0 or len(output) > 140) else output

    https://www.codewars.com/kata/52449b062fb80683ec000024/python
"""

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
