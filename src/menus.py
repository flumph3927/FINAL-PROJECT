#menus file, accessory to main function

import pygame
from helpers import *

# Clayton Baird, Main Menu



# basic skeleton for main menu, still need to make

def loadgame_menu(screen):
    current_screen = screen
    bg_image = pygame.image.load("images\\TitleScreen.png")
    bg_image = pygame.transform.scale(bg_image, (1000, 1000))
    while True:
        # clear other buttons
        current_screen.fill((255,255,255))
        current_screen.blit(bg_image,(0,0))
        return_button = Button(400,100,(255,0,0),(0,255,0),"Return to Main Menu",300,700)
        save_one = Button(400,100,(255,0,0),(0,255,0),"Load Save File One",300,100)
        save_two = Button(400,100,(255,0,0),(0,255,0),"Load Save File Two",300,300)
        save_three = Button(400,100,(255,0,0),(0,255,0),"Load Save File Three",300,500)

        return_button.draw(current_screen)
        save_one.draw(current_screen)
        save_two.draw(current_screen)
        save_three.draw(current_screen)
        for event in pygame.event.get():
            return_clicked = return_button.is_clicked(event)
            if return_clicked:
                return "Main"

            one_clicked = save_one.is_clicked(event)
            if one_clicked:
                return "One"

            two_clicked = save_two.is_clicked(event)
            if two_clicked:
                return "Two"

            three_clicked = save_three.is_clicked(event)
            if three_clicked:
                return "Three"
            
            pygame.display.flip()

def main_menu():
    pygame.init()
    current_screen = pygame.display.set_mode((1000,1000))
    bg_image = pygame.image.load("images\\TitleScreen.png")
    bg_image = pygame.transform.scale(bg_image, (1000, 1000))


    while True:
        current_screen.fill((255,255,255))
        current_screen.blit(bg_image,(0,0))

        
        quit_button = Button(400,100,(255,0,0),(0,255,0), "Quit Game",300,700) # still need to figure out what the x and y will be, as well as the colors
        demo_button = Button(400,100,(255,0,0),(0,255,0),"Try Demo",300,300)
        load_button = Button(400,100,(255,0,0),(0,255,0),"Load/Create Game",300,500)

        quit_button.draw(current_screen)
        demo_button.draw(current_screen)
        load_button.draw(current_screen)


        for event in pygame.event.get():
            quit_clicked = quit_button.is_clicked(event)
            if quit_clicked:
                return 1,"Quit"
            demo_clicked = demo_button.is_clicked(event)
            if demo_clicked:
                print("Demo")
                pass
            load_clicked = load_button.is_clicked(event)
            if load_clicked:
                file_choice = loadgame_menu(current_screen)
                if file_choice != "Main":
                    return 2,file_choice
                else:
                     pass
                    
        
        pygame.display.flip()



main_menu()
    # if quit button is pressed, just kill loop
    # if demo button is pressed, run run_generation function, set demo_run to true to it kicks user back to main menu once run ends
    # if load button is pressed, open load menu (gives user options for 3 different save files)


