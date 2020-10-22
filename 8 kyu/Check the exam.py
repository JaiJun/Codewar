"""
    The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"].

    The second one contains a student's submitted answers.

    The two arrays are not empty and are the same length.

    Return the score for this array of answers,

    giving +4 for each correct answer,

    -1 for each incorrect answer,

    and +0 for each blank answer,

    represented as an empty string (in C the space character is used).

    If the score < 0, return 0

    I think best solution:
        def check_exam(arr1,arr2):
            score = 0
            for i in range(0,4):
                if arr1[i] == arr2[i]:
                    score += 4
                elif arr1[i] == "" or arr2[i] == "":
                    score += 0
                else:
                    score -= 1

            return score if score >= 0  else 0

    https://www.codewars.com/kata/5a3dd29055519e23ec000074
"""
def check_exam(arr1,arr2):
    corevalue = 0
    for i in range(len(arr2)):
        if arr2[i] == "":
            corevalue+=0
        elif arr2[i] == arr1[i]:
            corevalue+=4
        else:
            corevalue+=-1
    print(corevalue)
    if corevalue <0:
        return 0
    else:
        return corevalue
if __name__ == '__main__':
    correct_answers = ["a", "a", "c", "b"]
    submitted_answers = ["a", "a", "b",  ""]
    check_exam(correct_answers, submitted_answers)