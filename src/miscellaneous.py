#Psuedocode for HUD function, pause function, in-run upgrades, and room rewards function
#Levi

import pygame

#create function show_hud, get screen, health, weapon, upgrades, ultimate, and in-run currency amount
def show_hud(scrn,hp,wpn,upgrade,ult,money):
    pygame.font.init()
    #place health as row of hearts and ultimate as progress bar in the top left of screen
    elements=pygame.image.load('images/HudElements.png').convert_alpha()
    full=pygame.transform.scale(elements.subsurface((50,110,100,100)),(60,60))
    half=pygame.transform.scale(elements.subsurface((480,110,100,100)),(60,60))
    ults=(pygame.transform.scale(elements.subsurface((50,420,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((193,420,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((337,420,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((480,420,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((623,420,100,100)),(60,60)))
    for i in range(int(hp)):
        scrn.blit(full,(100+80*i,20))
    if hp%1==0.5: scrn.blit(half,(100+80*int(hp),20))
    scrn.blit(ults[ult],(20,20))
    #place weapon name and sprite in bottom left of screen
    font=pygame.font.SysFont('',60)
    weapons=pygame.image.load('images/weapon.png').convert_alpha()
    if wpn==1:
        wsprt=pygame.transform.scale(weapons.subsurface((80, 180, 100, 100)),(60,60))
        text=font.render('GAUNTLET', True, (255, 255, 255))
    else:
        wsprt=pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60))
        text=font.render('M1 GARAND', True, (255, 255, 255))
    scrn.blit(wsprt,(20,920))
    scrn.blit(text,(100,920))
    #place money in bottom right
    coin=pygame.transform.scale(elements.subsurface((337,110,100,100)),(60,60))
    scrn.blit(coin,(500,20))
    text=font.render(str(money), True, (255, 255, 255))
    scrn.blit(text,(560,30))
    #place current in-run upgrades in right side of screen
    upgrades=(pygame.transform.scale(elements.subsurface((45,725,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((180,725,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((320,725,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((465,720,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((610,720,100,100)),(60,60)))
    for i in upgrade:
        scrn.blit(upgrades[i],(920,i*100+120))

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
