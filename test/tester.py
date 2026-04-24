import pygame
import math
import random

# Ask for the number of enemies
try:
    num_enemies = int(input("How many enemies do you want to spawn? "))
except ValueError:
    num_enemies = 1

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            sprite_sheet = pygame.image.load('images/spritesheet.webp').convert_alpha()
            # Save original image to apply alpha effects later
            self.image_original = pygame.transform.scale(sprite_sheet.subsurface((35, 159, 125, 200)), (25, 40))
        except:
            self.image_original = pygame.Surface((25, 40)); self.image_original.fill((0, 0, 255))
        
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect(center=(400, 350))

        try:
            weapon_sheet = pygame.image.load("images/weapon.png").convert_alpha()
            self.weapon_surf_original = pygame.transform.scale(weapon_sheet.subsurface((60, 180, 130, 90)), (32, 24))
            self.weapon_surf_original = pygame.transform.rotate(self.weapon_surf_original, -90)
        except:
            self.weapon_surf_original = pygame.Surface((32, 24)); self.weapon_surf_original.fill((255, 0, 0))

        self.speed, self.floor_y, self.y_velocity = 5, 460, 0
        self.gravity, self.jump_strength = 0.8, -12.5
        self.is_jumping = False
        self.is_attacking, self.attack_timer = False, 0
        self.weapon_rect = pygame.Rect(0, 0, 0, 0)
        
        # New: Player I-frames
        self.iframes = 0

    def jump(self):
        if not self.is_jumping:
            self.y_velocity = self.jump_strength
            self.is_jumping = True

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = 15 

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 100: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 700: self.rect.x += self.speed

        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity
        if self.rect.y >= self.floor_y:
            self.rect.y, self.y_velocity, self.is_jumping = self.floor_y, 0, False

        if self.attack_timer > 0: self.attack_timer -= 1 
        else: self.is_attacking = False
        
        # Handle I-frame countdown and visual feedback
        if self.iframes > 0:
            self.iframes -= 1
            self.image.set_alpha(150) # Become semi-transparent
        else:
            self.image.set_alpha(255) # Fully visible

    def draw_weapon(self, surface):
        if self.is_attacking:
            mx, my = pygame.mouse.get_pos()
            rel_x, rel_y = mx - self.rect.centerx, my - self.rect.centery
            angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            weapon_rotated = pygame.transform.rotate(self.weapon_surf_original, int(angle))
            self.weapon_rect = weapon_rotated.get_rect(center=self.rect.center)
            dist = 35 
            self.weapon_rect.centerx += math.cos(math.radians(-angle)) * dist
            self.weapon_rect.centery += math.sin(math.radians(-angle)) * dist
            surface.blit(weapon_rotated, self.weapon_rect)
            return self.weapon_rect
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
        self.speed, self.health = 2, 3
        self.hit_cooldown = 0 

    def update(self, target, others):
        dx, dy = target.rect.x - self.rect.x, target.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        if dist > 0:
            self.rect.x += (dx / dist) * self.speed
            self.rect.y += (dy / dist) * self.speed

        for other in others:
            if other != self and self.rect.colliderect(other.rect):
                if self.rect.x < other.rect.x: self.rect.x -= 1
                else: self.rect.x += 1

        if self.hit_cooldown > 0: self.hit_cooldown -= 1

def setup():
    player = Player()
    all_sprites, enemies = pygame.sprite.Group(player), pygame.sprite.Group()

    for i in range(num_enemies):
        new_enemy = Enemy(random.randint(150, 650), random.randint(150, 450))
        enemies.add(new_enemy); all_sprites.add(new_enemy)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: player.jump()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: player.attack()

        screen.fill((255, 255, 255))
        player.update()
        enemies.update(player, enemies)

        # Environment
        for wall in [(0,0,800,100), (0,500,800,100), (0,0,100,600), (700,0,100,600)]:
            pygame.draw.rect(screen, (0,0,0), wall)

        all_sprites.draw(screen)
        
        # Weapon Collision logic
        weapon_hitbox = player.draw_weapon(screen)
        if weapon_hitbox:
            for enemy in enemies:
                if weapon_hitbox.colliderect(enemy.rect) and enemy.hit_cooldown == 0:
                    enemy.health -= 1
                    print("hit")
                    enemy.hit_cooldown = 20 
                    if enemy.health <= 0: enemy.kill()

        # NEW: Player hit check with I-frames
        if player.iframes == 0:
            if pygame.sprite.spritecollide(player, enemies, False):
                print("player hit")
                player.iframes = 60 # Invincible for 1 second (60 frames)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

setup()
