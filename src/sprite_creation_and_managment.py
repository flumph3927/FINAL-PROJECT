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

import pygame
import math
import random

#  INITIAL SETUP 
num_enemies = 0

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
#  CLASSES 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, damage, color=(255, 200, 0)):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.damage = damage
        self.speed = 7 if color == (255, 0, 0) else 12 # Enemy bullets are slower
        angle = math.atan2(target_y - y, target_x - x)
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load Player Sprite
        try:
            sprite_sheet = pygame.image.load('images/spritesheet.webp').convert_alpha()
            self.image_original = pygame.transform.scale(sprite_sheet.subsurface((35, 159, 125, 200)), (25, 40))
        except:
            self.image_original = pygame.Surface((25, 40)); self.image_original.fill((0, 0, 255))
        
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect(center=(400, 350))
        
        #  WEAPON LOADING 
        # Melee (Gauntlet)
        try:
            weapon_sheet = pygame.image.load("images/weapon.png").convert_alpha()
            self.gauntlet_surf = pygame.transform.scale(weapon_sheet.subsurface((60, 180, 130, 90)), (32, 24))
            self.gauntlet_surf = pygame.transform.rotate(self.gauntlet_surf, -90)
        except:
            self.gauntlet_surf = pygame.Surface((32, 24)); self.gauntlet_surf.fill((255, 0, 0))

        # Ranged (Gun from your image)
        try:
            gun_sheet = pygame.image.load("images/gun_sprite.png").convert_alpha()
            # Coordinates tuned for the gun in the image you sent
            self.gun_surf = pygame.transform.scale(gun_sheet.subsurface((37, 14, 12, 25)), (40, 40))
            self.gun_surf = pygame.transform.rotate(self.gun_surf, -25)
        except:
            self.gun_surf = pygame.Surface((32, 16)); self.gun_surf.fill((100, 100, 100))

        # Stats
        self.speed, self.floor_y, self.y_velocity = 5, 460, 0
        self.gravity, self.jump_strength = 0.8, -16.5
        self.health = 5.0
        self.iframes = 0
        self.is_jumping = False
        self.is_attacking, self.attack_timer = False, 0
        self.is_shooting, self.shoot_timer = False, 0
        self.shoot_cooldown = 0

    def jump(self):
        if not self.is_jumping:
            self.y_velocity = self.jump_strength
            self.is_jumping = True

    def update(self):
        keys = pygame.key.get_pressed()
        if self.health > 0:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if self.rect.left > 100: self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if self.rect.right < 700: self.rect.x += self.speed
        
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity
        if self.rect.y >= self.floor_y:
            self.rect.y, self.y_velocity, self.is_jumping = self.floor_y, 0, False

        # Timers
        if self.attack_timer > 0: self.attack_timer -= 1
        else: self.is_attacking = False
        
        if self.shoot_timer > 0: self.shoot_timer -= 1
        else: self.is_shooting = False

        if self.shoot_cooldown > 0: self.shoot_cooldown -= 1
        if self.iframes > 0: self.iframes -= 1
        
        # Alpha/Death Visuals
        if self.health <= 0: self.image.set_alpha(100)
        elif self.iframes > 0: self.image.set_alpha(150)
        else: self.image.set_alpha(255)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.health <= 0: # Outline in red if health <= 0
            pygame.draw.rect(surface, (255, 0, 0), self.rect.inflate(6, 6), 3)

    def draw_active_weapon(self, surface):
        if self.health <= 0: return None
        
        weapon_sprite = None
        if self.is_attacking: weapon_sprite = self.gauntlet_surf
        elif self.is_shooting: weapon_sprite = self.gun_surf

        if weapon_sprite:
            mx, my = pygame.mouse.get_pos()
            rel_x, rel_y = mx - self.rect.centerx, my - self.rect.centery
            angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            
            rotated_w = pygame.transform.rotate(weapon_sprite, int(angle))
            w_rect = rotated_w.get_rect(center=self.rect.center)
            dist = 35
            w_rect.centerx += math.cos(math.radians(-angle)) * dist
            w_rect.centery += math.sin(math.radians(-angle)) * dist


            if math.cos(math.radians(-angle)) * dist > 0:
                w_rect.centerx -= 20
            elif math.cos(math.radians(-angle)) * dist < 0:
                w_rect.centerx += 20

            if math.sin(math.radians(-angle)) * dist > 0:
                w_rect.centery -= 5

            surface.blit(rotated_w, w_rect)
            return w_rect
        return None

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            img = pygame.image.load("images/spritesheet_2.png")
            self.image = pygame.transform.scale(img.subsurface((660, 190, 97, 83)), (30,30))
        except:
            self.image = pygame.Surface((30, 30)); self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed, self.health = 2, 10
        self.hit_cooldown, self.attack_cooldown = 0, 0

    def update(self, target, enemy_bullets):
        if target.health <= 0: return 

        dx, dy = target.rect.centerx - self.rect.centerx, target.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        
        if dist > 30: # Move toward player
            self.rect.x += (dx / dist) * self.speed
            self.rect.y += (dy / dist) * self.speed

        # Range-based attack logic
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        elif target.iframes == 0:
            if dist < 50: # In range for Punch (1.0 damage)
                target.health -= 1.0; target.iframes = 30; self.attack_cooldown = 60
            elif dist < 350: # In range for Shoot (0.5 damage)
                eb = Bullet(self.rect.centerx, self.rect.centery, target.rect.centerx, target.rect.centery, 0.5, (255, 0, 0))
                enemy_bullets.add(eb)
                self.attack_cooldown = 100

        if self.hit_cooldown > 0: self.hit_cooldown -= 1

    def draw_health_bar(self, surf):
        pygame.draw.rect(surf, (255, 0, 0), (self.rect.x, self.rect.y - 10, 30, 5))
        if self.health > 0:
            pygame.draw.rect(surf, (0, 255, 0), (self.rect.x, self.rect.y - 10, (self.health/10)*30, 5))

