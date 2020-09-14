"""
    Mission Details:
    The map is represented as a 2D array. See the example below:

    map_example = [[1,3,5],[2,0,10],[-3,1,4],[4,2,4],[1,1,5],[-3,0,12],[2,1,12],[-2,2,6]]

    Here are what the values of each subarray represent:

    Time Dilation:
    With each additional layer of time dilation entered, time slows by a factor of 2.
    At layer 0, time passes normally.
    At layer 1, time passes at half the rate of layer 0.
    At layer 2, time passes at half the rate of layer 1, and therefore one quarter the rate of layer 0.


    Directions are as follow: 0 = North, 1 = East, 2 = South, 3 = West

    Distance Traveled: This represents the distance traveled relative to the current time dilation layer.

    See below:
        For the mapExample above:

        mapExample[0] -> [1,3,5]
        1 represents the level shift of time dilation
        3 represents the direction
        5 represents the distance traveled relative to the current time dilation layer

        Solomon's new location becomes [-10,0]

        mapExample[1] -> [2,0,10]
        At this point, Solomon has shifted 2 layers deeper.
        He is now at time dilation layer 3.
        Solomon moves North a Standard Distance of 80.
        Solomon's new location becomes [-10,80]

        mapExample[2] -> [-3,1,4]
        At this point, Solomon has shifted out 3 layers.
        He is now at time dilation layer 0.
        Solomon moves East a Standard Distance of 4.
        Solomon's new location becomes [-6,80]

        Your function should return Goromon's [x,y] coordinates.

        For mapExample, the correct output is [346,40].

        Additional Technical Details
        Inputs are always valid.
        Solomon begins his quest at time dilation level 0, at [x,y] coordinates [0,0].
        Time dilation level at any point will always be 0 or greater.
        Standard Distance is the distance at time dilation level 0.
        For given distance d for each value in the array: d >= 0.
        Do not mutate the input
        Note from the author: I made up this story for the purpose of this kata.
        Any similarities to any fictitious persons or events are purely coincidental.

        I think best solution:
            def solomons_quest(arr):
                pos, lvl = [0,0], 0
                for dilat,dir,dist in arr:
                    lvl += dilat
                    pos[dir in [0,2]] += dist * 2**lvl * (-1)**( dir in [2,3] )
                return pos

        https://www.codewars.com/kata/59d7c910f703c460a2000034/python
"""


def solomons_quest(arr):
    directions ={0: "North",
                 1: "East",
                 2: "South",
                 3: "West"}
    x=0
    y=0
    nowlayr = 0
    for i in arr:
        layer =i[0]
        directionsstr = directions[int(i[1])]
        Distance =i[2]
        print(">", layer, directionsstr, Distance)
        if directionsstr == "North" :
            nowlayr += layer
            print("Current Layer>", nowlayr)
            y += Distance * (2 ** nowlayr)
        elif directionsstr == "South":
            nowlayr += layer
            print("Current Layer>", nowlayr)
            y -= Distance * (2 ** nowlayr)
        elif directionsstr == "East":
            nowlayr+=layer
            print("Current Layer>", nowlayr)
            x += Distance * (2**nowlayr)
        else:
            nowlayr += layer
            print("Current Layer>", nowlayr)
            x -= Distance * (2 ** nowlayr)
    print("Laction>[{},{}]".format(x,y))
    location = [x, y]
    return location



if __name__ == '__main__':
    map_example =[[1, 3, 5], [2, 0, 10], [-3, 1, 4], [4, 2, 4], [1, 1, 5], [-3, 0, 12], [2, 1, 12], [-2, 2, 6]]
    solomons_quest(map_example)