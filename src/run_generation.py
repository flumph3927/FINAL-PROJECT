# CB 1st Room and Run generation

# from room_classes import *
# from combat import *
# import all neccesary sprites

from room_classes import *
from sprite_manage import *
import pygame

# def generate_room(room_count):
    # check if room count is 4 or 5
    # if it is equal to 4, load a shop room
        # generate items to buy
    # if it is equal to 5, load boss room
        # generate boss and platforms
    # else:
    # randomly pick type of room (rectangle, square, bowl, dome) from a listddddd
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

pygame.init()
        

def run_loop():
    reward_given = False
    supper = False
    player = Player()
    enemies = pygame.sprite.Group()
    player_bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    room_count = 1
    
    while True:
        if room_count <= 4:
            room_count += 1
            alive, player = setup(player,enemies,player_bullets,enemy_bullets,supper,reward_given)

            if alive == False:
                return player
            else:
                continue
        elif room_count == 5:
            pass # generate healing room
        else:
            pass # generate boss room
if __name__ == "__main__":
    run_loop()
# What will need to be done from here is that we need to get room generation running at the start of setup so it actually generates the correct room.
# After this, we need to make sure setup() runs in run_loop the proper amount of times, and then have the heal room, shop room, and finally boss room load.
# This all needs to work so if the user dies, they return to the home base with the meta currency they collected.
            
# Maybe just generate platforms, enemies, and reward in setup instead of relying on a finicky room class?


