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
        self.x = x
        self.y = y
        self.top = -(self.y)
        self.bottom = self.y
        self.left = self.x
        self.right = -(self.x)
        self.sprite = pygame.image.load("images\Platform.png").convert_alpha()
        self.sprite_rect = self.sprite.image.get_rect(top_left=(self.x,self.y))

    def collide_player(self,player):
        if self.sprite_rect.collide_rect(player.rect):
            pass

    def draw(self,screen):
        
        screen.blit(self.sprite,self.sprite_rect)

class Reward:
    def __init__(self,type,x,y):
        self.type = type
        self.rect = pygame.Rect(50,50,x,y)

    def interact(self,player):
        pass        

    def draw(self,screen):
        pass


class CombatRoom:
    def __init__(self,width,height,reward):
        self.width = width
        self.height = height
        self.reward = reward
        self.enemies = []
        self.platforms = []
        self.next_rewards = []

    # low, mid, and high are values for the required x value of that room's range of platforms.
    def generate_platforms(self,low,mid,high):
        def low_platforms(low):
            platform_1_y = random.randint(100,300)
            platform_1 = Platform(low,platform_1_y)

            platform_2_y = random.randint(100,300)
            platform_2 = Platform(low,platform_2_y)

            return platform_1,platform_2

        def mid_platforms(mid):
            platform_y = random.randint(400,500)
            platform = Platform(mid,platform_y)

            return platform

        def high_platforms(high):
            platform_1_y = random.randint(600,800)
            platform_1 = Platform(high,platform_1_y)

            platform_2_y = random.randint(600,800)
            platform_2 = Platform(high,platform_2_y)

            return platform_1,platform_2
        
        low_1,low_2 = low_platforms(low)
        mid_1 = mid_platforms(mid)
        high_1,high_2 = high_platforms(high)

        self.platforms.append(low_1,low_2,mid_1,high_1,high_2)

    # need to figure out most of this
    def generate_enemies(self):
        enemy_types = ['drone','melee','ranger']
        enemies = []

        for i in range(1,5):
            enemies.append(random.choice(enemy_types))

        self.enemies = enemies

        
    def generate_rewards(self):
        # probably gonna want to add more reward types
        reward_choices = ["Health","Upgrade","Run Currency", "Meta Currency"]
        rewards = []
        for _ in range(2):
            rewards.append(random.choice(reward_choices))

        self.next_rewards = rewards
    
    # figure out what variables will be changed, how to make interactable rewards (make a reward class)
    def spawn_reward(self):
        pass
        # figure out how to make rewards

    def draw(self,background,screen,low,mid,high):
        bg_image = pygame.image.load(background).convert_alpha()
        bg_image = pygame.transform.scale(bg_image,(800,800))
        screen.blit(bg_image)
        self.platforms = self.generate_platforms(low,mid,high)
        for i in self.platforms:
            i.draw(screen)

        self.enemies = self.generate_enemies()
        for i in self.enemies:
            i.draw(screen)
            # ask Ryan how enemies are spawned

class BossRoom(CombatRoom):
    def __init__(self):
        # basic attributes will be #platforms and art
        self.image = pygame.image.load("images/BossRoom.png")

    def boss_reward():
        # override preset reward and genreate boss-specific reward (something special needed for certain upgrades)
        boss_sheet = pygame.image.load("images/boss-sheet.png").convert_alpha()
        sprite = (40,30,20,20)
        boss_drop = boss_sheet.subsurface(sprite)
        boss_drop = pygame.transform.scale(boss_drop,(100,100))
        screen.blit(boss_drop, (400,400))
