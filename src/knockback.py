# WM 1st Manage knockback and give i-frames
#import pygame
import pygame



#Define knockback function
    #For the knockback regarding player and enemey collison, there will be a point on the left side of the screen, that will be used to check the distance of both the sprites from it
    #The closer one will most likely be on the left, and so it will be knocked left, and the other will be knocked right.\
    #The same point will be used for attack knockback, as it the attacker is closer, then the hurt will go right
    #So if the hurt is closer they will go left
    #Take in the enemy object to be able to apply knockback

#Define collsion function
    #When a player and enemy collide, they will deal small damage to eachother, and deal more knockback to eachother, with the player getting i-frames
    #Using the sprite collide function in pygame, the game will always be checking if the player and any of the enemies are colliding, because the enemies will be in a group
    #When they do collide it will check which enemy collided and then do the damage, and the knockback, unless the player has i-frames
    #Will do the same thing with things like bullets and weapon

def knockbackfunc(s1,s2):
    point = pygame.Rect(0,600,1,1)
    pointvec = pygame.math.Vector2(point.center)
    s1vec = pygame.math.Vector2(s1.rect.center)
    s2vec = pygame.math.Vector2(s2.rect.center)
    d1 = pointvec.distance_to(s1vec)
    d2 = pointvec.distance_to(s2vec)
    if d1<d2:
        return -150, 150
    elif d2<d1:
        return 150, -150
    else:
        return 0, 0