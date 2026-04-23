import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load Player Sprite
        sprite_sheet = pygame.image.load('images/spritesheet.webp').convert_alpha()
        sprite_rect = pygame.Rect(35, 159, 125, 200)
        self.image = sprite_sheet.subsurface(sprite_rect)
        self.image = pygame.transform.scale(self.image, (25, 40))
        self.rect = self.image.get_rect(center=(400, 350))

        # Load Weapon Sprite
        weapon_sheet = pygame.image.load("images/weapon.png").convert_alpha()
        weapon_rect = pygame.Rect(60, 180, 130, 90)
        self.weapon_surf_original = weapon_sheet.subsurface(weapon_rect)
        self.weapon_surf_original = pygame.transform.scale(self.weapon_surf_original, (32, 24))
        self.weapon_surf_original = pygame.transform.rotate(self.weapon_surf_original, -90)
        # Physics and State
        self.speed = 5
        self.floor_y = 460
        self.y_velocity = 0
        self.gravity = 0.8
        self.jump_strength = -12.5
        self.is_jumping = False
        
        # Attack Logic
        self.is_attacking = False
        self.attack_timer = 0
        self.weapon_rect = pygame.Rect(0, 0, 0, 0) # Initialize weapon rect

    def jump(self):
        if not self.is_jumping:
            self.y_velocity = self.jump_strength
            self.is_jumping = True

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = 10 # weapon shows for 10 frames

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 100:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 700:
            self.rect.x += self.speed
            
        # Gravity and Jumping
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity
        if self.rect.y >= self.floor_y:
            self.rect.y = self.floor_y
            self.y_velocity = 0
            self.is_jumping = False
            
        # Manage Attack Timer
        if self.attack_timer > 0:
            self.attack_timer -= 10
        else:
            self.is_attacking = False

    def draw_weapon(self, surface):
        if self.is_attacking:
            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Calculate angle between player center and mouse
            rel_x, rel_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery
            angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            
            # Rotate weapon based on angle
            weapon_rotated = pygame.transform.rotate(self.weapon_surf_original, int(angle))
            self.weapon_rect = weapon_rotated.get_rect(center=self.rect.center)
            
            # Position weapon at edge of player towards mouse
            distance = 30
            self.weapon_rect.x += math.cos(math.radians(-angle)) * distance
            self.weapon_rect.y += math.sin(math.radians(-angle)) * distance
            
            surface.blit(weapon_rotated, self.weapon_rect)
            return self.weapon_rect
        return None

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.image = pygame.image.load("images/spritesheet_2.png")
        self.smallest_char_rect = (660, 190, 97, 83)
        self.image = self.image.subsurface(self.smallest_char_rect)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2

    def update(self, target):
        if self.rect.x < target.rect.x: self.rect.x += self.speed
        elif self.rect.x > target.rect.x: self.rect.x -= self.speed
        if self.rect.y < target.rect.y: self.rect.y += self.speed
        elif self.rect.y > target.rect.y: self.rect.y -= self.speed

# Setup
player = Player()
enemy1 = Enemy("Drone", 150, 150)
all_sprites = pygame.sprite.Group(player, enemy1)
enemies = pygame.sprite.Group(enemy1)

running = True
x = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()
        # CHANGE: Detect Left Click for attack
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                player.attack()

    # 1. CLEAR THE SCREEN
    screen.fill((255, 255, 255))
    
    # 2. UPDATE SPRITES
    player.update()
    for enemy in enemies:
        enemy.update(player)
        
    # 3. DRAW ENVIRONMENT
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 100)) # Top
    pygame.draw.rect(screen, (0, 0, 0), (0, 500, 800, 100)) # Bottom
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 100, 600)) # Left
    pygame.draw.rect(screen, (0, 0, 0), (700, 0, 100, 600)) # Right
    
    # 4. DRAW SPRITES
    all_sprites.draw(screen)
    
    # 5. DRAW WEAPON & COLLISION
    current_weapon_rect = player.draw_weapon(screen)
    
    if current_weapon_rect:
        # Check for weapon collision
        for enemy in enemies:
            if current_weapon_rect.colliderect(enemy.rect):
                x += 1
                if x == 3:
                    enemy.kill()
                else:
                    print(x)
                
    # Enemy collision
    if pygame.sprite.spritecollide(player, enemies, False):
        print("Hit by an enemy!")
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
