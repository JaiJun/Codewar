"""
    Your friend invites you out to a cool floating pontoon around 1km off the beach.
    Among other things, the pontoon has a huge slide that drops you out right into the ocean, a small way from a set of stairs used to climb out.

    As you plunge out of the slide into the water, you see a shark hovering in the darkness under the pontoon... Crap!

    You need to work out if the shark will get to you before you can get to the pontoon.

    To make it easier... as you do the mental calculations in the water you either freeze when you realise you are dead, or swim when you realise you can make it!

    You are given 5 variables;

        sharkDistance = distance from the shark to the pontoon. The shark will eat you if it reaches you before you escape to the pontoon.

        sharkSpeed = how fast it can move in metres/second.

        pontoonDistance = how far you need to swim to safety in metres.

        youSpeed = how fast you can swim in metres/second.

        dolphin = a boolean, if true, you can half the swimming speed of the shark as the dolphin will attack it.

    The pontoon, you, and the shark are all aligned in one dimension.

    If you make it, return "Alive!", if not, return "Shark Bait!".


    I think best solution:
        def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
            if dolphin:
                shark_speed = shark_speed / 2

            shark_eat_time = shark_distance / shark_speed
            you_safe_time = pontoon_distance / you_speed

            return "Shark Bait!" if you_safe_time > shark_eat_time else "Alive!"


    https://www.codewars.com/kata/57e921d8b36340f1fd000059/python
"""

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    shark_time =0
    you_time =pontoon_distance/ you_speed
    print("You>",you_time)
    if dolphin:
        Twice = shark_speed*0.5
        shark_time = shark_distance/Twice
        print("Shark*1.5>",shark_time)
    else:
        shark_time=shark_distance/shark_speed
        print("Shark>",shark_time)

    if you_time < shark_time:
        print("Alive!")
        return "Alive!"
    else:
        print("Shark Bait!")
        return "Shark Bait!"
if __name__=='__main__':
    # 18 and 74 and 4 and 19 and True
    pontoon_distance = 18
    shark_distance = 74
    you_speed = 4
    shark_speed = 19
    dolphin = True
    shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin)