#All home base items, NPC classes, 

import pygame, miscellaneous, helpers

#create class NPC
class NPC:
    #create function initialize, get name, img
    def __init__(self,name,img):
        #set variables to class variables, but inversed that
        self.name=name
        self.img=img

    #create function show, get screen
    def show(self,scrn,coords):
        #place img on screen with button to speak message below it and name above it on screen
        scrn.blit(self.img,coords)
        font=pygame.font.SysFont('',60)
        text=font.render(self.name, True, (255, 255, 255))
        scrn.blit(text,(coords[0],coords[1]-40))


#create class UpgradeNPC, subclass of NPC
    #create function speak, get screen, user upgrades, and currency
        #set upgrade tree
        #loop
            #place all user upgrades in their place on screen, upgrade sprite with name below
            #place esc to exit message in corner
            #loop through upgrades as upgrade
                #if user upgrades contain all prerequisites of upgrade
                    #place upgrade in appropriate position on screen
            #if upgrade clicked
                #loop
                    #draw upgrade clicked big with description added and an esc to exit on screen
                    #if user has enough currency, place enter to get box on screen
                    #if enter clicked
                        #return upgrade selected
                    #if esc clicked
                        #break out of loop
            #if esc clicked
                #break out of loop


#create class WeaponNPC, subclass of NPC
class WeaponNPC(NPC):

    #create function speak, get screen
    def speak(self,scrn,selected):
        weapons=pygame.image.load('images/weapon.png').convert_alpha()
        gaunt=miscellaneous.Button(60,60,pygame.transform.scale(weapons.subsurface((80, 180, 100, 100)),(60,60)),1,'GAUNTLET',300,700)
        gun=miscellaneous.Button(60,60,pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60)),2,'M1 GARAND',640,700)
        #loop
        loop=True
        while loop:
            scrn.fill((0,0,0))
            #place all weapons on screen as name and image
            gaunt.draw(scrn)
            gun.draw(scrn)
            #place selected weapon: selected weapon on top of screen
            if selected==1:
                shown=pygame.transform.scale(weapons.subsurface((80, 180, 100, 100)),(60,60))
            else: shown=pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60))
            scrn.blit(shown,(470,400))
            #place esc to exit in corner of screen
            font=pygame.font.SysFont('',60)
            text=font.render('ESC TO EXIT', True, (255, 255, 255))
            scrn.blit(text,(50,50))
            pygame.display.flip()
            #if weapon clicked
            for event in pygame.event.get():
                if gaunt.is_clicked(event): wpn=1
                elif gun.is_clicked(event): wpn=2
                else: wpn=0
                if wpn>0:
                    #loop
                    slcted=True
                    while slcted:
                        scrn.fill((0,0,0))
                        #draw weapon clicked big with description added and an esc to exit on screen
                        if wpn==1:
                            shown=pygame.transform.scale(weapons.subsurface((80, 180, 100, 100)),(300,300))
                            text=font.render('GAUNTLET - MELEE', True, (255, 255, 255))
                        else: 
                            shown=pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(300,300))
                            text=font.render('M1 GARAND - RANGED', True, (255, 255, 255))
                        rect=pygame.Rect(350,200,300,300)
                        scrn.blit(shown,rect)
                        text_rect = text.get_rect(center=(rect.center[0],rect.center[1]+160))
                        scrn.blit(text,text_rect)
                        #place enter to select box on screen
                        text=font.render('ENTER TO SELECT',True,(255,255,255))
                        scrn.blit(text,(50,850))
                        text=font.render('ESC TO EXIT', True, (255, 255, 255))
                        scrn.blit(text,(50,700))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type==pygame.KEYDOWN:
                                #if enter clicked
                                if event.key==pygame.K_RETURN:
                                    #return weapon selected
                                    scrn.fill((0,0,0))
                                    return wpn
                                #if esc clicked
                                if event.key==pygame.K_ESCAPE:
                                    #break out of loop
                                    slcted=False
                if event.type==pygame.KEYDOWN:
                    #if esc clicked
                    if event.key==pygame.K_ESCAPE:
                        #break out of loop
                        loop=False
        scrn.fill((0,0,0))
        return wpn


#create class TutorialNPC, sublclass of NPC
class TutorialNPC(NPC):

    #create function speak, get screen
    def speak(scrn):
        #run function tutorial on screen
        tutorial(scrn)


#create function tutorial, get screen
def tutorial(scrn):
    #draw background on screen
    pass
    #loop through instructions as instruction
        #display instruction on screen
        #until mouse clicked, loop
    #loop:
        #spawn enemy
        #if enemy dead: break out of loop
    #loop:
        #spawn 3 more enemies
        #if enemies dead:
            #return

#create function home, get scrn, difficulties
def home(scrn,diffs):
    #loop:
    room=1
    while True:
        #if room number is 4:
        if room==4:
            #loop:
            while True:
                #place avaliable difficulty options on screen
                if diffs==True:
                    hard=helpers.Button(200,100,(100,100,100),(150,150,150),'HARDMODE',200,400)
                    easy=helpers.Button(200,100,(100,100,100),(150,150,150),'NORMAL',600,400)
                    #if difficulty clicked: return difficulty level
                    for event in pygame.event.get():
                        if hard.is_pressed(event): return True
                        elif easy.is_pressed(event): return False
                else: return False
        #show room background on scrn
        #show HUD using function
        #if room is first:
            #show upgrades npc on scrn
        #elif room 2: #show weapons npc on scrn
        #elif room 3: #show tutorial npc on scrn
        #if user interacts with room npc:
            #run that npc's speak function
        #if user in exit:
            #change room number
            #next loop iteration
        #if user in entrance and room not 1
            #change room number
            #next loop iteration
'''
pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
elements=pygame.image.load('images/NPC.png').convert_alpha()
wnpc=WeaponNPC('bob',pygame.transform.scale(elements.subsurface((15, 150, 100, 100)),(60,60)))
wnpc.show(screen,(100,100))
print(wnpc.speak(screen,1))
while True:
    pygame.display.flip()'''