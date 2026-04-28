#Psuedocode for HUD function, pause function, in-run upgrades, and room rewards function
#Levi

import pygame

#create function show_hud, get screen, health, weapon, runtime, upgrades, ultimate
def show_hud(scrn,hp,wpn,time,upgrade,ult):
    #place health as row of hearts and ultimate as progress bar in the top left of screen
    elements=pygame.image.load('images/HudElements.png').convert_alpha()
    full=pygame.transform.scale(elements.subsurface((50,110,100,100)),(60,60))
    for i in range(int(hp)):
        scrn.blit(full,(100+80*(i-1),20))
    #place runtime in top right of screen
    #place weapon name and sprite in bottom left of screen
    #place current in-run upgrades in bottom right of screen

#create function pause, get screen
    #place PAUSED text on top of screen
    #place save and exit button on screen
    #place resume button on screen
    #loop:
        #if save and exit button clicked: return True
        #if resume button clicked: return False

#create run upgrade function, get upgrades and screen
    #choose three at random (weighted)
    #place the upgrade icons on screen with descriptions below
    #return upgrade user clicks on

#create rewards function, get screen, difficulty
    #randomize rewards and scale with difficulty
    #place reward amounts on screen
    #return reward amounts

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
show_hud(screen,3,1,1,1,1)
while True:
    pygame.display.flip()
    clock.tick(10)