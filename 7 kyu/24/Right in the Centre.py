"""
    Right in the Center
    This is inspired by one of Nick Parlante's exercises on the CodingBat online code practice tool.

    Given a sequence of characters, does "abc" appear in the CENTER of the sequence?

    The sequence of characters could contain more than one "abc".

    To define CENTER, the number of characters in the sequence to the left and right of the "abc" (which is in the middle) must differ by at most one.

    If it is in the CENTER, return True. Otherwise, return False.

    Write a function as the solution for this problem. This kata looks simple, but it might not be easy.

    I think best solution:
        def is_in_middle(seq):
            mid, rem = divmod(len(seq), 2)
            print(mid, rem)
            start = mid - 1
            print(start)
            end = start + 3
            print(end)
            if not rem:
                start -= 1
                print(" if not rem:")
            print(seq[start:end])
            return 'abc' in seq[start:end]


    https://www.codewars.com/kata/5f5da7a415fbdc0001ae3c69
"""

def is_in_middle(sequence):
    print("Input>", sequence)
    print("Length", len(sequence))
    check = "abc"
    remainder = len(sequence) %2
    if len(sequence) > 0:
        splitstring =sequence.count("abc")
        if splitstring == 1:
            onesplit=sequence.split("abc")
            print(onesplit)
            left = onesplit[0]
            right = onesplit[1]
            if len(left) == len(right) or abs(len(left)-len(right)) ==1:
                print("1-True")
                return True
            else:
                print("2-False")
                return False
        else:
            if remainder == 0:
                center = int(len(sequence) / 2) - 1
                print(sequence[center - 1], sequence[center], sequence[center + 1])
                centerstring = sequence[center - 1] + sequence[center] + sequence[center + 1]
                if centerstring == "abc":
                    print(remainder, "True")
                    return True
                else:
                    print(remainder, "Flase")
                    return False
            else:
                print(len(sequence) / 2)
                center = int(len(sequence) / 2)
                print(sequence[center - 1], sequence[center], sequence[center + 1])
                centerstring = sequence[center - 1] + sequence[center] + sequence[center + 1]
                if centerstring == "abc":
                    print(remainder, "True")
                    return True
                else:
                    print(remainder, "Flase")
                    return False
    else:
        return False


if __name__ == '__main__':
    input = "Yabc"

    is_in_middle(input)