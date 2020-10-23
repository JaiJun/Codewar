"""
    Write a function getDrinkByProfession/get_drink_by_profession() that receives as input parameter a string, and produces outputs according to the following table:

    Input	                Output
    "Jabroni"	            "Patron Tequila"
    "School Counselor"	    "Anything with Alcohol"
    "Programmer"	        "Hipster Craft Beer"
    "Bike Gang Member"	    "Moonshine"
    "Politician"	        "Your tax dollars"
    "Rapper"	            "Cristal"
    *anything else*	        "Beer"

    I think best solution:
        d = {
            "jabroni": "Patron Tequila",
            "school counselor": "Anything with Alcohol",
            "programmer": "Hipster Craft Beer",
            "bike gang member": "Moonshine",
            "politician": "Your tax dollars",
            "rapper": "Cristal"
        }

        def get_drink_by_profession(s):
            return d.get(s.lower(), "Beer")

    https://www.codewars.com/kata/568dc014440f03b13900001d
"""


def get_drink_by_profession(param):
    dict = {"Jabroni": "Patron Tequila",
            "School Counselor": "Anything with Alcohol",
            "Programmer": "Hipster Craft Beer",
            "Bike Gang Member": "Moonshine",
            "Politician": "Your tax dollars",
            "Rapper": "Cristal"
            }
    if param.title() in dict.keys():
        print(dict[param.title()])
        return dict[param.title()]
    else:
        print("Beer")
        return "Beer"


if __name__ == '__main__':
    input = "bike ganG member"
    get_drink_by_profession(input)
