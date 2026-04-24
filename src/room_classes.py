# CB 1st Room Templates

# from combat import *
# import all neccesary sprites

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

# class BossRoom(CombatRoom):
    # def __init__():
        # basic attributes will be #platforms and art

    # def boss_reward():
        # override preset reward and genreate boss-specific reward (something special needed for certain upgrades)

# class Shop:
    # def __init__():
        # basic variables are sprites, width, height, and stock (list of purchasable items)

    # def generate_stock():
        # pick 3 items from a list of possible purchase items
        # return these items

    # def load_sprites():
        # load background and npc sprite
        # load shop items and prices floating above them

# class HealingRoom
    # def __init__():
        # basic attributes are sprites, width, height, and heal_used

    # def heal():
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