#All home base items, NPC classes, 

import pygame

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
    #create function speak, get screen, weapons
        #loop
            #place all weapons on screen as name and image
            #place selected weapon: selected weapon on top of screen
            #place esc to exit in corner of screen
            #if weapon clicked
                #loop
                    #draw weapon clicked big with description added and an esc to exit on screen
                    #if user has enough currency, place enter to select box on screen
                    #if enter clicked
                        #return weapon selected
                    #if esc clicked
                        #break out of loop
            #if esc clicked
                #break out of loop


#create class TutorialNPC, sublclass of NPC
    #create instruction list
    #create function speak, get screen
        #run function tutorial on screen


#create function tutorial, get screen
    #draw background on screen
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
    #loop:
        #if room number is 4:
            #loop:
                #place avaliable difficulty options on screen
                #if difficulty clicked: return difficulty level
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