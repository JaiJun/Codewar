"""
    Our football team finished the championship. The result of each match look like "x:y".

    Results of all matches are recorded in the collection.

    For example: ["3:1", "2:2", "0:1", ...]

    Write a function that takes such collection and counts the points of our team in the championship.

    Rules for counting points for each match:

    if x>y - 3 points
    if x<y - 0 point
    if x=y - 1 point
    Notes:

    there are 10 matches in the championship
    0 <= x <= 4
    0 <= y <= 4

    I think best solution:
        def points(games):
            count = 0
            for score in games:
                res = score.split(':')
                if res[0]>res[1]:
                    count += 3
                elif res[0] == res[1]:
                    count += 1
            return count

    https://www.codewars.com/kata/5bb904724c47249b10000131
"""
def points(games):
    Totalvalue =0
    for i in games:
        Result = i.split(":")
        if int(Result[0]) > int(Result[1]):
            Totalvalue+=3
        elif int(Result[0]) < int(Result[1]):
            Totalvalue+=0
        elif int(Result[0]) == int(Result[1]):
            Totalvalue += 1
    print(Totalvalue)
    return Totalvalue
if __name__ == '__main__':
    input= ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
    points(input)