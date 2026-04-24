#RC 1st, manage sprites and creat them

#import pygame and math as well as any other needed module



#Create the Player class
    #Define init so that we can get each variable needed
        #(Define each sprites, weapons (Check to see if they've beeten the boss. If they have give them the gun option), and stats (Health, strenght, speed, velocity, jump strength).)


    #define a jump function
        #Make sure that the velocity is set
        #set is jumping to True so they can't spam jump

    #Define attack function
        #make usre there not attacking, then set attacking to true and show the weapon for ten frames


    #Create key press function
        #If left arrow key is pressed, move left

        #If right arrom key is pressed, move right

        #if up arrow is pressed, check to see that is jumping is false 
            #Set y value += to velocity and then is_jumping to false


        #Check if attack timer is above 0, then set it down one until it is returned as false


    #Define weapon creation
        #If wepaon is attacking then find mouse x and mouse y
            #If weapon is fist:
                #If key being pressed is left click
                    #calculate angle between player center and mouse
                    #Rotate the weapon bassed on that angle

                    #Then position it at the edge of the player towards the mouse.


                #Elif key being presses is right click
                    #Rotate the weapon bassed on that angle
                    #Then position it at the edge of the player towards the mouse.
                    
                    #Take that angle and launch a bullet at that enemy via that direction (Weakest bullet in the game)

                #Elif key being pressed is mouse wheel
                    #Remove I.frames and attack insanley fast with your punch
                    #Then reset the stats

                #Else
                    #pass

            #If weapon is rifle:
                #calculate angle between player center and mouse
                    #Rotate the weapon bassed on that angle
                    #Then position it at the edge of the player towards the mouse.
                    
                    #Take that angle and launch a bullet at that enemy via that direction

                #Elif key being presses is right click
                    #Rotate the bayonet and then jab it forward, if it hits the enemy they get dealt damage (Same logic as gauntlet, but its weaker)

                #Elif key being pressed is mouse wheel
                    #Increase damage and shoot off a masive laserbeam that can hit up to twice.
                



#Cretae an Enemy class:
    #initialze the name, image, and speed

    #Check to see if its name contains drone
        #create specific stats
        #Define the movement for the drone 
            #Check player location and move there

        #run the attacking for the drone:
            #if x and y values are in range:
                #attack with a punch, damaging the 
            #Else grab there location and the slope:
                #Use that to track the player and shoot a low damage, fast firing bullet.


    #Define Platform_get_on function
        #Go to the x of the player, if player.colliderect(paltform) ==True:
        #Jump to the y of them and also land on the platform.


    #If its a Grunt
        #Redifine specific stats
        #Follow x value, then if there on a platform, run the platform_get_on fucntion
        
        #Run the attacks for the grunt
            #If in range, use an attack similar to the users punch to damage the enemie
            #Damage will be affected by difficulty modifier

    #If its a Ranger
        #Redifine specific stats
        #Start on the right side of the map, if the user gets to close (set amount), go straight to the other side of the map while still shooting

        #Run the attacks for the Ranger
            #Take the location finder function from the drone and fire a bullet that will follow the needed slope.
            #Then define its attack and shoot it at the enemy.
        
        


#Define the setup 
    #Create the player through the player class
    #Add the player to the all_sprites group.
    #Add the enemies to there group

    #Spawn the enemies in a random place using random

    #Set running to true and loop bassed of off running

        #Check for every event that could happen:
        #Check for exiting game
        #Check for jumping
        #Check for attacking

        #If your colliding with a platform, set the ground to the platforms y
        #Otherwise set the ground value to the original 550

        #Start the movement function and the enemie function


        #Draw the environment and draw the sprites on the screen

        #Check to see if the players weapon hits and enemey
        #If it does then check each and every enemie until you find the one
        #Then have them take damage, gain I frames, and get knocked back

        
        #If there is a colision between an enemy and the player, check the i frames.
            #If the i frames = 0 then have them colide, have both take damage, and have them both colide

        #Make sure to display
        #Make sure to create frames per second




#Setup will be used in the main function, it will create all of the enemies and the players.