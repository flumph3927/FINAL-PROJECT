        # Floor collision
        if self.rect.bottom >= FLOOR_BOTTOM_Y:
            self.rect.bottom = FLOOR_BOTTOM_Y
            self.y_velocity = 0
            self.is_jumping = False
            landed = True

        # Platform collision
        if not landed and self.y_velocity > 0:
            for plat in platforms:
                if self.rect.colliderect(plat.sprite_rect):
                    if self.rect.bottom - self.y_velocity <= plat.sprite_rect.top + 5:
                        self.rect.bottom = plat.sprite_rect.top  # ← also uses rect.bottom
                        self.y_velocity = 0
                        self.is_jumping = False
                        landed = True
                        break