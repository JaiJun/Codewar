"""
    Messi's Goal Total
        Use variables to find the sum of the goals Messi scored in 3 competitions

    Information
    Messi goal scoring statistics:

    Competition	Goals
        La Liga	            43
        Champions League	10
        Copa del Rey	     5

    Task
    1) Create these three variables and store the appropriate values using the table above:

    la_liga_goals
    champions_league_goals
    copa_del_rey_goals
    2) Create a fourth variable named total_goals that stores the sum of all of Messi's goals for this year.

    https://www.codewars.com/kata/55ca77fa094a2af31f00002a
"""
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5
total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

if __name__ == '__main__':
    print(total_goals)
