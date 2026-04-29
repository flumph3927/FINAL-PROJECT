# CB 1st Room and Run generation

# from room_classes import *
# from combat import *
# import all neccesary sprites

from room_classes import *

# def generate_room(room_count):
    # check if room count is 4 or 5
    # if it is equal to 4, load a shop room
        # generate items to buy
    # if it is equal to 5, load boss room
        # generate boss and platforms
    # else:
    # randomly pick type of room (rectangle, square, bowl, dome) from a list
    # create an object of that subclass
    # generate the platforms and make sure user will be able to get out of room not matter what (and access all exits)
    # generate reward for next room(s)
    # generate enemies
    # once player kills all enemies, spawn reward and open up doors for next rooms
    # if player dies, make a pop up window, and return them to home base

# def run_loop():
    # function for the run's main loop
    # basically just start a loop and keep track of room count, check user health each iteration
    # if user dies, kick back to home base main loop

def generate_room(room_count):
    if room_count == 5:
        pass
        # generate a shop room
    elif room_count == 6:
        pass
        # generate the boss room
    else:
        if room_count == 1:
            room = CombatRoom(800,800,"Upgrade")
            room.generate_platforms()
