import pygame
from sprite_manage import *


#sprite = (5,15,28,40)
        #boss_sheet = pygame.image.load("images/boss-sheet.png").convert_alpha()
        #boss_drop = boss_sheet.subsurface(sprite).convert_alpha()
        #boss_drop = pygame.transform.scale(boss_drop,(70,100))
        #screen.blit(boss_drop, (300,300))
#Add the boss into the enemy class so it can use all the functions and other things
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.location = (300,300)
        self.speed = 4
        self.sprite_p1_loc = (5,15,28,40)
        self.sword1_loc = (2,60,20,35)
        self.sheet = pygame.image.load("images/boss-sheet.png").convert_alpha()
        self.sprite = self.sheet.subsurface(self.sprite_p1_loc).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite,(70,100))
        self.sword1 = self.sheet.subsurface(self.sword1_loc).convert_alpha()
        self.sword1 = pygame.transform.scale(self.sword1,(50,100))
        self.rect = self.sprite.get_rect(center=(self.location))
        screen.blit(self.sprite, self.location)
    def phase_change(self):
        self.sprite_p2_loc = (72,15,28,40)
        self.sword2_loc = (2,60,20,35)
        self.sheet = pygame.image.load("images/boss-sheet.png").convert_alpha()
        self.sprite = self.sheet.subsurface(self.sprite_p1_loc).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite,(70,100))
        self.sword1 = self.sheet.subsurface(self.sword1_loc).convert_alpha()
        self.sword1 = pygame.transform.scale(self.sword1,(50,100))
        self.rect = self.sprite.get_rect(center=(self.location))