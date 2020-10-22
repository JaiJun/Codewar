"""
    Who is the killer?
    Some people have been killed!

    You have managed to narrow the suspects down to just a few.

    Luckily, you know every person who those suspects have seen on the day of the murders.

    Task.
    Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

    {'James': ['Jacob', 'Bill', 'Lucas'],
     'Johnny': ['David', 'Kyle', 'Lucas'],
     'Peter': ['Lucy', 'Kyle']}
    and also a list of the names of the dead people:

    ['Lucas', 'Bill']
    return the name of the one killer,

    in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'

    I think best solution:
        def killer(info, dead):
            for name, seen in info.items():
                print(set(dead), set(seen))
                if set(dead) <= set(seen):
                    print("True")
                    return name

    https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d
"""


def killer(suspect_info, dead):
    for i, value in suspect_info.items():
        print(i, value)
        count = 0
        for element in dead:
            for j in value:
                if element == j:
                    count += 1
        print(count)
        if count == len(dead):
            return i
if __name__ == '__main__':
    info = {'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}
    deader = ['Lucas', 'Bill']
    print(killer(info, deader))
