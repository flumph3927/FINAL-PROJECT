# CB 1st Final Project Main loop

# basically import everything

import pygame
from data_management import *
from helpers import *
from home_base import *
from menus import *
from miscellaneous import *
from sprite_manage import *
from run_generation import*

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
    screen = pygame.display.set_mode((1000,1000))
    
    while True:
        save_path = None
        screen.fill((255,255,255))
        type, main_action = main_menu(screen)

        if type == 1:
            if main_action == "Quit":
                break
        else:
            if main_action=='One':
                save_path = 'documents/savefile_one.csv'
                player=Player('documents/savefile_one.csv')
            elif main_action=='Two':
                save_path = 'documents/savefile_two.csv'
                player=Player('documents/savefile_two.csv')
            elif main_action=='Three':
                save_path = 'documents/savefile_three.csv'
                player=Player('documents/savefile_three.csv')
        while True:
            trigger_run = home(screen,False,player,save_path)

            if trigger_run in [True,False]:
                player = run_loop(save_path,player)
            elif trigger_run == "Exit":
                del player
                break
    
            
            
if __name__ == "__main__":
    main_loop()