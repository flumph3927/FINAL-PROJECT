#RC 1st, manage sprites and creat them

#import pygame and math as well as any other needed module


#Initialize pygame
#create the screen that will be played on


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
                    ###ULTIMATE ATTACK###

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
                    ###ULTIMATE ATTACK###
                



#Cretae an Enemy class:
    #initialze the name, image, and speed

    #Check to see if its name contains drone
        #create specific stats
        #Define the movement for the drone 
            #Check player location and move there

        #run the attacking for the drone:

        ########WORK HERE ON ATTACKS.############


    #Define Platform_get_on function
        ################WORK HERE###############


    #If its a Grunt
        #Redifine specific stats
        #Follow x value, then if there on a platform, run the platform_get_on fucntion
        
        #Run the attacks for the grunt

        ###########WORK HERE ON ATTACKS##########

    #If its a Ranger
        #Redifine specific stats
        #Start on the right side of the map, if the user gets to close (set amount), go straight to the other side of the map while still shooting

        #Run the attacks for the Ranger

        ############ WORK HERE ON ATTACKS ##########
        


#Define the setup 