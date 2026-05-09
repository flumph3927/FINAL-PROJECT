#All home base items, NPC classes, 

import pygame,time,random, miscellaneous, helpers, sprite_manage

#create class NPC
class NPC:
    #create function initialize, get name, img
    def __init__(self,name,img):
        #set variables to class variables, but inversed that
        self.name=name
        self.img=img

    #create function show, get screen
    def show(self,scrn,coords):
        #place img on screen with button to speak message below it and name above it on screen
        scrn.blit(self.img,coords)
        font=pygame.font.SysFont('',60)
        text=font.render(self.name, True, (255, 255, 255))
        scrn.blit(text,(coords[0],coords[1]-40))



#OOF=miscellaneous.Button(width,height,image,returns,text,x,y)


#create class UpgradeNPC, subclass of NPC
class UpgradeNPC(NPC):

    #create function speak, get screen,weapon, user upgrades, and currency
    def speak(self,scrn,wpn,u_up,money):
        #set upgrade tree
        weapons=pygame.image.load('images/weapon.png').convert_alpha()
        tree={'+1 HEALTH':[pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60)),470,200,None,100],'2X DAMAGE':[pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60)),200,300,'+1 HEALTH',100],'2X I-FRAMES':[pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60)),470,300,'+1 HEALTH',100],'+1 HEALTH 2':[pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60)),740,300,'+1 HEALTH',100],'3X DAMAGE':[pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60)),200,400,'2X DAMAGE',100],'DOUBLE JUMP':[pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60)),470,400,'2X I-FRAMES',100],'+1 HEALTH 3':[pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60)),740,400,'+1 HEALTH 2',100],'+2 HEALTH':[pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60)),740,500,'+1 HEALTH 3',100]}         #ADD CORRECT IMAGES
        #loop
        buttons=[]
        for i in tree:
            buttons.append(miscellaneous.Button(60,60,tree[i][0],i,i,tree[i][1],tree[i][2]))
        runb=True
        while runb:
            scrn.fill((0,0,0))
            #place all user upgrades in their place on screen, upgrade sprite with name below
            for i in buttons:
                if i.text in u_up:
                    i.draw(scrn)
            #place esc to exit message in corner
            font=pygame.font.SysFont('',60)
            text=font.render('ESC TO EXIT', True, (255, 255, 255))
            scrn.blit(text,(50,50))
            #draw amount of coins
            coin=pygame.transform.scale(pygame.image.load('images/HudElements.png').convert_alpha().subsurface((200,110,100,100)),(60,60))
            scrn.blit(coin,(500,20))
            text=font.render(str(money), True, (255, 255, 255))
            scrn.blit(text,(560,30))
            #loop through upgrades as upgrade
            for i in buttons:
                if tree[i.text][3]:
                    #if user upgrades contain all prerequisites of upgrade
                    if tree[i.text][3] in u_up:
                        #place upgrade in appropriate position on screen
                        i.draw(scrn)
                else: i.draw(scrn)
            pygame.display.flip()
            for event in pygame.event.get():
                #if esc clicked
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        #break out of loop
                        runb=False
                #if upgrade clicked
                for i in buttons:
                    if i.is_clicked(event):
                        #loop
                        loopa=True
                        while loopa:
                            scrn.fill((0,0,0))
                            #draw upgrade clicked big with description added and an esc to exit on screen
                            scrn.blit(tree[i.text][0],(470,200))
                            #if user has enough currency, place enter to get box on screen
                            text=font.render(i.text, True, (255, 255, 255))
                            scrn.blit(text,(370,260))
                            if i.text in u_up:
                                text=font.render('OWNED', True, (255, 255, 255))
                            elif money>=tree[i.text][4]:
                                text=font.render('ENTER TO BUY FOR'+str(tree[i.text][4]), True, (255, 255, 255))
                            else:
                                text=font.render('COSTS '+str(tree[i.text][4]), True, (255, 255, 255))
                            scrn.blit(text,(300,500))
                            text=font.render('ESC TO EXIT', True, (255, 255, 255))
                            scrn.blit(text,(50,50))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type==pygame.KEYDOWN:
                                    #if enter clicked
                                    if event.key==pygame.K_RETURN:
                                        if tree[i.text][4]<=money:
                                            #return upgrade selected
                                            u_up.append(i.text)
                                            money-=tree[i.text][4]
                                    #if esc clicked
                                    if event.key==pygame.K_ESCAPE:
                                        #break out of loop
                                        loopa=False
        return u_up,wpn,money


