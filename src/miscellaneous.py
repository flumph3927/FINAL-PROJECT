#Psuedocode for HUD function, pause function, in-run upgrades, and room rewards function
#Levi

#create function show_hud, get screen, health, weapon, runtime, upgrades, ultimate
    #place health and ultimate as progress bars in the top left of screen
    #place runtime in top right of screen
    #place weapon name and sprite in bottom left of screen
    #place current in-run upgrades in bottom right of screen

#create function pause, get screen
    #place PAUSED text on top of screen
    #place save and exit button on screen
    #place resume button on screen
    #loop:
        #if save and exit button clicked: return True
        #if resume button clicked: return False