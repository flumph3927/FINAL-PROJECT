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

def knockbackfunc(s1,s2,s3):
    point = pygame.Rect(0,600,1,1)
    pointvec = pygame.math.Vector2(point.center)
    s1vec = pygame.math.Vector2(s1.rect.center)
    try:
        s2vec = pygame.math.Vector2(s2.rect.center)
    except:
        s2vec = None
        s3vec = pygame.math.Vector2(s3.rect.center)
    d1 = pointvec.distance_to(s1vec)
    try:
        d2 = pointvec.distance_to(s2vec)
    except:
        d2 = pointvec.distance_to(s3vec)
    counter = 0
    if d1<d2:
        while counter < 5 and s1.rect.x >110:
            s1.rect.x -=10
            counter += 1
        counter = 0
        if s2vec != None:
            while counter < 5 and s2.rect.x <890:
                s2.rect.x +=10
                counter += 1
    elif d2<d1:
        if s2vec  != None:
            while counter < 5 and s2.rect.x >110:
                    s2.rect.x -=10
                    counter += 1
        counter = 0
        while counter < 5 and s1.rect.x <890:
                    s1.rect.x +=10
                    counter += 1