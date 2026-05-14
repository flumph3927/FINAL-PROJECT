import pygame
import math
import random
from knockback import knockbackfunc
from data_management import *
from miscellaneous import *
from room_classes import *
from home_base import *

#  INITIAL SETUP 
num_enemies = 0

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

#  CLASSES 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, damage, color=(255, 200, 0)):
        super().__init__()
        if color == (0, 0, 225):
            self.image = pygame.Surface((48, 16), pygame.SRCALPHA)
        elif color == (0, 0, 250):
            self.image = pygame.Surface((24, 8), pygame.SRCALPHA)
        else:
            self.image = pygame.Surface((8, 8), pygame.SRCALPHA)

        self.image.fill(color)
        self.damage = damage
        self.speed = 10 if color == (255, 0, 0) else 14  # Enemy bullets are slower
        angle = math.atan2(target_y - y, target_x - x)
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed

        if self.image.get_width() != self.image.get_height():
            self.image = pygame.transform.rotate(self.image, -math.degrees(angle))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self,save_file = "documents/savefile_one.csv"):
        super().__init__()
        # Load Player Sprite
        try:
            sprite_sheet = pygame.image.load('images/spritesheet.webp').convert_alpha()
            self.image_original = pygame.transform.scale(sprite_sheet.subsurface((35, 159, 125, 200)), (25, 40))
        except:
            self.image_original = pygame.Surface((25, 40)); self.image_original.fill((0, 0, 255))
        
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect(center=(150, 850))
        
        #  WEAPON LOADING 
        # Melee (Gauntlet)
        #Quick fix
        try:
            weapon_sheet = pygame.image.load("images/weapon.png").convert_alpha()
            self.gauntlet_surf = pygame.transform.scale(weapon_sheet.subsurface((60, 180, 130, 90)), (32, 24))
            self.gauntlet_surf = pygame.transform.rotate(self.gauntlet_surf, -90)
        except:
            self.gauntlet_surf = pygame.Surface((32, 24)); self.image.fill((255, 0, 0))

        # Ranged (Gun from your image)
        try:
            gun_sheet = pygame.image.load("images/gun_sprite.png").convert_alpha()
            self.gun_surf = pygame.transform.scale(gun_sheet.subsurface((37, 14, 12, 25)), (40, 40))
            self.gun_surf = pygame.transform.rotate(self.gun_surf, -25)
        except:
            self.gun_surf = pygame.Surface((32, 16)); self.gun_surf.fill((100, 100, 100))

        ###########Have variable file path############
        self.user_data = load_game(file_path=save_file)
        self.max_health = 5.0
        self.damage_mod = float(self.user_data["damage_mod"]) ##########Implement at each damge use #############
        self.iframes_mod = float(self.user_data["i_frame_mod"]) #########Implement this at each of the uses of player i frames ###########
        

        # Stats
        self.speed, self.floor_y, self.y_velocity = 8, 800, 0
        self.gravity, self.jump_strength = 0.8, -16.5
        self.iframes = 0
        self.is_jumping = False
        self.is_attacking, self.attack_timer = False, 0
        self.is_shooting, self.shoot_timer = False, 0
        self.shoot_cooldown = 0
        """self.weapon_choices = self.user_data["weapons"] #########Check this when switching weapon ###########"""
        self.weapon = 2
        self.max_charge = 4
        self.charge = 0
        self.money = 0
        self.fix = 0
        ##############Manage these variables #########################
        self.money = float(self.user_data["money"])
        self.meta_upgrades = self.user_data['upgrades']
        self.upgrades = []
        self.old_upgrades=[]
        for i in self.meta_upgrades:
            if i in ['+1 HEALTH','+1 HEALTH 2','+1 HEALTH 3']: self.max_health+=1
            elif i=='+2 HEALTH': self.max_health+=2
            elif i in ['+2X DAMAGE','3X DAMAGE']: self.damage_mod+=1
            elif i=='DOUBLE JUMP': pass
            elif i=='2X I-FRAMES': self.iframe_mod==2
        self.health = self.max_health

    def jump(self):
        if not self.is_jumping:
            self.y_velocity = self.jump_strength
            self.is_jumping = True

    def update(self,platforms):
        keys = pygame.key.get_pressed()
        if self.health > 0:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if self.rect.left > 100: self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if self.rect.right < 900: self.rect.x += self.speed
        
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity
        
        landed = False
        FLOOR_BOTTOM_Y = 840  # set this to wherever the visual floor surface actually is

        # Floor collision
        if self.rect.bottom >= FLOOR_BOTTOM_Y:
            self.rect.bottom = FLOOR_BOTTOM_Y
            self.y_velocity = 0
            self.is_jumping = False
            landed = True

        # Platform collision
        if platforms == None:
            pass
        else:
            if not landed and self.y_velocity > 0:
                for plat in platforms:
                    if self.rect.colliderect(plat.sprite_rect):
                        if self.rect.bottom - self.y_velocity <= plat.sprite_rect.top + 5:
                            self.rect.bottom = plat.sprite_rect.top  # ← also uses rect.bottom
                            self.y_velocity = 0
                            self.is_jumping = False
                            landed = True
                            break

        # Timers
        if self.attack_timer > 0: self.attack_timer -= 1
        else: self.is_attacking = False
        
        if self.shoot_timer > 0: self.shoot_timer -= 1
        else: self.is_shooting = False

        if self.shoot_cooldown > 0: self.shoot_cooldown -= 1
        if self.iframes > 0: self.iframes -= 1
        
        # Alpha / I-frame visuals
        if self.iframes > 0:
            self.image.set_alpha(150)
        else:
            self.image.set_alpha(255)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def draw_active_weapon(self, surface):
        if self.health <= 0: return None
        if self.weapon == 1:
            weapon_sprite = None
            if self.is_attacking or self.is_shooting:
                weapon_sprite = self.gauntlet_surf
            if weapon_sprite:
                mx, my = pygame.mouse.get_pos()
                rel_x, rel_y = mx - self.rect.centerx, my - self.rect.centery
                angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
                rotated_w = pygame.transform.rotate(weapon_sprite, int(angle))
                w_rect = rotated_w.get_rect(center=self.rect.center)
                dist = 35
                w_rect.centerx += math.cos(math.radians(-angle)) * dist
                w_rect.centery += math.sin(math.radians(-angle)) * dist
                surface.blit(rotated_w, w_rect)
                return w_rect
        elif self.weapon == 2:
            weapon_sprite = None
            if self.is_shooting or self.is_attacking:
                weapon_sprite = self.gun_surf
            if weapon_sprite:
                mx, my = pygame.mouse.get_pos()
                rel_x, rel_y = mx - self.rect.centerx, my - self.rect.centery
                angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
                rotated_w = pygame.transform.rotate(weapon_sprite, int(angle))
                w_rect = rotated_w.get_rect(center=self.rect.center)
                dist = 35
                w_rect.centerx += math.cos(math.radians(-angle)) * dist
                w_rect.centery += math.sin(math.radians(-angle)) * dist
                if math.cos(math.radians(-angle)) * dist > 5:
                    w_rect.centerx -= 20
                elif math.cos(math.radians(-angle)) * dist < 0:
                    w_rect.centerx += 20
                if math.sin(math.radians(-angle)) * dist > 0:
                    w_rect.centery -= 5
                surface.blit(rotated_w, w_rect)
                return w_rect
        return None

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type='drone'):
        super().__init__()

        if enemy_type=='drone':
            try:
                img = pygame.image.load("images/spritesheet_2.png")
                self.image = pygame.transform.scale(img.subsurface((660, 190, 97, 83)), (30,30))
            except:
                self.image = pygame.Surface((30, 30))
                self.image.fill((0, 255, 0))
        if enemy_type == 'melee':
            img = pygame.image.load("image/spritesheet_2.png")
            self.image = pygame.transform.scale(img.subsurface((60, 190, 97, 130)), (30,30))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed, self.health = 2, 5
        self.hit_cooldown, self.attack_cooldown = 0, 0
        self.max_health = self.health
        self.type = enemy_type
        if self.type == 'drone':
            pass
        elif self.type == 'melee':
            self.image.fill((255, 0, 255))

    def update(self, target, enemy_bullets):
        if target.health <= 0: return
        dx, dy = target.rect.centerx - self.rect.centerx, target.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if self.type == 'melee':
            # stay on ground, no vertical movement
            if dist > 5:
                self.rect.x += (dx / dist) * self.speed
            # y stays fixed
        else:
            if dist > 30:
                self.rect.x += (dx / dist) * self.speed
                self.rect.y += (dy / dist) * self.speed
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1
            elif target.iframes == 0:
                if dist < 50:
                    target.health -= 0.5
                    target.iframes = 30
                    self.attack_cooldown = 60
                elif dist < 350:
                    eb = Bullet(self.rect.centerx, self.rect.centery, target.rect.centerx, target.rect.centery, 0.5, (255, 0, 0))
                    enemy_bullets.add(eb)
                    self.attack_cooldown = 100
        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

    def draw_health_bar(self, surf):
        pygame.draw.rect(surf, (255, 0, 0), (self.rect.x, self.rect.y - 10, 30, 5))
        if self.health > 0:
            pygame.draw.rect(surf, (0, 255, 0), (self.rect.x, self.rect.y - 10, (self.health / self.max_health) * 30, 5))


class MeleeEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img = pygame.image.load("images/spritesheet_2.png")
        self.image = pygame.transform.scale(img.subsurface((65, 150, 130, 170)), (30,40))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 3
        self.health = 3.1
        self.max_health = self.health
        self.hit_cooldown, self.attack_cooldown = 0, 0

    def update(self, target, enemy_bullets):
        if target.health <= 0:
            return
        dx, dy = target.rect.centerx - self.rect.centerx, target.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist > 5:
            self.rect.x += (dx / dist) * self.speed
            # y stays fixed
            self.rect.y = self.rect.y
        if self.rect.colliderect(target.rect):
            if target.iframes == 0:
                target.health -= 1
                target.iframes = 25
        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

    def draw_health_bar(self, surf):
        pygame.draw.rect(surf, (255, 0, 0), (self.rect.x, self.rect.y - 10, 30, 5))
        if self.health > 0:
            pygame.draw.rect(surf, (0, 255, 0), (self.rect.x, self.rect.y - 10, (self.health / self.max_health) * 30, 5))

# New RangerEnemy class with improved collision handling
class RangerEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img = pygame.image.load("images/spritesheet_2.png")
        self.image = pygame.transform.scale(img.subsurface((365, 150, 130, 170)), (30,40))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 3
        self.health = 4
        self.max_health = self.health
        self.state = 'attack'
        self.move_left_bound = 150
        self.move_right_bound = 850
        self.y = y
        self.shoot_cooldown = 0
        self.hit_cooldown = 0

    def update(self, target, enemy_bullets, all_rangers):
        self.rect.y = self.y

        # Store original position
        original_x = self.rect.x

        # Move within bounds
        if self.rect.centerx <= self.move_left_bound:
            self.rect.centerx = self.move_left_bound
            self.rect.x += 50
        elif self.rect.centerx >= self.move_right_bound:
            self.rect.centerx = self.move_right_bound
            self.rect.x -= 50

        # Move towards/away from player
        dx = target.rect.centerx - self.rect.centerx
        dist_x = abs(dx)

        if dist_x < 200:
            if self.rect.centerx > self.move_left_bound:
                self.rect.x -= self.speed
            elif self.rect.centerx < self.move_right_bound:
                self.rect.x += self.speed
        else:
            if self.rect.centerx < self.move_left_bound:
                self.rect.x += self.speed
            elif self.rect.centerx > self.move_right_bound:
                self.rect.x -= self.speed

        # Save position before checking collisions
        prev_x = self.rect.x

        # Check for collisions with other ranger enemies
        collided_rangers = [r for r in all_rangers if r != self and self.rect.colliderect(r.rect)]
        if collided_rangers:
            # Revert to previous position to avoid overlapping
            self.rect.x = prev_x
            # Optional: move away slightly
            for r in collided_rangers:
                if self.rect.centerx < r.rect.centerx:
                    self.rect.x -= self.speed
                else:
                    self.rect.x += self.speed

        # Keep within bounds after collision resolution
        if self.rect.left < self.move_left_bound:
            self.rect.left = self.move_left_bound
        if self.rect.right > self.move_right_bound:
            self.rect.right = self.move_right_bound

        # Shoot at player with "infinite range"
        if self.shoot_cooldown == 0:
            dy = target.rect.centery - self.rect.centery
            dx_total = target.rect.centerx - self.rect.centerx
            dist = math.hypot(dx_total, dy)
            if dist < 600:
                enemy_bullets.add(Bullet(self.rect.centerx, self.rect.centery, target.rect.centerx, target.rect.centery, damage=1, color=(0, 0, 250)))
                self.shoot_cooldown = 90
        else:
            self.shoot_cooldown -= 1

        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

    def draw_health_bar(self, surf):
        pygame.draw.rect(surf, (255, 0, 0), (self.rect.x, self.rect.y - 10, 30, 5))
        if self.health > 0:
            pygame.draw.rect(surf, (0, 255, 0), (self.rect.x, self.rect.y - 10, (self.health / self.max_health) * 30, 5))

