"""
    Create a function which answers the question "Are you playing banjo?".
    If your name starts with the letter "R" or lower case "r", you are playing banjo!

    The function takes a name as its only argument, and returns one of the following strings:

    name + " plays banjo"
    name + " does not play banjo"

    I think best solution:
        def areYouPlayingBanjo(name):
            if name[0].lower() == 'r':
                return name + ' plays banjo'
            else:
                return name + ' does not play banjo'

    https://www.codewars.com/kata/53af2b8861023f1d88000832
"""
def areYouPlayingBanjo(name):
    namelist = list(name)
    print(namelist[0])
    if namelist[0] == "R" or namelist[0] == "r":
        print(name+" plays banjo")
        return name+" plays banjo"
    else:
        print(name+" does not play banjo!")
        return name+" does not play banjo!"

if __name__ == '__main__':
    input = "martin"
    areYouPlayingBanjo(input)