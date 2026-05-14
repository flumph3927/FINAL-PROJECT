# CB 1st Room and Run generation

# from room_classes import *
# from combat import *
# import all neccesary sprites

from tkinter import font

from room_classes import *
from sprite_manage import *
import pygame
import time

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
        

def run_loop(save_path,player):
    alive = True
    reward_given = False
    supper = False
    enemies = pygame.sprite.Group()
    player_bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    room_count = 1
    room_total = random.randint(5,10)
    
    while True:
        if room_count <= room_total:
            room_count += 1
            alive, player = setup(player,enemies,player_bullets,enemy_bullets,supper,reward_given,alive,save_path)

            if alive == False:
                player.upgrades = []
                return player
        else:
            screen.fill((0,0,0))
            font = pygame.font.SysFont(None, 48)
            text_surface_one = font.render("You have reached the end of the developed game.", True, (255, 255, 255))
            text_rect = text_surface_one.get_rect(center=(500,500))
            screen.blit(text_surface_one, text_rect)
            text_surface_three = font.render("Thank you for playing!", True, (255, 255, 255))
            text_rect = text_surface_three.get_rect(center=(500,500))
            screen.blit(text_surface_three, text_rect)
            text_surface_two = font.render("You will be returned to the home base in 10 seconds.", True, (255, 255, 255))
            text_rect = text_surface_two.get_rect(center=(500,550))
            screen.blit(text_surface_two, text_rect)
            pygame.display.flip()
            time.sleep(10)
            player.upgrades = []
            player.health = player.max_health
            return player


        
if __name__ == "__main__":
    run_loop('documents/savefile_one.csv')
# What will need to be done from here is that we need to get room generation running at the start of setup so it actually generates the correct room.
# After this, we need to make sure setup() runs in run_loop the proper amount of times, and then have the heal room, shop room, and finally boss room load.
# This all needs to work so if the user dies, they return to the home base with the meta currency they collected.
            
# Maybe just generate platforms, enemies, and reward in setup instead of relying on a finicky room class?


