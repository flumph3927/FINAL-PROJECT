# WM 1st Manage knockback and give i-frames
#import pygame


#Define knockback function
    #For the knockback regarding player and enemey collison, there will be a point on the left side of the screen, that will be used to check the distance of both the sprites from it
    #The closer one will most likely be on the left, and so it will be knocked left, and the other will be knocked right.\
    #The same point will be used for attack knockback, as it the attacker is closer, then the hurt will go right
    #So if the hurt is closer they will go left
    #Take in the enemy object to be able to apply knockback

#Define collsion function
    #When a player and enemy collide, they will deal small damage to eachother, and deal more knockback to eachother, with the player getting i-frames
    #Using the sprite collide function in pygame, the game will always be checking if the player and any of the enemies are colliding
    #When they do collide it will check which enemy collided and then do the damage, and the knockback, unless the player has i-frames
    #Will do the same thing with things like bullets and weapons