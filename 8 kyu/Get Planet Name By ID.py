"""
    The function is not returning the correct values. Can you figure out why?

    get_planet_name(3) # should return 'Earth'

    I think best solution:
        def get_planet_name(id):
            return {
                1: "Mercury",
                2: "Venus",
                3: "Earth",
                4: "Mars",
                5: "Jupiter",
                6: "Saturn",
                7: "Uranus",
                8: "Neptune",
            }.get(id, None)

    https://www.codewars.com/kata/515e188a311df01cba000003
"""
def get_planet_name(id):
    # This doesn't work; Fix it!

    dictstring ={
            1: "Mercury",
            2: "Venus",
            3: "Earth",
            4: "Mars",
            5: "Jupiter",
            6: "Saturn",
            7: "Uranus",
            8: "Neptune",
    }

    return dictstring[id]


if __name__ == '__main__':
    input = 3
    get_planet_name(input)