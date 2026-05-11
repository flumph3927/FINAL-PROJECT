# CB 1st Room Templates

# from combat import *
# import all neccesary sprites
import random
import pygame
from sprite_manage import *
# class Reward

# class CombatRoom:
    # def __init__():
        # basic variables will be width, height, reward, enemies (list)

    # def generate_platforms():
        # def low_platforms()
            # generate the coordinates for x # of platforms in the lower half of the room
            # verify that coordinates aren't outside of map
            # turn each of these into Rect objects and return objects
        # def mid_platforms()
            # generate the coordinates for x # of platforms in the middle of the room
            # verify that coordinates aren't outside of map
            # turn each of these into Rect objects and return objects
        # def high_platforms()
            # generate the coordinates for x # of platforms in the upper half of the room
            # verify that coordinates aren't outside of map
            # turn each of these into Rect objects and return objects

        # Note: all of these use platform sprite

        # run low_platforms, mid_platforms, and high_platforms specified amount of times

    # def generate_enemies():
        # pick enemy type from a list (Grunt, Drone, Ranger)
        # if there are not already 2 of that type of enemy, add a class object of it to the enemy list
        # do this for a specified amount of times

    # def generate_rewards():
        # pick possible rewards from a list for the next rooms once player eliminates all enemies

    # def spawn_reward():
        # check what self.reward is, spawn that sprite and make sure to incremement related variable

    # load_art():
        # load background art and set up basic collision



# class Shop:
    # def __init__():
        # basic variables are sprites, width, height, and stock (list of purchasable items)

    # def generate_stock():
        # pick 3 items from a list of possible purchase items
        # return these items

    # def load_sprites():
        # load background and npc sprite
        # load shop items and prices floating above them

class HealingRoom:
    def __init__(self):
        self.image = pygame.image.load("images/HealingRoom.png")
        self.width, self.height = self.image.get_size()
        self.table_trigger = pygame.Rect(70,110,20,20)
        self.heal_used = False
        
        # basic attributes are sprites, width, height, and heal_used

    def heal(self,player):
        if player.rect.colliderect(self.table_trigger) == True and self.heal_used == False:
            self.heal_used = True
            healing = random.randint(1,2.5)
            player.health += healing
            if player.health > player.max_health:
                player.health = player.max_health
        # triggered when user uses the heal thing and heal_used is false
        # generate a random number between 1 and 2.5, add that many hearts
        # set heal_used to true

    # def load_sprites():
        # load background and heal_area art

# class SquareRoom(CombatRoom):
    # def__init__():
        # basic attributes will be #enemies, #platforms, and the background

# class RectangularRoom(CombatRoom)
    # def__init__():
        # basic attributes will be #enemies, #platforms, and the background


# class ArchRoom(CombatRoom)
    # def__init__():
        # basic attributes will be #enemies, #platforms, and the background


# class BowlRoom(CombatRoom)
    # def__init__():
        # basic attributes will be #enemies, #platforms, and the background

# class Platform():
    # def __init__():
        # basic attributes will be locations, sprite, and rect

    # def draw():
        # load the platform sprite at the location set

class Platform:
    def __init__(self,x,y):
        self.sprite = pygame.image.load("images\\NewPlatform.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite,(75,150))
        self.sprite_rect = pygame.Rect(x,y,100,30)



    def draw(self,screen):
        screen.blit(self.sprite,self.sprite_rect)


class CombatRoom:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.enemies = []
        

    def generate_platforms(self):
        platforms = []
        def low_platforms():
            platform_1_y = random.randint(50,150)
            platform_1 = Platform(300,platform_1_y)

            platform_2_y = random.randint(100,300)
            platform_2 = Platform(700,platform_2_y)

            return platform_1,platform_2

        def mid_platforms():
            platform_y = random.randint(400,500)
            platform = Platform(500,platform_y)

            return platform

        def high_platforms():
            platform_1_y = random.randint(500,600)
            platform_1 = Platform(300,platform_1_y)

            platform_2_y = random.randint(500,600)
            platform_2 = Platform(700,platform_2_y)

            return platform_1,platform_2
        
        low_1,low_2 = low_platforms()
        mid_1 = mid_platforms()
        high_1,high_2 = high_platforms()

        platforms.append(low_1)
        platforms.append(low_2)
        platforms.append(mid_1)
        platforms.append(high_1)
        platforms.append(high_2)

        return platforms

    # need to figure out most of this
    def generate_enemies(self):
        enemy_types = ['drone','melee','ranger']
        enemies = []

        for _ in range(1,5):
            enemies.append(random.choice(enemy_types))

        self.enemies = enemies


    def draw(self,screen,platforms):
        bg_image = pygame.image.load("images//squarecombatroom-pixilart.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image,(800,800))
        screen.blit(bg_image,(100,100))
        self.platforms = self.generate_platforms()
        for i in platforms:
            i.draw(screen)

        

class BossRoom(CombatRoom):
    def __init__(self):
        # basic attributes will be #platforms and art
        self.image = pygame.image.load("images//BossRoom.png")

    def boss_reward():
        # override preset reward and genreate boss-specific reward (something special needed for certain upgrades)
        boss_sheet = pygame.image.load("images//boss-sheet.png").convert_alpha()
        sprite = (40,30,20,20)
        boss_drop = boss_sheet.subsurface(sprite)
        boss_drop = pygame.transform.scale(boss_drop,(100,100))
        screen.blit(boss_drop, (400,400))
