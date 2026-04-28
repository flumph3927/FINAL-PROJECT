# CB 1st Final Project Main loop

# basically import everything

import pygame
from data_management import *
from helpers import *
from home_base import *
from menus import *
from miscellaneous import *
from sprite_creation_and_managment import *

# def main_loop():
    # initialize pygame
    # start actual loop
        # load main menu (Demo, Load/Create Save, Quit)
        # check which button user presses
        # if Demo:
            # instantly go to the run main_loop and do a run
        # if Load/Create
            # display 3 save file options for the user to choose
            # if chosen save file if not intialized
                # set up all needed things and load
            # if chosen save file is initliazed
                # load all things

            # load home base main_loop
            # once user goes to start a run, load the run main_loop

            # if save and quit is run from home base, just save and quit
            # if save and quit is run from run main_loop, warn user that their run progress is not saved, and allow user to choose whether to leave or not (if in the middle of combat, do not allow to quit)


def main_loop():
    pygame.init()

    # create screen, setup all basic surfaces and other stuff
    screen = pygame.Surface((1000,1000))
    
    while True:
        screen.fill((255,255,255))
        main_action = main_menu(screen)

        if main_action == "Quit":
            break

        if main_action == "Demo":
            pass

        if main_action == "One":
            # load user data from save file one
            pass

        if main_action == "Two":
            # load user data from save file two
            pass

        if main_action == "Three":
            # load user data from save file three
            pass



