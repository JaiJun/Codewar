"""
    In English, all words at the begining of a sentence should begin with a capital letter.

    You will be given a paragraph that does not use capital letters.

    Your job is to capitalise the first letter of the first word of each sentence.

    For example,

    input:

    "hello. my name is inigo montoya. you killed my father. prepare to die."

    output:

    "Hello. My name is inigo montoya. You killed my father. Prepare to die."

    You may assume:

    there will be no punctuation besides full stops and spaces

    all but the last full stop will be followed by a space and at least one word

    I think best solution:
        def fix(paragraph):
            return '. '.join(s.capitalize() for s in paragraph.split('. '))

    https://www.codewars.com/kata/5bf774a81505a7413400006a
"""

def fix(paragraph):
    if paragraph == "" or None:
        return ""
    else:
        words = paragraph.split(". ")
        new = []
        print(words)
        for i in range(len(words)):
            new.append(words[i].capitalize())

        Result = ". ".join(new)
        print(Result)
        return Result

if __name__ == '__main__':
    input = "hello. my name is inigo montoya. you killed my father. prepare to die."
    fix(input)