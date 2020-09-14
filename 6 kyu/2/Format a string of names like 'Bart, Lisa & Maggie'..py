"""
    Given: an array containing hashes of names

    Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand

    Example:

    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
    # returns 'Bart, Lisa & Maggie'

    namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
    # returns 'Bart & Lisa'

    namelist([ {'name': 'Bart'} ])
    # returns 'Bart'

    namelist([])
    # returns ''

    I think best solution:
        def namelist(names):
            if len(names) > 1:
                return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                        names[-1]['name'])
            elif names:
                return names[0]['name']
            else:
                return ''

        https://www.codewars.com/kata/53368a47e38700bd8300030d
"""

def namelist(names):
    combine = []

    print(names)
    if len(names) >= 3:
        print("Must work with many names")
        for i in range(len(names)):
            print(names[i]['name'])
            combine.append(names[i]['name'])
        Result = ", ".join(combine[:-1]) + " & " + combine[-1]
    elif len(names) == 2:
        print("Must work with two names")
        for i in range(len(names)):
            print(names[i]['name'])
            combine.append(names[i]['name'])
        Result = " & ".join(combine)
    elif len(names) == 1:
        print("Wrong output for a single name")
        for i in range(len(names)):
            print(names[i]['name'])
            combine.append(names[i]['name'])
        Result ="".join(combine)
    else:
        print("Must work with no names")
        Result = "".join(combine)
    print(Result)
    return Result
if __name__=='__main__':
    namestr=([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}])
    namelist(namestr)