#create class WeaponNPC, subclass of NPC
class WeaponNPC(NPC):

    #create function speak, get screen
    def speak(self,scrn,selected,upss,money):
        weapons=pygame.image.load('images/weapon.png').convert_alpha()
        gaunt=miscellaneous.Button(60,60,pygame.transform.scale(weapons.subsurface((80, 180, 100, 100)),(60,60)),1,'GAUNTLET',300,700)
        gun=miscellaneous.Button(60,60,pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60)),2,'M1 GARAND',640,700)
        #loop
        lop=True
        while lop:
            scrn.fill((0,0,0))
            #place all weapons on screen as name and image
            gaunt.draw(scrn)
            gun.draw(scrn)
            #place selected weapon: selected weapon on top of screen
            if selected==1:
                shown=pygame.transform.scale(weapons.subsurface((80, 180, 100, 100)),(60,60))
            else: shown=pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(60,60))
            scrn.blit(shown,(470,400))
            #place esc to exit in corner of screen
            font=pygame.font.SysFont('',60)
            text=font.render('ESC TO EXIT', True, (255, 255, 255))
            scrn.blit(text,(50,50))
            pygame.display.flip()
            #if weapon clicked
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    #if esc clicked
                    if event.key==pygame.K_ESCAPE:
                        #break out of loop
                        lop=False
                if gaunt.is_clicked(event): wpn=1
                elif gun.is_clicked(event): wpn=2
                else: wpn=0
                if wpn>0:
                    #loop
                    slcted=True
                    while slcted:
                        scrn.fill((0,0,0))
                        #draw weapon clicked big with description added and an esc to exit on screen
                        if wpn==1:
                            shown=pygame.transform.scale(weapons.subsurface((80, 180, 100, 100)),(300,300))
                            text=font.render('GAUNTLET - MELEE', True, (255, 255, 255))
                        else: 
                            shown=pygame.transform.scale(weapons.subsurface((475, 180, 100, 100)),(300,300))
                            text=font.render('M1 GARAND - RANGED', True, (255, 255, 255))
                        rect=pygame.Rect(350,200,300,300)
                        scrn.blit(shown,rect)
                        text_rect = text.get_rect(center=(rect.center[0],rect.center[1]+160))
                        scrn.blit(text,text_rect)
                        #place enter to select box on screen
                        text=font.render('ENTER TO SELECT',True,(255,255,255))
                        scrn.blit(text,(50,850))
                        text=font.render('ESC TO EXIT', True, (255, 255, 255))
                        scrn.blit(text,(50,700))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type==pygame.KEYDOWN:
                                #if enter clicked
                                if event.key==pygame.K_RETURN:
                                    #return weapon selected
                                    scrn.fill((0,0,0))
                                    return upss, wpn, money
                                #if esc clicked
                                if event.key==pygame.K_ESCAPE:
                                    #break out of loop
                                    slcted=False
                                    time.sleep(0.1)
        scrn.fill((0,0,0))
        return upss, wpn, money


#create class TutorialNPC, sublclass of NPC
class TutorialNPC(NPC):

    #create function speak, get screen
    def speak(self,scrn,weapon,upss,money):
        #run function tutorial on screen
        tutorial(scrn)
        return upss, weapon, money
    

#create function tutorial, get screen
def tutorial(scrn):
    instructions=['Enter to see next instructions','WASD or Arrow Keys to move','W, up arrow, or space to jump','Right click for primary attack','Left click for secondary attack','E to interact','Enter to begin combat tutorial']
    #draw background on screen
    bg=pygame.transform.scale(pygame.image.load('images/TutorialRoom.png').convert_alpha(),(1000,1000))
    scrn.blit(bg,(0,0))
    #loop through instructions as instruction
        #display instruction on screen
        #until mouse clicked, loop
    #loop:
        #spawn enemy
        #if enemy dead: break out of loop
    #loop:
        #spawn 3 more enemies
        #if enemies dead:
            #return

