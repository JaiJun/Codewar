"""
    The distance formula can be used to find the distance between two points.
    What if we were trying to walk from point A to point B, but there were buildings in the way?
    We would need some other formula..but which?

    Manhattan Distance
    Manhattan distance is the distance between two points in a grid
    (like the grid-like street geography of the New York borough of Manhattan)
    calculated by only taking a vertical and/or horizontal path.

    Write a function manhattanDistance that accepts two points, pointA and pointB,
    and returns the Manhattan Distance between the two points.
    pointA and pointB are arrays containing the x and y coordinate in the grid.
    you can think of x as the row in the grid, and y as the column.

    Examples:
        manhattan_distance( [1, 1], [1, 1] ) # => returns 0
        manhattan_distance( [5, 4], [3, 2] ) # => returns 4
        manhattan_distance( [1, 1], [0, 3] ) # => returns 3

    I think best solution:
        def manhattan_distance(pointA, pointB):
            return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])

    https://www.codewars.com/kata/52998bf8caa22d98b800003a
"""

def manhattan_distance(pointA, pointB):
    print(pointA[0],pointB[0])
    print(pointA[1],pointB[1])
    x = abs(pointA[0]-pointB[0])
    y = abs(pointA[1]-pointB[1])
    distance =x+y
    print(distance)
    return distance

if __name__=='__main__':
    A = [1,1]
    B = [1,1]
    Result=manhattan_distance(A,B)
    print(Result)