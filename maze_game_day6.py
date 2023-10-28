def turn_right():
        turn_left()
        turn_left()
        turn_left()

#The functions move() and turn_left().
#Either the test front_is_clear() or wall_in_front(), 
#right_is_clear() or wall_on_right(), and at_goal().

""" 
    The secret is to have Reeborg follow along the 
    right edge of the maze, turning right if it can, 
    going straight ahead if it can’t turn right, 
    or turning left as a last resort.
    https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
"""
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