#create function home, get scrn, difficulties
def home(scrn,diffs,player):
    #loop:
    room=1
    while True:
        #if room number is 4:
        if room==4:
            #loop:
            while True:
                #place avaliable difficulty options on screen
                if diffs==True:
                    hard=helpers.Button(200,100,(100,100,100),(150,150,150),'HARDMODE',200,400)
                    easy=helpers.Button(200,100,(100,100,100),(150,150,150),'NORMAL',600,400)
                    #if difficulty clicked: return difficulty level
                    while True:
                        scrn.fill((0,0,0))
                        hard.draw(scrn)
                        easy.draw(scrn)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if hard.is_clicked(event): return True
                            elif easy.is_clicked(event): return False
                else: return False
        #show room background on 
        npc_images=pygame.image.load('images/NPC.png').convert_alpha()
        #show HUD using function
        #if room is first:
        if room==1:
            bg=pygame.transform.scale(pygame.image.load('images/MetaUpgradesRoom.png').convert_alpha(),(800,800))
            current=UpgradeNPC('UPGRADES (E)',pygame.transform.scale(npc_images.subsurface((50,180,130,200)),(100,160)))
        #elif room 2: #show weapons npc on scrn
        elif room==2:
            bg=pygame.transform.scale(pygame.image.load('images/WeaponsRoom.png').convert_alpha(),(800,800))
            current=WeaponNPC('WEAPONS (E)',pygame.transform.scale(npc_images.subsurface((50,180,130,200)),(100,160)))
        #elif room 3: #show tutorial npc on scrn
        elif room==3:
            bg=pygame.transform.scale(pygame.image.load('images/TutorialRoom.png').convert_alpha(),(800,800))
            current=TutorialNPC('TUTORIAL (E)',pygame.transform.scale(npc_images.subsurface((880,180,130,200)),(100,160)))
        run=True
        while run:
            miscellaneous.show_hud(scrn,player.health,player.weapon,player.upgrades,player.charge,player.money)
            scrn.blit(bg,(100,100))
            current.show(scrn,(300,678))
            #player movement here
            player.update()
            player.draw(scrn)
            pygame.display.flip()
            #if user interacts with room npc:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_e:
                        #run that npc's speak function
                        player.meta_upgrades, player.weapon,player.money = current.speak(scrn,player.weapon,player.upgrades,player.money)              #CHANGE WHAT iS PASSED TO IT TO META_UPGRADES
                    elif event.key==pygame.K_w or event.key==pygame.K_UP or event.key==pygame.K_SPACE:
                        player.jump()
            #if user in exit:
            if player.rect.x>=875:
                #change room number
                room+=1
                #next loop iteration
                player.rect.x=150
                run=False
            #if user in entrance and room not 1
            if player.rect.x<=100 and room!=1:
                #change room number
                room-=1
                #next loop iteration
                player.rect.x=825
                run=False
            
            

#create rewards class, get screen, difficulty
class Rewards(NPC):
    def speak(self,scrn,player):
        font=pygame.font.SysFont('',60)
        typ=random.randint(1,3)
        if typ==1:
            if player.health<=player.max_health-1:
                player.health+=1
                text=font.render('INCREASED HEALTH', True, (255, 255, 255))
            else:
                amt=random.randint(5,25)
            player.money+=amt
            text=font.render('+'+str(amt)+' MONEY', True, (255, 255, 255))
        elif typ==2:
            amt=random.randint(5,25)
            player.money+=amt
            text=font.render('+'+str(amt)+' MONEY', True, (255, 255, 255))
        elif typ==3:
            up=miscellaneous.run_upgrade(scrn,player)
            if up:
                player.upgrades=up
                return player
            else:
                print('fail')
                amt=random.randint(5,25)
                player.money+=amt
                text=font.render('+'+str(amt)+' MONEY', True, (255, 255, 255))
        scrn.blit(text,(300,470))
        pygame.display.flip()
        time.sleep(5)
        return player

'''pygame.init()
screen=pygame.display.set_mode((1000, 1000))
home(screen,True,sprite_manage.Player())'''