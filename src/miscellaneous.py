#Psuedocode for HUD function, pause function, in-run upgrades, and room rewards function
#Levi

import pygame,random, helpers

#create function show_hud, get screen, health, weapon, upgrades, ultimate, and in-run currency amount
def show_hud(scrn,hp,wpn,upgrade,ult,money):
    pygame.font.init()
    #place health as row of hearts and ultimate as progress bar in the top left of screen
    elements=pygame.image.load('images/HudElements.png').convert_alpha()
    full=pygame.transform.scale(elements.subsurface((50,110,100,100)),(60,60))
    half=pygame.transform.scale(elements.subsurface((480,110,100,100)),(60,60))
    ults=(pygame.transform.scale(elements.subsurface((50,420,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((193,420,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((337,420,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((480,420,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((623,420,100,100)),(60,60)))
    for i in range(int(hp)):
        scrn.blit(full,(100+80*i,20))
    if hp%1==0.5: scrn.blit(half,(100+80*int(hp),20))
    scrn.blit(ults[ult],(20,20))
    #place weapon name and sprite in bottom left of screen
    font=pygame.font.SysFont('',60)
    weapons=pygame.image.load('images/weapon.png').convert_alpha()
    if wpn==1:
        wsprt=pygame.transform.scale(weapons.subsurface((80, 180, 100, 100)),(60,60))
        text=font.render('GAUNTLET', True, (255, 255, 255))
    else:
        wsprt=pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60))
        text=font.render('M1 GARAND', True, (255, 255, 255))
    scrn.blit(wsprt,(20,920))
    scrn.blit(text,(100,920))
    #place money in bottom right
    coin=pygame.transform.scale(elements.subsurface((337,110,100,100)),(60,60))
    scrn.blit(coin,(500,920))
    text=font.render(str(money), True, (255, 255, 255))
    scrn.blit(text,(560,930))
    #place current in-run upgrades in right side of screen
    upgrades=(pygame.transform.scale(elements.subsurface((45,725,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((180,725,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((320,725,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((465,720,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((610,720,100,100)),(60,60)))
    for i in upgrade:
        scrn.blit(upgrades[i],(920,i*100+120))

#create function pause, get screen
def pause(scrn):
    #place PAUSED text on top of screen
    font=pygame.font.SysFont('',200)
    text=font.render('PAUSED', True, (0,255,0))
    scrn.blit(text,(220,100))
    #place save and exit button on screen
    save=helpers.Button(200,100,(100,100,100),(50,50,50),'Save and Exit',400,700)
    #place resume button on screen
    resume=helpers.Button(200,100,(100,100,100),(50,50,50),'Resume',400,300)
    #loop:
    while True:
        save.draw(scrn)
        resume.draw(scrn)
        pygame.display.flip()
        for event in pygame.event.get():
            #if save and exit button clicked: return True
            if save.is_clicked(event): return True
            #if resume button clicked: return False
            if resume.is_clicked(event): return False

#adapted class button to check which upgrades clicked
class Button(helpers.Button):
    def draw(self,screen):
        #by color i mean image
        screen.blit(self.color,self.rect)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(self.rect.center[0],self.rect.center[1]+40))
        screen.blit(text_surf, text_rect)


#create run upgrade function, get upgrades and screen
def run_upgrade(scrn,player):
    elements=pygame.image.load('images/HudElements.png').convert_alpha()
    upgrades=[0,1,2,3]
    #choose three at random (weighted)
    for i in player.upgrade:
        if i in upgrades:
            upgrades.remove(i)
    if upgrades==[]: return False
    if len(upgrades)<4:
        chosen=upgrades
    else:
        chosen=[]
        for i in range(3): chosen.append(upgrades.pop(random.randrange(len(upgrades))))
    #place the upgrade icons on screen with descriptions below
    elements=pygame.image.load('images/HudElements.png').convert_alpha()
    sprites=(pygame.transform.scale(elements.subsurface((45,725,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((180,725,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((320,725,100,100)),(60,60)),pygame.transform.scale(elements.subsurface((610,720,100,100)),(60,60)))
    texts=['HEALTH UP','DAMAGE UP','ULT RECHARGE','MONEY UP']
    buttons=[]
    buttons.append(Button(60,60,sprites[chosen[0]],chosen[0],texts[chosen[0]],240,500))
    if len(chosen)!=1:
        buttons.append(Button(60,60,sprites[chosen[1]],chosen[1],texts[chosen[1]],470,500))
        if len(chosen)!=2:
            buttons.append(Button(60,60,sprites[chosen[2]],chosen[2],texts[chosen[2]],700,500))
    #return upgrade user clicks on
    while True:
        for i in buttons:
            i.draw(scrn)
        pygame.display.flip()
        for event in pygame.event.get():
            for i in buttons:
                if i.is_clicked(event): return i.hover_color