#  MAIN ENGINE 

def setup():
    player = Player()
    enemies = pygame.sprite.Group()
    player_bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()

    for i in range(num_enemies):
        enemies.add(Enemy(random.randint(150, 650), random.randint(150, 450)))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            
            if event.type == pygame.KEYDOWN:
                # Spawn enemy with M
                if event.key == pygame.K_m:
                    enemies.add(Enemy(random.randint(150, 650), random.randint(150, 450)))
                
                if player.health > 0:
                    if event.key in [pygame.K_UP, pygame.K_w, pygame.K_SPACE]: player.jump()

            if event.type == pygame.MOUSEBUTTONDOWN and player.health > 0:
                if event.button == 1: # Melee Attack
                    player.is_attacking = True; player.attack_timer = 15
                if event.button == 3 and player.shoot_cooldown == 0: # Shoot Attack
                    mx, my = pygame.mouse.get_pos()
                    player.is_shooting = True; player.shoot_timer = 15
                    player_bullets.add(Bullet(player.rect.centerx, player.rect.centery, mx, my, 1))
                    player.shoot_cooldown = 25

        # Logic Updates
        player.update()
        enemies.update(player, enemy_bullets)
        player_bullets.update()
        enemy_bullets.update()

        # Bullet Collision (Enemy hits player)
        if player.iframes == 0 and player.health > 0:
            hits = pygame.sprite.spritecollide(player, enemy_bullets, True)
            for hit in hits:
                player.health -= 0.5; player.iframes = 25
                

        # Rendering
        screen.fill((255, 255, 255))
        for wall in [(0,0,800,100), (0,500,800,100), (0,0,100,600), (700,0,100,600)]:
            pygame.draw.rect(screen, (0,0,0), wall)
        
        player.draw(screen)
        weapon_hitbox = player.draw_active_weapon(screen)
        
        # Collision: Player attacking Enemies
        for enemy in list(enemies):
            if weapon_hitbox and weapon_hitbox.colliderect(enemy.rect) and enemy.hit_cooldown == 0:
                enemy.health -= 1; enemy.hit_cooldown = 20
            
            bullet_hits = pygame.sprite.spritecollide(enemy, player_bullets, True)
            for b in bullet_hits: enemy.health -= 0.5

            collision = pygame.sprite.spritecollide(player,enemies, False)
            if collision and player.iframes == 0:
                player.health -= 1
                player.iframes = 25
                
                for enemy in collision:
                    enemy.health -= 0.5


            if enemy.health <= 0: enemy.kill()
            else:
                screen.blit(enemy.image, enemy.rect)
                enemy.draw_health_bar(screen)

        player_bullets.draw(screen)
        enemy_bullets.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


setup()