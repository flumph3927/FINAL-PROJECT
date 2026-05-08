import pygame
import time


#sprite = (5,15,28,40)
        #boss_sheet = pygame.image.load("images/boss-sheet.png").convert_alpha()
        #boss_drop = boss_sheet.subsurface(sprite).convert_alpha()
        #boss_drop = pygame.transform.scale(boss_drop,(70,100))
        #screen.blit(boss_drop, (300,300))
#Add the boss into the enemy class so it can use all the functions and other things
class Boss(pygame.sprite.Sprite):
    def __init__(self,location):
        super().__init__()
        self.location = location
        self.speed = 4
        self.sprite_loc = (5,15,28,40)
        self.sword_loc = (2,60,20,35)
        self.sheet = pygame.image.load("images/boss-sheet.png").convert_alpha()
        self.sprite = self.sheet.subsurface(self.sprite_loc).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite,(70,100))
        self.sword = self.sheet.subsurface(self.sword_loc).convert_alpha()
        self.sword = pygame.transform.scale(self.sword,(50,100))
        self.rect = self.sprite.get_rect(center=(self.location))
    def phase_change(self):
        self.sprite_loc = (72,15,28,40)
        self.sword_loc = (87,60,13,35)
        self.sprite = self.sheet.subsurface(self.sprite_loc).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite,(70,100))
        self.sword = self.sheet.subsurface(self.sword_loc).convert_alpha()
        self.sword = pygame.transform.scale(self.sword,(36,100))