#  MAIN ENGINE 

# 0 increases health
#1 damage
#2 equals charge

def setup(player,enemies,player_bullets,enemy_bullets,supper,reward_given,alive,save_path):

    # List containing enemy types to spawn
    enemy_type_list = []
    # This code is for generating enemies randomly. Currently commented out for dev purposes
    
    

    room = CombatRoom(900,900) # Initialize the room
    room.generate_enemies() # Generate enemy list, similar to above code
    platforms = room.generate_platforms() # Generate platforms, to be drawn later.

    #enemy_type_list = ['drone', 'melee', 'ranger', 'drone', 'melee', 'ranger']
    # Count how many of each type
    drone_count = room.enemies.count('drone')
    melee_count = room.enemies.count('melee')
    ranger_count = room.enemies.count('ranger')

    # Spawn drones at fixed y position 50 pixels above ground
    drone_spawn_y = player.floor_y - 50
    for _ in range(drone_count):
        enemies.add(Enemy(random.randint(150, 650), drone_spawn_y, enemy_type='drone'))

    # Spawn melee enemies at ground level
    for _ in range(melee_count):
        enemies.add(MeleeEnemy(random.randint(150, 650), player.floor_y))

    # Spawn ranger enemies on the right side, at fixed y
    ranger_spawn_y = player.floor_y
    for _ in range(ranger_count):
        enemies.add(RangerEnemy(random.randint(700, 950), ranger_spawn_y))

    running = True
    player.rect.x, player.rect.y = 100,800
    while running:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (100, 100, 800, 800))
        show_hud(screen, player.health, player.weapon, player.upgrades, player.charge, player.money)
        room.draw(screen,platforms)
        player.draw(screen)
        for i in player.upgrades:
            if i not in player.old_upgrades:
                if i == 0:
                    player.health += 1
                elif i == 1:
                    player.damage_mod += 1
                elif i == 2:
                    player.max_charge -= 1
        player.old_upgrades=player.upgrades
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_check = miscellaneous.pause(screen, player, save_path)
                    if exit_check == "Exit":
                        # Return to home base without saving run progress
                        alive = False
                        return alive, player
                if player.health > 0:
                    if event.key in [pygame.K_UP, pygame.K_w, pygame.K_SPACE]:
                        player.jump()


            ##################DUPLICATE THIS TO ALLOW FOR THE supper TO BE CAST BY PRESSING U######################
            if player.weapon == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if player.health > 0:
                        if event.button == 1:
                            player.is_attacking = True
                            player.attack_timer = 15
                        if event.button == 2:
                            if player.charge >= player.max_charge:
                                player.damage_mod = 4
                                player.is_attacking = True
                                player.attack_timer = 15
                                supper = True
                                player.charge = 0
                        if event.button == 3 and player.shoot_cooldown == 0:
                            mx, my = pygame.mouse.get_pos()
                            player.is_shooting = True
                            player.shoot_timer = 15
                            player_bullets.add(Bullet(player.rect.centerx, player.rect.centery, mx, my, 1*player.damage_mod))
                            player.shoot_cooldown = 15

            if player.weapon == 2:
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if player.health > 0:
                        if event.button == 1:
                            mx, my = pygame.mouse.get_pos()
                            player.is_shooting = True
                            player.shoot_timer = 15
                            player_bullets.add(Bullet(player.rect.centerx, player.rect.centery, mx, my, 2*player.damage_mod, (192, 192, 192)))
                            player.shoot_cooldown = 25
                        if event.button == 2:
                            if player.charge >= player.max_charge:
                                supper = True
                                mx, my = pygame.mouse.get_pos()
                                player.is_shooting = True
                                player.shoot_timer = 15
                                player_bullets.add(Bullet(player.rect.centerx, player.rect.centery, mx, my, 8, (0,0, 225)))
                                player.shoot_cooldown = 15
                                player.charge = 0
                        if event.button == 3 and player.shoot_cooldown == 0:
                            player.is_attacking = True
                            player.attack_timer = 15

        # Update logic
        player.update(platforms)
        # List of ranger enemies
        ranger_enemies = [enemy for enemy in enemies if isinstance(enemy, RangerEnemy)]
        for enemy in list(enemies):
            if isinstance(enemy, RangerEnemy):
                enemy.update(player, enemy_bullets, ranger_enemies)
            else:
                enemy.update(player, enemy_bullets)
        player_bullets.update()
        enemy_bullets.update()

        # Collisions
        if player.iframes == 0 and player.health > 0:
            hits = pygame.sprite.spritecollide(player, enemy_bullets, True)
            for hit in hits:
                player.health -= 0.5
                player.iframes = 25

        weapon_hitbox = player.draw_active_weapon(screen)

        for enemy in list(enemies):
            if weapon_hitbox and weapon_hitbox.colliderect(enemy.rect) and enemy.hit_cooldown == 0:
                enemy.health -= 1.5*player.damage_mod
                enemy.hit_cooldown = 20
                knockbackfunc(enemy, None, player)

            bullet_hits = pygame.sprite.spritecollide(enemy, player_bullets, True)
            for b in bullet_hits:
                enemy.health -= b.damage*player.damage_mod

            # Damage from melee enemies
            if isinstance(enemy, MeleeEnemy):
                if enemy.rect.colliderect(player.rect):
                    if player.iframes == 0:
                        player.health -= 1
                        player.iframes = 25*player.iframes_mod

            # Draw enemy if alive
            if enemy.health <= 0:
                enemy.kill()
                if player.charge <= 3:
                    player.charge += 1
            else:
                screen.blit(enemy.image, enemy.rect)
                enemy.draw_health_bar(screen)
        
        # End run if player is dead: clear enemies/bullets then exit loop cleanly
        if player.health <= 0:
            for enemy in list(enemies):
                enemy.kill()
            enemy_bullets.empty()
            player_bullets.empty()
            alive = False
            player.health = player.max_health
            return alive, player

        if supper == True:
            player.fix += 1
            if player.fix == 2:
                player.damage_mod = float(player.user_data["damage_mod"])
                player.fix = 0
                supper = False


        
        if bool(enemies) == False and reward_given == False:
            reward = Rewards("Reward","images\\RewardChest.png")
            reward.show(screen,(450,450))
            player = reward.speak(screen,player)
            reward_given = True
            del reward

        if player.rect.x in range(850,900) and bool(enemies) == False:
            print("This would generate the next room if it actually worked")
            break
                

        # Draw bullets
        player_bullets.draw(screen)
        enemy_bullets.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    return alive, player


####Fix meta upgrades####

####Fix the way to pull#####
